# Autn Service Backend

Это сервис аутентификации, созданный с использованием FastAPI, который поддерживает OAuth2-аутентификацию через несколько провайдеров (Google, Yandex, GitHub) и использует JWT для access и refresh токенов.

## Возможности:

- OAuth2 вход через Google, Yandex и GitHub
- Аутентификация на основе JWT 

## Стек технологий:

1. **FastAPI** ![FastAPI](https://img.shields.io/badge/FastAPI-0.115.11-blue)

2. **PyJWT** ![PyJWT](https://img.shields.io/badge/PyJWT-2.10.1-yellow)

3. **Pydantic** ![Pydantic](https://img.shields.io/badge/Pydantic-2.10.6-green)

4. **PostgreSQL** ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16.2-blueviolet)

5. **pytest** ![pytest](https://img.shields.io/badge/pytest-8.3.5-lightgray)

6. **Loguru** ![Loguru](https://img.shields.io/badge/Loguru-0.7.3-blue)

## Запуск проекта:

### 1. Создание файла `.env`:

```bash
# Настройки API
API_HOST = "0.0.0.0"
API_PORT = 8000

# Настройки фронтенда
FRONTEND_BASE_URL= "frontend_url"

# Настройки PostgreSQL
POSTGRES_HOST = "localhost"
POSTGRES_PORT = 5432
POSTGRES_USER = "your_postgres_user"
POSTGRES_DB = "your_postgres_db"
POSTGRES_PASSWORD = "your_postgres_password"
POSTGRES_DRIVER = "postgresql+asyncpg"

# Настройки JWT
SECRET_KEY = "your_jwt_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7

# Настройки OAuth
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

### 2. Запуск docker-compose:

#### 1-й способ (Запуск через `docker-compose.yml`
):

Для запуска 2 два сервиса: Fastapi и PostgreSQL:

```bash
 docker-compose up -d
 ```

#### 2-й способ (Запуск через `docker-compose.test.yml`
):

В этом случае запустится только PostgresSQL:

```bash
docker-compose -f docker-compose.test.yml up -d
```

Установка зависимостей:

```bash
pip install -r requirements.txt
```

Запуск Fastapi приложения:

```bash
python -m src.main 
```

#### Миграция БД:

После запуска контейнера выполните миграции базы данных с помощью Alembic:

```bash
alembic upgrade head
```


