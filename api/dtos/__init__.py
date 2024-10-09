from pydantic import BaseModel


class ApiResponse(BaseModel):
    is_success: bool
    failed_message: str = None