import enum
from sqlalchemy import Column, String
from sqlalchemy import Column, String, Integer, Enum, ForeignKey
from src.infra.config import Base


class TruckModels(enum.Enum):
    """Truck models"""

    hr = "HR"
    carreta = "Carreta"
    cegonha = "Cegonha"


class Trucks(Base):
    """Trucks Entity"""

    __tablename__ = "trucks"

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False, unique=True)
    model = Column(Enum(TruckModels), nullable=False)
    size = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"Truck: [name={self.name}, model={self.model}]"
