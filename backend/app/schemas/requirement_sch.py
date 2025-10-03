from pydantic import BaseModel

class RequirementBase(BaseModel):
    req_name: str

class RequirementCreate(RequirementBase):
    pass

