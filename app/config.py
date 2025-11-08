from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import model_validator, Field

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    DATABASE_URL: Optional[str] = Field(None)

    @model_validator(mode='after')
    def get_database_url(self) -> 'Settings':
        """
        Генерирует DATABASE_URL после того, как все поля успешно загружены.
        
        """
        self.DATABASE_URL = f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return self

    model_config = SettingsConfigDict(env_file=".env", extra='ignore')

settings = Settings()