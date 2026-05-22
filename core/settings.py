from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ORIGINS: str
    ROOT_PATH: str
    ENV: str
    LOG_LEVEL: str
    PORT: int

    ACCESS_TOKEN_EXPIRE_MINUTES: int
    SECRET_AUTH_KEY: SecretStr
    AUTH_ALGORITHM: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
