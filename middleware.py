import re

from fastapi import status
from sqlalchemy.orm import Session

import models
import controller
import responses
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


def get_session():
    session: Session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


class AuthenticationMiddleware:
    async def __call__(self, request, call_next):
        if "employees" in request.scope.get("path"):
            auth: str = request.headers.get('authorization')
            if not auth:
                return responses.not_authenticated()
            try:
                if not re.search("^Bearer .+$", auth):
                    return responses.authentication_failed()
                commerce_api_key: str = auth.split(" ")[1]
                session: Session = SessionLocal()
                try:
                    commerce = controller.commerce_authentication(session, commerce_api_key)
                finally:
                    session.close()
                if commerce is None:
                    return responses.authentication_failed()
                request.state.commerce = commerce
                response = await call_next(request)
                return response
            except TypeError:
                return responses.authentication_failed()
        response = await call_next(request)
        return response
