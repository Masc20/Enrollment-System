from pydantic import BaseModel, ConfigDict

class RequirementBase(BaseModel):
    req_name: str

class RequirementCreate(RequirementBase):
    pass

class RequirementUpdate(RequirementBase):
    pass

class RequirementOut(RequirementBase):
    req_id: int
    model_config = ConfigDict(from_attributes=True)