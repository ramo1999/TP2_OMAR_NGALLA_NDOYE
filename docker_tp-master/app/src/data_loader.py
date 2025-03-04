import os
from pathlib import Path

import pandas as pd
from loguru import logger


def load_data() -> pd.DataFrame:
    """
    Charge le dataset Bank Marketing.
    Returns:
        pd.DataFrame: Données chargées
    """
    logger.info("Chargement des données")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    current_dir = Path(current_dir)
    csv_file = current_dir.parent.absolute() / "data" / "bank-additional-full.csv"

    logger.debug(csv_file)
    df = pd.read_csv(csv_file, sep=";")
    logger.info(f"Données chargées : {df.shape}")
    return df
