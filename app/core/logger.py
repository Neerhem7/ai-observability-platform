from loguru import logger


logger.add(
    "logs/platform.log",
    rotation="10 MB",
    level="INFO"
)
