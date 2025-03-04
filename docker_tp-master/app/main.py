from loguru import logger
from src.data_loader import load_data
from src.eda import eda
from src.model import predict, train_model
from src.utils import setup_logging


def main():
    logger.info("Démarrage de l'application")
    setup_logging()  # Configurer les logs
    logger.debug("Démarrage de l'application en mode debug")
    
    # Charger les données
    df = load_data()
    
    # Navigation
    st.sidebar.title("Navigation")
    choice = st.sidebar.radio("Choisissez une section", ["EDA", "Entraînement du Modèle", "Prédiction"])
    
    if choice == "EDA":
        eda(df)
    elif choice == "Entraînement du Modèle":
        model, scaler, label_encoder = train_model(df)
    elif choice == "Prédiction":
        model, scaler, label_encoder = train_model(df)
        predict(model, scaler, label_encoder)
    
    logger.info("Application terminée")

if __name__ == "__main__":
    import streamlit as st
    main()
