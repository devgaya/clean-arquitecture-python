from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import true
from src.infra.config import Base


class Users(Base):
    """ Users Entity """

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False, unique=False)
    id_truck = relationship("Trucks")

    def __repr__(self):
        return f"User: [name={self.name}]"

    def __eq__(self, other: object) -> bool:
        if (self.id == other.id and self.name == other.name and self.password == other.password):
            return True
        return False