import schemas

all_employees_schema_response = {
    200: {"model": schemas.EmployeesResponseSchema, "description": "success"}
}

create_employees_schema_response = {
    200: {"model": schemas.EmployeeResponseSchema, "description": "success"},
    400: {"model": schemas.ErrorResponseSchema, "description": "bad request"},
    409: {"model": schemas.ErrorResponseSchema, "description": "conflict"}
}

find_employees_schema_response = {
    200: {"model": schemas.EmployeeResponseSchema, "description": "success"},
    404: {"model": schemas.ErrorResponseSchema, "description": "not found"}
}

update_employees_schema_response = {
    200: {"model": schemas.EmployeeResponseSchema, "description": "success"},
    400: {"model": schemas.ErrorResponseSchema, "description": "bad request"},
    404: {"model": schemas.ErrorResponseSchema, "description": "not found"},
    409: {"model": schemas.ErrorResponseSchema, "description": "conflict"}
}

delete_employees_schema_response = {
    204: {"description": "not content"},
    404: {"model": schemas.ErrorResponseSchema, "description": "not found"}
}
