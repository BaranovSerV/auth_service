from fastapi import APIRouter, Depends

from src.auth.dependency import get_current_auth_user

router = APIRouter(prefix="/api/user", tags=["user"])


@router.get("/")
async def user(user = Depends(get_current_auth_user)):
    return user
