from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Database
    database_url: str

    # Redis
    redis_url: str

    # JWT
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # Application
    debug: bool = True
    log_level: str = "INFO"

    # File Upload
    max_file_size: int = 5242880  # 5MB in bytes
    max_files_per_task: int = 3
    upload_dir: str = "uploads"

    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parents[1] / ".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",  # allow POSTGRES_* extras in .env
    )



settings = Settings()
