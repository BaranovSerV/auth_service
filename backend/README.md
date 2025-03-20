# Auth Service Backend

This is an authentication service built with FastAPI, which supports OAuth2 authentication with multiple providers (Google, Yandex, GitHub) and JWT-based access and refresh tokens.

## Features:

- OAuth2 login with Google, Yandex, and GitHub
- JWT-based authentication (Access and Refresh tokens)

## Stack:

1. **FastAPI** ![FastAPI](https://img.shields.io/badge/FastAPI-0.115.11-blue)

2. **PyJWT** ![PyJWT](https://img.shields.io/badge/PyJWT-2.10.1-yellow)

3. **Pydantic** ![Pydantic](https://img.shields.io/badge/Pydantic-2.10.6-green)

4. **PostgreSQL** ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16.2-blueviolet)

5. **pytest** ![pytest](https://img.shields.io/badge/pytest-8.3.5-lightgray)

6. **Loguru** ![Loguru](https://img.shields.io/badge/Loguru-0.7.3-blue)

## Start project:

### Create `.env` file:

```bash
# API Settings
API_HOST = "0.0.0.0"
API_PORT = 8000

# Frontend Settings
FRONTEND_BASE_URL= "frontend_url"

# PostgreSQL Settings
POSTGRES_HOST = "localhost"
POSTGRES_PORT = 5432
POSTGRES_USER = "your_postgres_user"
POSTGRES_DB = "your_postgres_db"
POSTGRES_PASSWORD = "your_postgres_password"
POSTGRES_DRIVER = "postgresql+asyncpg"

# JWT Settings
SECRET_KEY = "your_jwt_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7

# OAuth Settings
GOOGLE_CLIENT_ID = "your_google_client_id"
GOOGLE_CLIENT_SECRET = "your_google_client_secret"
GOOGLE_REDIRECT_URI = "your_google_redirect_uri"

YANDEX_CLIENT_ID = "your_yandex_client_id"
YANDEX_CLIENT_SECRET = "your_yandex_client_secret"
YANDEX_REDIRECT_URI = "your_yandex_redirect_uri"

GITHUB_CLIENT_ID = "your_github_client_id"
GITHUB_CLIENT_SECRET = "your_github_client_secret"
GITHUB_REDIRECT_URI = "your_github_redirect_uri"
```

### Docker Compose Setup:

This docker-compose.yml defines two services: `app` and `db`.

```bash
 docker-compose up -d
 ```