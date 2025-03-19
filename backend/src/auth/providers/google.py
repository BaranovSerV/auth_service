from urllib.parse import urlencode

import httpx
from fastapi import HTTPException

from src.auth.providers import Auth
from src.settings import settings


class GoogleAuth(Auth):
    def __init__(self):
        self.client_id = settings.GOOGLE_CLIENT_ID
        self.client_secret = settings.GOOGLE_CLIENT_SECRET
        self.redirect_uri = settings.GOOGLE_REDIRECT_URI


    def get_auth_url(self) -> str:
        google_auth_url = "https://accounts.google.com/o/oauth2/auth"
        params = {
            "response_type": "code",
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri, 
            "scope": "openid email profile",  
            "access_type": "offline",
        }
    
        auth_url = f"{google_auth_url}?{urlencode(params)}"
        return auth_url

    async def exchange_code_for_token(self, code: str) -> str:
        token_url = "https://oauth2.googleapis.com/token"
        data = {
            "code": code,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "redirect_uri": self.redirect_uri,
            "grant_type": "authorization_code",
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(token_url, data=data)
            if response.status_code != 200:
                raise HTTPException(status_code=400, detail="Ошибка получения токена")
            tokens = response.json()
            return tokens.get("access_token")


    async def get_user_info(self, access_token: str) -> dict:
        user_info_url = "https://www.googleapis.com/oauth2/v1/userinfo"
        headers = {"Authorization": f"Bearer {access_token}"}
        async with httpx.AsyncClient() as client:
            response = await client.get(user_info_url, headers=headers)
            if response.status_code != 200:
                raise HTTPException(
                    status_code=400, 
                    detail="Ошибка получения данных пользователя"
                )
            return response.json()

