import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
import fastapi.openapi.utils as docs

from routers import router
from middleware import AuthenticationMiddleware

import responses

app = FastAPI(
    title="API Commerce Employees FastAPI",
    description="Employee microservice",
    version="1.0.0",
    contact={
        "name": "Ricardo Pizano",
        "email": "rikymon2@hotmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

docs.validation_error_response_definition = {
    "title": "BadRequest",
    "type": "object",
    "properties": {
        "rc": {"type": "int", "example": -1004}, "msg": {"type": "int", "example": "Incomplete data"}
    }
}


authentication_middleware = AuthenticationMiddleware()
app.middleware("http")(authentication_middleware)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return responses.incomplete_data_error()


app.include_router(router)

if __name__ == '__main__':
    uvicorn.run("main:app", port=8001)
