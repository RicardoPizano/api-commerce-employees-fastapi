import uuid
from typing import List

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

import models
import schemas
from models import Employee, Commerce


def commerce_authentication(session: Session, commerce_api_key: str) -> Commerce:
    return session.query(Commerce).filter(Commerce.api_key == commerce_api_key).filter(Commerce.active).first()


def all_employees(session: Session, commerce_id: int, offset: int = 0, limit: int = 50) -> List[Employee]:
    return session.query(Employee).filter(Employee.commerce_id == commerce_id).offset(offset).limit(limit).all()


def find_employee(session: Session, commerce_id: int, employee_uuid: str) -> Employee:
    employee_uuid = uuid.UUID(employee_uuid)
    return session.query(Employee).filter(Employee.uuid == employee_uuid).filter(
        Employee.commerce_id == commerce_id).first()


def create_employee(session: Session, employee: schemas.EmployeeSchema, commerce_id: int) -> [Employee, None]:
    try:
        db_employee = models.Employee()
        db_employee.name = employee.name
        db_employee.last_name = employee.last_name
        db_employee.pin = employee.pin
        db_employee.commerce_id = commerce_id
        session.add(db_employee)
        session.commit()
        session.refresh(db_employee)
        return db_employee
    except IntegrityError:
        return None


def update_employee(session: Session, db_employee: Employee, employee: schemas.EmployeeUpdateSchema) -> [Employee,
                                                                                                         None]:
    try:
        session.query(Employee).filter(Employee.id == db_employee.id).update(
            {Employee.name: employee.name,
             Employee.last_name: employee.last_name,
             Employee.pin: employee.pin,
             Employee.active: employee.active != 0},
            synchronize_session=False)
        session.commit()
        # session.refresh(updated_employee)
        return session.query(Employee).filter(Employee.id == db_employee.id).first()
    except IntegrityError:
        return None


def delete_employee(session: Session, db_employee: Employee):
    session.delete(db_employee)
    session.commit()
