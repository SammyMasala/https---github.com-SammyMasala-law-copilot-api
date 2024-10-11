

from pydantic import BaseModel


class Session(BaseModel):
   id: str
   session: str = None