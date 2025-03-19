from abc import ABC, abstractmethod

from src.auth.shemas import UserAuthShema


class AuthDataValidator(ABC):
    @abstractmethod
    def get_data(self, user_data: dict) -> UserAuthShema:
        pass


class GoogleAuthDataValidator(AuthDataValidator):
    def get_data(self, user_data: dict) -> UserAuthShema:
        email = user_data.get("email")

        return UserAuthShema(email=email)


class YandexAuthDataValidator(AuthDataValidator):
    def get_data(self, user_data: dict) -> UserAuthShema:
        email = user_data.get("default_email")

        return UserAuthShema(email=email)


class GithubAuthDataValidator(AuthDataValidator):
    def get_data(self, user_data: dict) -> UserAuthShema:
        email = user_data.get("email")

        return UserAuthShema(email=email)


AUTH_VALIDATORS = {
    "google": GoogleAuthDataValidator,
    "yandex": YandexAuthDataValidator,
    "github": GithubAuthDataValidator,
}
