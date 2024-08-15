from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db import Base
from src.db.custom_types import intpk, updated_at, created_at, str_128


class Chapters(Base):
    __tablename__ = "chapters"

    id: Mapped[intpk]
    number: Mapped[int]
    title: Mapped[str_128]
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id", ondelete="CASCADE"))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    course: Mapped["Courses"] = relationship(
        back_populates="chapters"
    )

    lessons: Mapped[List["Lessons"]] = relationship(
        back_populates="chapter"
    )

    repr_cols_num = 4
