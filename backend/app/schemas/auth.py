from pydantic import BaseModel

class LoginSchema(BaseModel):
    username: str
    password: str

class LoginRequest(LoginSchema):
    pass

class LoginResponse(BaseModel):
    username: str
    role: str
    message: str