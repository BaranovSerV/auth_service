from pydantic import BaseModel


class UserAuthShema(BaseModel):
    email: str
