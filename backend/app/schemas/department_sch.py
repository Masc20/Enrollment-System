from pydantic import BaseModel

class DepartmentBase(BaseModel):
    dept_name: str

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentOut(DepartmentBase):
    dept_id: int

    class Config:
        from_attributes = True