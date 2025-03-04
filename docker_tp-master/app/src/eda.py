import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from loguru import logger


# Dictionnaire pour mapper les noms de colonnes aux descriptions complètes
column_descriptions = {
    "age": "Âge (numérique)",
    "job": "Type d'emploi (catégoriel)",
    "marital": "Statut matrimonial (catégoriel)",
    "education": "Niveau d'éducation (catégoriel)",
    "default": "Crédit en défaut ? (catégoriel)",
    "housing": "Prêt immobilier ? (catégoriel)",
    "loan": "Prêt personnel ? (catégoriel)",
    "contact": "Type de communication (catégoriel)",
    "month": "Mois du dernier contact (catégoriel)",
    "day_of_week": "Jour de la semaine du dernier contact (catégoriel)",
    "duration": "Durée du dernier contact (en secondes, numérique)",
    "campaign": "Nombre de contacts pendant cette campagne (numérique)",
    "pdays": "Jours écoulés depuis le dernier contact (numérique)",
    "previous": "Nombre de contacts avant cette campagne (numérique)",
    "poutcome": "Résultat de la campagne précédente (catégoriel)",
    "emp.var.rate": "Taux de variation de l'emploi (indicateur trimestriel, numérique)",
    "cons.price.idx": "Indice des prix à la consommation (indicateur mensuel, numérique)",
    "cons.conf.idx": "Indice de confiance des consommateurs (indicateur mensuel, numérique)",
    "euribor3m": "Taux Euribor à 3 mois (indicateur quotidien, numérique)",
    "nr.employed": "Nombre d'employés (indicateur trimestriel, numérique)",
    "y": "Souscription à un dépôt à terme ? (binaire)",
}


def eda(df: pd.DataFrame) -> None:
    """
    Effectue l'analyse exploratoire des données.
    Args:
        df (pd.DataFrame): Données à analyser
    """
    logger.info("Début de l'analyse exploratoire")

    # Vue générale des données
    st.subheader("Vue générale des données")
    st.write(df.head())

    # Statistiques descriptives
    st.subheader("Statistiques descriptives")
    st.write(df.describe())

    # Distribution des variables catégorielles
    st.subheader("Distribution des variables catégorielles")
    for col in df.select_dtypes(include=["object"]).columns:
        if col in column_descriptions:  # Utiliser le nom complet si disponible
            title = f"Distribution de {column_descriptions[col]}"
        else:
            title = f"Distribution de {col}"
        fig = px.histogram(df, x=col, title=title)
        st.plotly_chart(fig, use_container_width=True)

    # Distribution des variables numériques
    st.subheader("Distribution des variables numériques")
    for col in df.select_dtypes(include=["float64", "int64"]).columns:
        if col in column_descriptions:  # Utiliser le nom complet si disponible
            title = f"Distribution de {column_descriptions[col]}"
        else:
            title = f"Distribution de {col}"
        fig = px.histogram(df, x=col, title=title, nbins=50)
        st.plotly_chart(fig, use_container_width=True)

    # Boxplot des variables numériques
    st.subheader("Boxplot des variables numériques")
    for col in df.select_dtypes(include=["float64", "int64"]).columns:
        if col in column_descriptions:  # Utiliser le nom complet si disponible
            title = f"Boxplot de {column_descriptions[col]}"
        else:
            title = f"Boxplot de {col}"
        fig = px.box(df, y=col, title=title)
        st.plotly_chart(fig, use_container_width=True)

    # Nuage de points pour les relations entre variables numériques
    st.subheader("Relations entre variables numériques")
    numeric_columns = df.select_dtypes(include=["float64", "int64"]).columns
    if len(numeric_columns) >= 2:
        x_axis = st.selectbox(
            "Sélectionnez la variable pour l'axe X :", numeric_columns
        )
        y_axis = st.selectbox(
            "Sélectionnez la variable pour l'axe Y :", numeric_columns
        )
        if x_axis in column_descriptions and y_axis in column_descriptions:
            title = f"{column_descriptions[x_axis]} vs {column_descriptions[y_axis]}"
        else:
            title = f"{x_axis} vs {y_axis}"
        fig = px.scatter(df, x=x_axis, y=y_axis, title=title)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning(
            "Moins de deux colonnes numériques disponibles pour créer un nuage de points."
        )

    # Matrice de corrélation (seulement pour les colonnes numériques)
    st.subheader("Matrice de corrélation")
    numeric_df = df.select_dtypes(include=["float64", "int64"])
    if not numeric_df.empty:
        corr_matrix = numeric_df.corr()
        fig = go.Figure(
            data=go.Heatmap(
                z=corr_matrix,
                x=corr_matrix.columns,
                y=corr_matrix.columns,
                colorscale="RdBu",  # Correction ici
                zmin=-1,
                zmax=1,
            )
        )
        fig.update_layout(
            title="Matrice de corrélation",
            xaxis_nticks=len(corr_matrix.columns),
            yaxis_nticks=len(corr_matrix.columns),
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning(
            "Aucune colonne numérique disponible pour calculer la matrice de corrélation."
        )

    # Distribution de la variable cible (si elle existe)
    if "y" in df.columns:
        st.subheader("Distribution de la variable cible (y)")
        title = f"Répartition de {column_descriptions['y']}"
        fig = px.pie(df, names="y", title=title)
        st.plotly_chart(fig, use_container_width=True)

        # Relation entre les variables numériques et la variable cible
        st.subheader("Relation entre les variables numériques et la cible")
        for col in df.select_dtypes(include=["float64", "int64"]).columns:
            if col in column_descriptions:
                title = f"{column_descriptions[col]} vs {column_descriptions['y']}"
            else:
                title = f"{col} vs y"
            fig = px.box(df, x="y", y=col, title=title)
            st.plotly_chart(fig, use_container_width=True)

    logger.info("Analyse exploratoire terminée")
