from pydantic_settings import BaseSettings, SettingsConfigDict


class API(BaseSettings):
    API_HOST: str
    API_PORT: int


class Frontend(BaseSettings):
    FRONTEND_BASE_URL: str


class Postgres(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_PASSWORD: str
    POSTGRES_DRIVER: str
    
    @property
    def postgres_url(self):
        return (
            f"{self.POSTGRES_DRIVER}://{self.POSTGRES_USER}:"\
            f"{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:"\
            f"{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


class JWT(BaseSettings):
    SECRET_KEY: str  
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS: int

class Google(BaseSettings):
    GOOGLE_CLIENT_ID: str 
    GOOGLE_CLIENT_SECRET: str
    GOOGLE_REDIRECT_URI: str


class Yandex(BaseSettings):
    YANDEX_CLIENT_ID: str 
    YANDEX_CLIENT_SECRET: str
    YANDEX_REDIRECT_URI: str


class Github(BaseSettings):
    GITHUB_CLIENT_ID: str 
    GITHUB_CLIENT_SECRET: str
    GITHUB_REDIRECT_URI: str


class Settings(
    Google, 
    Yandex, 
    Github, 
    Postgres, 
    JWT, 
    Frontend,
    API
):
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
