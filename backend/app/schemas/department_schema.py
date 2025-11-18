from pydantic import BaseModel, ConfigDict

class DepartmentBase(BaseModel):
    dept_name: str

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentUpdate(DepartmentBase):
    pass

class DepartmentOut(DepartmentBase):
    dept_id: int
    model_config = ConfigDict(from_attributes=True)