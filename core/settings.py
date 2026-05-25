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

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: SecretStr
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    @property
    def DATABASE_URL(self):
        passwd = self.POSTGRES_PASSWORD.get_secret_value()
        return f"postgresql://{self.POSTGRES_USER}:{passwd}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
