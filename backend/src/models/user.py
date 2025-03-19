from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class User(Base):
    __tablename__ = "users"

    email: Mapped[String] = mapped_column(String, primary_key=True, index=True)
