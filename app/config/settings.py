from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MODEL_NAME: str = "gemini-2.5-flash"

    GEMINI_API_KEY: str

    BASE_URL: str

    TEMPERATURE: float = 0.8

    MAX_TOKENS: int = 5000

    class Config():
        env_file = ".env"

settings = Settings()