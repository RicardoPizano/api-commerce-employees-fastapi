from fastapi import APIRouter, Depends, Request, Response
from sqlalchemy.orm import Session

import controller
import models
import schemas
import schemas_responses
import responses
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
router = APIRouter()


def get_session():
    session: Session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@router.get("/employees", responses={**schemas_responses.all_employees_schema_response})
async def all_employees(request: Request, response: Response, offset: int = 0, limit: int = 50,
                        session: Session = Depends(get_session)):
    employees = controller.all_employees(session, request.state.commerce.id, offset, limit)
    if len(employees) == 0:
        return responses.success(response)
    return responses.success(response, [employee.serializer() for employee in employees])


@router.post("/employees", responses={**schemas_responses.create_employees_schema_response})
async def create_employee(request: Request, response: Response, employee: schemas.EmployeeSchema,
                          session: Session = Depends(get_session)):
    new_employee = controller.create_employee(session, employee, request.state.commerce.id)
    if not new_employee:
        return responses.duplicated_pin_error(response)
    return responses.created(response, new_employee.serializer())


@router.get("/employees/{id_employee}", responses={**schemas_responses.find_employees_schema_response})
async def find_employee(request: Request, response: Response, id_employee: str,
                        session: Session = Depends(get_session)):
    employee = controller.find_employee(session, request.state.commerce.id, id_employee)
    if employee is None:
        return responses.invalid_employee_error(response)
    return responses.success(response, employee.serializer())


@router.put("/employees/{id_employee}", responses={**schemas_responses.update_employees_schema_response})
async def update_employee(request: Request, response: Response, id_employee: str,
                          employee: schemas.EmployeeUpdateSchema,
                          session: Session = Depends(get_session)):
    db_employee = controller.find_employee(session, request.state.commerce.id, id_employee)
    if db_employee is None:
        return responses.invalid_employee_error(response)
    updated_employee = controller.update_employee(session, db_employee, employee)
    if not updated_employee:
        return responses.duplicated_pin_error(response)
    return responses.success(response, updated_employee.serializer())


@router.delete("/employees/{id_employee}", responses={**schemas_responses.delete_employees_schema_response})
async def delete_employee(request: Request, response: Response, id_employee: str,
                          session: Session = Depends(get_session)):
    db_employee = controller.find_employee(session, request.state.commerce.id, id_employee)
    if db_employee is None:
        return responses.invalid_employee_error(response)
    controller.delete_employee(session, db_employee)
    return responses.not_content(response)
