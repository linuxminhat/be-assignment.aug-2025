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

# Debug print (masking secrets)
if __name__ == "__main__":
    print("database_url:", settings.database_url)
    print("redis_url:", settings.redis_url)
    print("secret_key:", settings.secret_key[:4] + "..." if settings.secret_key else None)
    print("algorithm:", settings.algorithm)
    print("access_token_expire_minutes:", settings.access_token_expire_minutes)
    print("debug:", settings.debug)
    print("log_level:", settings.log_level)
    print("max_file_size:", settings.max_file_size)
    print("max_files_per_task:", settings.max_files_per_task)
    print("upload_dir:", settings.upload_dir)
