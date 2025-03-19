from datetime import timedelta

from fastapi import APIRouter, HTTPException, Depends, Response
from fastapi.responses import RedirectResponse

from src.auth.service import AuthService
from src.auth.dependency import get_auth_service, get_current_refresh_token_payload
from src.auth.token import create_token 
from src.settings import settings


router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.get("/{provider}/login")
async def oauth_login(
    provider: str,
    auth_service: AuthService = Depends(get_auth_service)
):
    auth_url = await auth_service.get_auth_url(provider)
    return RedirectResponse(auth_url) 


@router.get("/{provider}/callback")
async def oauth_callback(
    response: Response,
    provider: str, 
    code: str, 
    auth_service: AuthService = Depends(get_auth_service)
):
    user_data = await auth_service.auth(code, provider)
    
    access_token = create_token(
        user_data, 
        timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    )

    refresh_token = create_token(
        user_data, 
        timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    )
    
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        samesite="lax",
        max_age=settings.REFRESH_TOKEN_EXPIRE_DAYS * 24 * 3600
    )


    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=False, 
        samesite="lax",
        max_age=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
    )

    return {
        "access_token": access_token,
    }



@router.get("/refresh")
async def refresh_access_token(
    payload = Depends(get_current_refresh_token_payload)
):
    new_access_token = create_token(
        payload,
        timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": new_access_token}


@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie("refresh_token")
