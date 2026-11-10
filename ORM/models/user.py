from models.base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

class User(Base):
  __tablename__ = 'users'
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(String(50), nullable=False)
  email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
  addresses: Mapped[List['Address']] = relationship(back_populates='user')
  cars: Mapped[List['Car']] = relationship(back_populates='user')