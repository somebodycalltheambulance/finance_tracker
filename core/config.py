from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Finance Tracker"
    secret_key: str = "supersecretkey"
    algorithm: str = "HS256"
    database_url: str
    access_token_expire_minutes: int = 30

    class Config:
        from_attributes = True

settings = Settings()
