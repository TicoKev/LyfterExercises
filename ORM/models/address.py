from models.base import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Address(Base):
  __tablename__ = 'addresses'
  id: Mapped[int] = mapped_column(primary_key=True)
  address: Mapped[str] = mapped_column(String(200), nullable=False)
  user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
  user: Mapped["User"] = relationship(back_populates='addresses')

