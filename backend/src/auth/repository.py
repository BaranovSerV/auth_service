from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import User
from src.logger import logger


class AuthRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session


    async def get_or_create(self, user_data: dict) -> User:
        query = select(User).where(
            (User.email == user_data["email"])
        )
        result = await self.db_session.execute(query)
        user = result.scalars().first()
        
        if not user:
            new_user = User(
                **user_data
            )
            logger.debug(f"Создание нового пользователя: {new_user.email}")
            
            self.db_session.add(new_user)
            
            await self.db_session.commit()
            await self.db_session.refresh(new_user)
            
            return new_user
        
        logger.debug(f"Пользователь существует: {user.email}")

        return user
