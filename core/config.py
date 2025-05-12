from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Finance Tracker"
    secret_key: str
    database_url: str

    class Config:
        from_attributes = True

settings = Settings()
