import random
import string

from fastapi.testclient import TestClient
from fastapi import status

from main import app

client = TestClient(app)

bad_auth_headers = {"authorization": "Bearer 5a25c9f25c334f4197df4d2aafca5f"}
auth_headers = {"authorization": "Bearer 5a25c9f25c334f4197df4d2aafca5fd9"}
employee_uuid = "0f348928-3463-4e2d-b677-b9acc8f89438"
employee_uuid_not_exist = "e46ac4d7-b823-4f6e-8860-e67fc76e2cb0"


def test_auth_bad_api_token():
    response = client.get("/employees", headers=bad_auth_headers)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_auth_not_api_token():
    response = client.get("/employees")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_all_employees_success():
    response = client.get("/employees", headers=auth_headers)
    assert response.status_code == status.HTTP_200_OK


def test_create_employee_success_and_same_pin():
    pin = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    response = client.post("/employees", headers=auth_headers, json={
        "name": "Juan",
        "last_name": "Perez",
        "pin": pin
    })
    assert response.status_code == status.HTTP_201_CREATED
    response = client.post("/employees", headers=auth_headers, json={
        "name": "Juan",
        "last_name": "Perez",
        "pin": pin
    })
    assert response.status_code == status.HTTP_409_CONFLICT


def test_create_employee_bad_request():
    response = client.post("/employees", headers=auth_headers, json={
        "name": "Juan",
        "pin": "123"
    })
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_find_employee_success():
    response = client.get("/employees/{}".format(employee_uuid), headers=auth_headers)
    assert response.status_code == status.HTTP_200_OK


def test_find_employee_not_found():
    response = client.get("/employees/{}".format(employee_uuid_not_exist), headers=auth_headers)
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_update_employee_success():
    response = client.put("/employees/{}".format(employee_uuid), headers=auth_headers, json={
        "name": "Steve",
        "last_name": "Rogers",
        "pin": "000000",
        "active": True
    })
    assert response.status_code == status.HTTP_200_OK


def test_delete_employee_success():
    pin = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    response = client.post("/employees", headers=auth_headers, json={
        "name": "deleted",
        "last_name": "employee",
        "pin": pin
    })
    assert response.status_code == status.HTTP_201_CREATED
    response = client.delete("/employees/{}".format(response.json()["data"]["id"]), headers=auth_headers)
    assert response.status_code == status.HTTP_204_NO_CONTENT
