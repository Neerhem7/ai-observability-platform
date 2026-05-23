from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    DATABASE_URL = os.getenv("DATABASE_URL")

    REDIS_URL = os.getenv("REDIS_URL")

    API_PORT = int(
        os.getenv("API_PORT", 8000)
    )


settings = Settings()
