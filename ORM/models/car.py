from models.base import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Car(Base):
  __tablename__ = 'cars'
  id: Mapped[int] = mapped_column(primary_key=True)
  make: Mapped[str] = mapped_column(String(100), nullable=False)
  model: Mapped[str] = mapped_column(String(100), nullable=False)
  user_id: Mapped[int | None] = mapped_column(ForeignKey('users.id'), nullable=True)
  user: Mapped['User | None'] = relationship(back_populates='cars')