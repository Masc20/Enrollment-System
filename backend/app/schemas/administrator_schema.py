from pydantic import BaseModel, ConfigDict

from typing import Optional


class AdministratorBase(BaseModel):
    username: str
    password: str
    role: str

class AdministratorCreate(AdministratorBase):
    pass

class AdministratorUpdate(BaseModel):
    username: Optional[str]
    password: Optional[str]
    role: Optional[str]

class AdministratorOut(BaseModel):
    admin_id: int
    username: str
    model_config = ConfigDict(from_attributes=True)