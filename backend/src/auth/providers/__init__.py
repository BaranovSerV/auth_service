from src.auth.providers.base_auth import Auth
from src.auth.providers.google import GoogleAuth
from src.auth.providers.yandex import YandexAuth
from src.auth.providers.github import GithubAuth


OAUTH_PROVIDERS = {
    "google": GoogleAuth,
    "yandex": YandexAuth,
    "github": GithubAuth,
}

__all__ = ["Auth", "GoogleAuth", "YandexAuth", "GithubAuth"]
