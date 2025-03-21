# Auth Service

<img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI" width="280" height="100">

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/React-icon.svg/512px-React-icon.svg.png" alt="React" width="110" height="90">

Это полноценный сервис аутентификации, который объединяет **бэкенд** (FastAPI) и **фронтенд** (React). Сервис поддерживает OAuth2-аутентификацию через провайдеров (**Google**, **Yandex**, **GitHub**) и использует JWT для управления токенами доступа и обновления.

---

## Основные компоненты проекта:

### 1. Бэкенд 



Бэкенд реализован на основе **FastAPI** — современного веб-фреймворка для создания высокопроизводительных API. Он отвечает за:

- Аутентификацию через OAuth2.
- Генерацию и управление JWT-токенами.
- Взаимодействие с PostgreSQL.

- [Документация](backend/README.md)

---

### 2. Фронтенд

Фронтенд реализован с использованием **React** — популярной библиотеки для создания пользовательских интерфейсов. Он предоставляет:

- Интерфейс для входа через OAuth2.
- Управление состоянием пользователя.
- Отображение данных, полученных от бэкенда.

- [Документация](frontend/README.md)

---

#### Клонируйте репозиторий:

```bash
git clone https://github.com/BaranovSerV/auth_service.git
```