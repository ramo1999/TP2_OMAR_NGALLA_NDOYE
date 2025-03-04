from loguru import logger


def setup_logging() -> None:
    """
    Configure les logs avec Loguru.
    """
    logger.add(
        "logs/app.log", rotation="10 MB", level="DEBUG", backtrace=True, diagnose=True
    )
