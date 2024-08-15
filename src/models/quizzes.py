from typing import List

from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db import Base
from src.db.custom_types import intpk, updated_at, created_at, str_128


class Quizzes(Base):
    __tablename__ = "quizzes"

    id: Mapped[intpk]
    title: Mapped[str_128]
    description: Mapped[str] = mapped_column(Text)
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lessons.id", ondelete="CASCADE"))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    lesson: Mapped["Chapters"] = relationship(
        back_populates="quizzes"
    )

    questions: Mapped[List["Questions"]] = relationship(
        back_populates="question"
    )

    repr_cols_num = 2
    repr_cols = ("lesson_id", )
