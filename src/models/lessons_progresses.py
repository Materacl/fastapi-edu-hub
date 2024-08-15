import enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db import Base
from src.db.custom_types import updated_at, created_at


class ProgressStatus(enum.Enum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class LessonsProgresses(Base):
    __tablename__ = 'lessons_progresses'

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete="CASCADE"), primary_key=True, index=True)
    lesson_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    status: Mapped[ProgressStatus] = mapped_column(default=ProgressStatus.NOT_STARTED)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    user: Mapped["User"] = relationship(back_populates="lessons_in_progress")
    lesson: Mapped["Lesson"] = relationship(foreign_keys=[lesson_id],
                                            primaryjoin="LessonsProgresses.lesson_id==Lesson.id")

    repr_cols_num = 3
