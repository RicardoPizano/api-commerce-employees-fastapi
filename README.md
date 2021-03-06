# API Commerce Employees FastAPI

## Install

### Python 3

Install python 3 (recommended python 3.7), view: [python.org](https://www.python.org)

#### Virtualenv (optional)

Install Virtualenv with the command:
> $ pip install virtualenv

Crate a new virtualenv with the command (is recommended create the virtualenv in the project dir):
> $ virtualenv venv

Activate the virtualenv with the command:

- in Windows
  > $ ./venv/Scripts/activate
- in Linux or Mac
  > $ source ./venv/bin/activate

#### Install requirements

Install the requirements from the file requirements.txt with the command:
> $ pip install -r requirements.txt

Needed requirements:

- asgiref==3.4.1
- atomicwrites==1.4.0
- attrs==21.2.0
- certifi==2021.5.30
- charset-normalizer==2.0.4
- click==8.0.1
- colorama==0.4.4
- coverage==5.5
- fastapi==0.68.0
- greenlet==1.1.0
- h11==0.12.0
- idna==3.2
- iniconfig==1.1.1
- packaging==21.0
- pluggy==0.13.1
- py==1.10.0
- pydantic==1.8.2
- pyparsing==2.4.7
- pytest==6.2.4
- requests==2.26.0
- SQLAlchemy==1.4.22
- starlette==0.14.2
- toml==0.10.2
- typing-extensions==3.10.0.0
- urllib3==1.26.6
- uvicorn==0.14.0

# Configuration

The configuration require a .env file in root dir with the following vars:

#### Database

`DATABASE_URL` : Database connection URLs

## Run

### Run command

> python main.py

## Run tests

> pytest tests.py

## API endpoints

This section describes the calls that accepts the API

#### Auth
All endpoints require authentication of type Bearer token this means that all request to following endpoint require the header: `Authorization: Bearer {commerce_api_token}` 

### `GET /employees`

Retrieve all employees

### `POST /employees`

Create an employee

### `GET /employees/{employee_id}`

Find an employee

### `PUT /employees/{employee_id}`

Update an employee

### `DELETE /employees/{employee_id}`

Delete an employee

#### To see the full API documentation check the url in the environment of local one time run the project ([swagger](http://localhost:8001/docs) or [redoc](http://localhost:8001/redoc))
