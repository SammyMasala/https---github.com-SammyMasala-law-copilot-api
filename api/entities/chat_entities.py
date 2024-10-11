from pydantic import BaseModel


class Message(BaseModel):
    is_user: bool
    message: str