from fastapi import Depends, Cookie, status, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.repository import AuthRepository
from src.auth.service import AuthService
from src.auth.exception import InvalidTokenError, ExpiredTokenError
from src.auth.token import decode_token
from src.dependency import get_db_session
from src.logger import logger


async def get_auth_repository(
    db_session: AsyncSession = Depends(get_db_session)
):
    return AuthRepository(db_session)


async def get_auth_service(
    auth_repository: AuthRepository = Depends(get_auth_repository)
):
    return AuthService(auth_repository)


async def get_current_refresh_token_payload(
    refresh_token: str = Cookie(None)
):
    if not refresh_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Access token is missing",
        )

    try:
        payload = decode_token(refresh_token)
        return payload
    except ExpiredTokenError:
        raise HTTPException(status_code=401, detail="Access token expired")

    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid access token")


async def get_current_access_token_payload(
    request: Request
) -> dict:
    authorization: str = request.headers.get("Authorization")
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,

            detail="Authorization header is missing",
        )


    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,

            detail="Invalid token prefix. Expected 'Bearer'",
        )

    access_token = authorization[7:]

    try:
        payload = decode_token(access_token)
        logger.info(f"Декодирование прошло успешно")

        return payload
    except ExpiredTokenError:
        raise HTTPException(status_code=401, detail="Access token expired")
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid access token")



async def get_current_auth_user(
    f: dict = Depends(get_current_refresh_token_payload),
    payload: dict = Depends(get_current_access_token_payload),
    auth_repository: AuthRepository = Depends(get_auth_repository)
) -> dict:
    
    email = payload.get("email")

    if not email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload",
        )

    user = await auth_repository.get_or_create(payload)

    return user
