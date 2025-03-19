from pprint import pformat


from src.logger import logger
from src.auth.providers import OAUTH_PROVIDERS 
from src.auth.repository import AuthRepository
from src.auth.validator import AUTH_VALIDATORS


class AuthService:
    def __init__(self, auth_repository: AuthRepository):
        self.auth_repository = auth_repository


    async def get_auth_url(self, provider: str) -> str:
        logger.info(f"Создание ссылки на провайдер: {provider}")

        oauth_provider = OAUTH_PROVIDERS[provider]()
        auth_url = oauth_provider.get_auth_url()
        
        return auth_url


    async def auth(self, code: str, provider: str):
        oauth_provider = OAUTH_PROVIDERS[provider]()

        access_token = await oauth_provider.exchange_code_for_token(code)
        logger.info(f"Получен access_token от провайдера: {provider}")

        user_info = await oauth_provider.get_user_info(access_token)
        logger.debug(f"USER_INFO:\n{pformat(user_info, indent=4)}")

        validator = AUTH_VALIDATORS[provider]()
        
        user_data = validator.get_data(user_info)

        user = await self.auth_repository.get_or_create(user_data.model_dump())

        return {"email": user.email}
    


