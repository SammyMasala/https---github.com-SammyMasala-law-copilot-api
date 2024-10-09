from typing import Any
from pydantic import BaseModel
from api.dtos import ApiResponse
from api.entities.session_entities import Session

# Get Session
class LoadSessionRequest(BaseModel):
    id: str

class LoadSessionResponse(ApiResponse):
    session: Any = None

# Save Session
class SaveSessionRequest(Session):
    pass

class SaveSessionResponse(ApiResponse):
    session: Any = None