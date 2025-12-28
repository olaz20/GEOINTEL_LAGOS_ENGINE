from pydantic import BaseModel, EmailStr


class SignupRequest(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str


class SignupResponse(BaseModel):
    id: str
    email: EmailStr
    full_name: str
