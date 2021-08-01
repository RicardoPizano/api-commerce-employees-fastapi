import uuid
from typing import TypedDict

from datetime import datetime
from sqlalchemy import Column, String, Boolean, Integer, DateTime, BigInteger, ForeignKey, CHAR, UniqueConstraint, types
from sqlalchemy.orm import relationship

from database import Base


class Uuid(types.TypeDecorator):
    impl = CHAR
    cache_ok = True

    def __init__(self):
        self.impl.length = 32
        types.TypeDecorator.__init__(self, length=self.impl.length)

    def process_bind_param(self, value, dialect=None):
        if value and isinstance(value, uuid.UUID):
            return value.hex
        else:
            return None

    def process_result_value(self, value, dialect=None):
        if value:
            return uuid.UUID(value)
        else:
            return None

    def is_mutable(self):
        return False


class Commerce(Base):
    __tablename__ = "main_comercio"

    id = Column("id", Integer, primary_key=True, index=True, nullable=False)
    uuid = Column("uuid", Uuid(), default=uuid.uuid4, nullable=False)
    name = Column("nombre", String(100), nullable=False)
    active = Column("activo", Boolean, nullable=False)
    email = Column("email_contacto", String(50), nullable=True)
    phone = Column("telefono_contacto", String(15), nullable=True)
    api_key = Column("api_key", CHAR(32), nullable=False)
    created_at = Column("fecha_creacion", DateTime, default=datetime.utcnow(), nullable=False)


class Employee(Base):
    __tablename__ = "main_empleado"

    id = Column("id", Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    uuid = Column("uuid", Uuid(), default=uuid.uuid4, nullable=False)
    name = Column("nombre", String(40), nullable=False)
    last_name = Column("apellidos", String(40), nullable=False)
    pin = Column("pin", String(6), nullable=False)
    created_at = Column("fecha_creacion", DateTime, default=datetime.utcnow(), nullable=False)
    active = Column("activo", Boolean, default=True, nullable=False)
    commerce_id = Column("comercio_id", BigInteger, ForeignKey("main_comercio.id"))
    commerce = relationship("Commerce")

    UniqueConstraint("pin", "commerce_id", name="main_empleado_pin_comercio_id_ca3250c0_uniq")

    def full_name(self):
        return "{} {}".format(self.name, self.last_name)

    def serializer(self):
        return {"id": self.uuid, "full_name": self.full_name(), "pin": self.pin, "created_at": self.created_at,
                "active": self.active}
