from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db import Base
from src.db.custom_types import intpk, updated_at, created_at


class Comments(Base):
    __tablename__ = "comments"

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lessons.id", ondelete="CASCADE"))
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    user: Mapped["Users"] = relationship(
        back_populates="comments"
    )

    repr_cols_num = 3
