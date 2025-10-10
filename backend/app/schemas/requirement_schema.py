from pydantic import BaseModel

class RequirementBase(BaseModel):
    req_name: str

class RequirementCreate(RequirementBase):
    pass

class RequirementUpdate(RequirementBase):
    pass

class RequirementOut(RequirementBase):
    req_id: int

    class Config:
        from_attributes = True