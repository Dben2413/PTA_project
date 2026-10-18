from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base


class BizOrder(Base):
    __tablename__ = "biz_order"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_by: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("User.User_id")
    )
    status: Mapped[bool | None] = mapped_column(Boolean)
    order_id: Mapped[int | None] = mapped_column(Integer)
    content: Mapped[str | None] = mapped_column(String(255))

    creator: Mapped["User | None"] = relationship(
        back_populates="orders",
    )
    approvals: Mapped[list["BizApproval"]] = relationship(
        back_populates="order",
    )