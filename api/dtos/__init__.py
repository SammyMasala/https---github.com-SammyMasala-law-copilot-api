from pydantic import BaseModel

class ApiResponse(BaseModel):
    is_success: bool = True
    failed_message: str = None