from typing import List

from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db import Base
from src.db.custom_types import intpk, updated_at, created_at


class UsersAnswers(Base):
    __tablename__ = "users_answers"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE", primary_key=True, index=True))
    answer_id: Mapped[int] = mapped_column(ForeignKey("answers.id", ondelete="CASCADE", primary_key=True, index=True))
    is_correct: Mapped[bool]
    text: Mapped[str] = mapped_column(Text)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    question: Mapped["Questions"] = relationship(
        back_populates="answers"
    )

    user: Mapped["Users"] = relationship(
        back_populates="user_answers"
    )

    repr_cols_num = 3
