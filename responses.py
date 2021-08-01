from typing import Dict

from fastapi import Response, status
from fastapi.responses import JSONResponse


def success(response: Response, data: any = None) -> Dict:
    response.status_code = status.HTTP_200_OK
    success_respond = {
        "rc": 0,
        "msg": "Ok"
    }
    if data is None:
        return success_respond
    if "rc" in data:
        return data
    success_respond["data"] = data
    return success_respond


def created(response: Response, data: any = None) -> Dict:
    response.status_code = status.HTTP_201_CREATED
    success_respond = {
        "rc": 0,
        "msg": "Ok"
    }
    if data is None:
        return success_respond
    if "rc" in data:
        return data
    success_respond["data"] = data
    return success_respond


def not_content(response: Response):
    response.status_code = status.HTTP_204_NO_CONTENT
    return {
        "rc": 0,
        "msg": "Ok"
    }


def invalid_employee_error(response: Response):
    response.status_code = status.HTTP_404_NOT_FOUND
    return {
        "rc": -1002,
        "msg": "Invalid id"
    }


def duplicated_pin_error(response: Response):
    response.status_code = status.HTTP_409_CONFLICT
    return {
        "rc": -1003,
        "msg": "Duplicated PIN"
    }


def authentication_failed():
    return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={
        "rc": -401,
        "msg": "Incorrect authentication credentials."
    })


def not_authenticated():
    return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={
        "rc": -401,
        "msg": "Authentication credentials were not provided."
    })


def permission_denied():
    return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content={
        "rc": -403,
        "msg": "You do not have permission to perform this action."
    })


def incomplete_data_error():
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={
        "rc": -1004,
        "msg": "Incomplete data"
    })


def no_empleado_error():
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={
        "rc": -1001,
        "msg": "Incomplete data"
    })
