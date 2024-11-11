from pydantic import BaseModel


class AuthResponse(BaseModel):
    token: str
    user: str
