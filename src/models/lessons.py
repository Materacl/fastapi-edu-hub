from typing import List

from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db import Base
from src.db.custom_types import intpk, updated_at, created_at, str_128


class Lessons(Base):
    __tablename__ = "lessons"

    id: Mapped[intpk]
    number: Mapped[int]
    title: Mapped[str_128]
    content: Mapped[str] = mapped_column(Text)
    chapter_id: Mapped[int] = mapped_column(ForeignKey("chapters.id", ondelete="CASCADE"))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    chapter: Mapped["Chapters"] = relationship(
        back_populates="lessons"
    )

    quizzes: Mapped[List["Quizzes"]] = relationship(
        back_populates="lesson"
    )

    lessons_progresses: Mapped[List["LessonsProgresses"]] = relationship(
        back_populates="lesson"
    )

    repr_cols_num = 3
    repr_cols = ("chapter_id", )
