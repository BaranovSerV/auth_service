from urllib.parse import urlencode

import httpx
from fastapi import HTTPException

from src.auth.providers import Auth
from src.settings import settings


class GithubAuth(Auth):
    def __init__(self):
        self.client_id = settings.GITHUB_CLIENT_ID
        self.client_secret = settings.GITHUB_CLIENT_SECRET
        self.redirect_uri = settings.GITHUB_REDIRECT_URI


    def get_auth_url(self) -> str:
        github_auth_url = "https://github.com/login/oauth/authorize"
        params = {
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "scope": "user:email",  
        }
        return f"{github_auth_url}?{urlencode(params)}"
    

    async def exchange_code_for_token(self, code: str) -> str:
        token_url = "https://github.com/login/oauth/access_token"
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": code,
        }
        headers = {"Accept": "application/json"}

        async with httpx.AsyncClient() as client:
            response = await client.post(token_url, data=data, headers=headers)
            if response.status_code != 200:
                raise HTTPException(status_code=400, detail="Ошибка получения токена")
            tokens = response.json()
            return tokens.get("access_token")
   

    async def get_user_info(self, access_token: str) -> dict:
        user_info_url = "https://api.github.com/user"
        headers = {
            "Authorization": f"token {access_token}", 
            "Accept": "application/json"
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(user_info_url, headers=headers)
            if response.status_code != 200:
                raise HTTPException(
                    status_code=400, 
                    detail="Ошибка получения данных пользователя"
                )
            user_data = response.json()

            emails_url = "https://api.github.com/user/emails"
            emails_response = await client.get(emails_url, headers=headers)
            if emails_response.status_code == 200:
                emails = emails_response.json()
                primary_email = next(
                    (email["email"] for email in emails if email["primary"]), None
                )
                user_data["email"] = primary_email

        return user_data
