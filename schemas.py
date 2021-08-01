from datetime import datetime
from typing import List

from pydantic import BaseModel


class EmployeeSchema(BaseModel):
    name: str
    last_name: str
    pin: str


class EmployeeUpdateSchema(BaseModel):
    name: str
    last_name: str
    pin: str
    active: bool


class EmployeeObjectResponseSchema(BaseModel):
    id: str
    full_name: str
    pin: str
    created_at: datetime
    active: bool


class EmployeeResponseSchema(BaseModel):
    rc: int
    msg: str
    data: EmployeeObjectResponseSchema


class EmployeesResponseSchema(BaseModel):
    rc: int
    msg: str
    data: List[EmployeeObjectResponseSchema]


class ErrorResponseSchema(BaseModel):
    rc: int
    msg: str
