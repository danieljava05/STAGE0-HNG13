from pydantic_settings import BaseSettings, SettingsConfigDict

class settings(BaseSettings):
    EMAIL : str
    NAME : str
    STACK :str
    FACT_URL : str
    


    model_config = SettingsConfigDict(
        env_file = "src/.env",
        extra = "ignore"
    )

Config = settings()