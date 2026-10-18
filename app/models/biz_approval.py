from sqlalchemy import Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base


class BizApproval(Base):
    __tablename__ = "biz_approval"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    order_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("biz_order.id")
    )
    status: Mapped[bool] = mapped_column(Boolean, nullable=False)
    approver_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("User.User_id")
    )

    order: Mapped["BizOrder | None"] = relationship(
        back_populates="approvals",
    )
    approver: Mapped["User | None"] = relationship(
        back_populates="approvals",
    )