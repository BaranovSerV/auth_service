from urllib.parse import urlencode

import httpx
from fastapi import HTTPException

from src.auth.providers import Auth
from src.settings import settings


class YandexAuth(Auth):
    def __init__(self):
        self.client_id = settings.YANDEX_CLIENT_ID
        self.client_secret = settings.YANDEX_CLIENT_SECRET
        self.redirect_uri = settings.YANDEX_REDIRECT_URI


    def get_auth_url(self) -> str:
        yandex_auth_url = "https://oauth.yandex.ru/authorize"
        params = {
            "response_type": "code",
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
        }

        return f"{yandex_auth_url}?{urlencode(params)}"
  

    async def exchange_code_for_token(self, code: str) -> str:
        token_url = "https://oauth.yandex.ru/token"
        data = {
            "grant_type": "authorization_code",
            "code": code,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(token_url, data=data)
            if response.status_code != 200:
                raise HTTPException(status_code=400, detail="Ошибка получения токена")
            tokens = response.json()
            return tokens.get("access_token")


    async def get_user_info(self, access_token: str) -> dict:
        user_info_url = "https://login.yandex.ru/info"
        headers = {"Authorization": f"OAuth {access_token}"}

        async with httpx.AsyncClient() as client:
            response = await client.get(user_info_url, headers=headers)
            if response.status_code != 200:
                raise HTTPException(
                    status_code=400, 
                    detail="Ошибка получения данных пользователя"
                )
            return response.json()

