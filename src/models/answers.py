from typing import List

from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db import Base
from src.db.custom_types import intpk, updated_at, created_at


class Answers(Base):
    __tablename__ = "answers"

    id: Mapped[intpk]
    is_correct: Mapped[bool]
    text: Mapped[str] = mapped_column(Text)
    question_id: Mapped[int] = mapped_column(ForeignKey("questions.id", ondelete="CASCADE"))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    question: Mapped["Questions"] = relationship(
        back_populates="answers"
    )

    repr_cols_num = 3
