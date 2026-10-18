from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base
from app.models.association import user_role

class User(Base):
    __tablename__ = "User"

    User_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str | None] = mapped_column(String(20))
    password: Mapped[str | None] = mapped_column(String(128))

    roles: Mapped[list["Role"]] = relationship(
        secondary=user_role,
        back_populates="users",
    )
    orders: Mapped[list["BizOrder"]] = relationship(
        back_populates="creator",
    )
    approvals: Mapped[list["BizApproval"]] = relationship(
        back_populates="approver",
    )