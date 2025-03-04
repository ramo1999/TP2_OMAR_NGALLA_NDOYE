from typing import Any, Optional, Tuple

import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import streamlit as st
from loguru import logger
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler


def train_model(
    df: pd.DataFrame,
) -> Tuple[
    Optional[RandomForestClassifier], Optional[StandardScaler], Optional[LabelEncoder]
]:
    """
    Entraîne un modèle de classification et affiche les résultats.
    Args:
        df (pd.DataFrame): Données à utiliser pour l'entraînement
    Returns:
        tuple: Modèle entraîné, scaler, et label encoder
    """
    logger.info("Début de l'entraînement du modèle")

    # Vérifier si la colonne cible 'y' existe
    if "y" not in df.columns:
        st.error("La colonne cible 'y' est manquante dans le dataset.")
        return None, None, None

    # Prétraitement des données
    df = df.dropna()  # Supprimer les lignes avec des valeurs manquantes
    X = df.drop("y", axis=1)  # Features
    y = df["y"]  # Target

    # Initialisation du label encoder si nécessaire
    label_encoder = None
    if y.dtype == "object":  # Si la cible est catégorielle
        label_encoder = LabelEncoder()
        y = label_encoder.fit_transform(y)

    # Encodage des variables catégorielles dans X
    X = pd.get_dummies(X, drop_first=True)

    # Initialisation et application du scaler
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Division en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.3, random_state=42
    )

    # Entraînement du modèle
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Prédictions
    y_pred = model.predict(X_test)

    # Affichage des résultats
    st.subheader("Résultats du modèle")

    # 1. Rapport de classification
    st.markdown("### Rapport de classification")
    classification_report_dict = classification_report(y_test, y_pred, output_dict=True)
    classification_report_df = pd.DataFrame(classification_report_dict).transpose()
    st.dataframe(classification_report_df.style.highlight_max(axis=0))

    # 2. Matrice de confusion
    st.markdown("### Matrice de confusion")
    conf_matrix = confusion_matrix(y_test, y_pred)
    if label_encoder is not None:
        labels = sorted(label_encoder.classes_)  # Récupérer les labels originaux
    else:
        labels = sorted(np.unique(y))  # Utiliser les valeurs uniques de y
    fig = ff.create_annotated_heatmap(
        z=conf_matrix, x=labels, y=labels, colorscale="Blues"
    )
    fig.update_layout(
        title="Matrice de confusion",
        xaxis_title="Prédictions",
        yaxis_title="Valeurs réelles",
    )
    st.plotly_chart(fig, use_container_width=True)

    # 3. Précision globale
    accuracy = accuracy_score(y_test, y_pred)
    st.markdown("### Précision globale")
    st.metric(label="Précision", value=f"{accuracy:.2%}")

    # 4. Importance des caractéristiques
    st.markdown("### Importance des caractéristiques")
    feature_importances = pd.Series(
        model.feature_importances_, index=X.columns
    ).sort_values(ascending=False)
    fig = px.bar(
        feature_importances,
        x=feature_importances.values,
        y=feature_importances.index,
        title="Importance des caractéristiques",
        labels={"x": "Importance", "y": "Caractéristiques"},
    )
    st.plotly_chart(fig, use_container_width=True)

    logger.info("Entraînement du modèle terminé")

    return model, scaler, label_encoder


def predict(model: Any, scaler: Any, label_encoder: Any) -> None:
    """
    Effectue une prédiction avec le modèle entraîné.
    Args:
        model (Any): Modèle entraîné
        scaler (Any): Scaler utilisé pour la normalisation
        label_encoder (Any): LabelEncoder utilisé pour l'encodage
    """
    logger.info("Début de la prédiction")

    # Formulaire pour saisir les données
    st.subheader("Saisie des données pour la prédiction")
    form = st.form(key="prediction_form")
    age = form.number_input("Âge", min_value=18, max_value=100)
    job = form.selectbox("Profession", label_encoder.classes_)
    marital = form.selectbox("État civil", label_encoder.classes_)
    education = form.selectbox("Éducation", label_encoder.classes_)
    default = form.selectbox("Default", label_encoder.classes_)
    housing = form.selectbox("Housing Loan", label_encoder.classes_)
    loan = form.selectbox("Personal Loan", label_encoder.classes_)
    contact = form.selectbox("Contact", label_encoder.classes_)
    month = form.selectbox("Month", label_encoder.classes_)
    day_of_week = form.selectbox("Day of Week", label_encoder.classes_)
    duration = form.number_input("Duration", min_value=0)
    campaign = form.number_input("Campaign", min_value=1)
    pdays = form.number_input("Pdays", min_value=0)
    previous = form.number_input("Previous", min_value=0)
    poutcome = form.selectbox("Poutcome", label_encoder.classes_)
    emp_var_rate = form.number_input("Employment Variation Rate", min_value=0.0)
    cons_price_idx = form.number_input("Consumer Price Index", min_value=0.0)
    cons_conf_idx = form.number_input("Consumer Confidence Index", min_value=0.0)
    euribor3m = form.number_input("Euribor 3 Month Rate", min_value=0.0)
    nr_employed = form.number_input("Number of Employed", min_value=0.0)

    if form.form_submit_button("Prédire"):
        # Création du DataFrame
        data = {
            "age": age,
            "job": job,
            "marital": marital,
            "education": education,
            "default": default,
            "housing": housing,
            "loan": loan,
            "contact": contact,
            "month": month,
            "day_of_week": day_of_week,
            "duration": duration,
            "campaign": campaign,
            "pdays": pdays,
            "previous": previous,
            "poutcome": poutcome,
            "emp.var.rate": emp_var_rate,
            "cons.price.idx": cons_price_idx,
            "cons.conf.idx": cons_conf_idx,
            "euribor3m": euribor3m,
            "nr.employed": nr_employed,
        }
        df = pd.DataFrame([data])

        # Encodage des variables catégorielles (comme pendant l'entraînement)
        df_encoded = pd.get_dummies(df, drop_first=True)

        # S'assurer que les colonnes correspondent à celles utilisées pendant l'entraînement
        # Ajouter les colonnes manquantes (avec des valeurs 0)
        missing_cols = set(scaler.feature_names_in_) - set(df_encoded.columns)
        for col in missing_cols:
            df_encoded[col] = 0

        # Réordonner les colonnes pour correspondre au scaler
        df_encoded = df_encoded[scaler.feature_names_in_]

        # Normalisation des données
        df_scaled = scaler.transform(df_encoded)

        # Prédiction
        prediction = model.predict(df_scaled)
        st.subheader("Résultat de la prédiction")
        st.write(f"Le modèle prédit : {label_encoder.inverse_transform(prediction)[0]}")

    logger.info("Prédiction terminée")