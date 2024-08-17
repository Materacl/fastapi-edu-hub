import enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db import Base
from src.db.custom_types import updated_at, created_at


class ProgressStatus(enum.Enum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class ChaptersProgresses(Base):
    __tablename__ = 'chapters_progresses'

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete="CASCADE"), primary_key=True, index=True)
    chapter_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    status: Mapped[ProgressStatus] = mapped_column(default=ProgressStatus.NOT_STARTED)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    user: Mapped["Users"] = relationship(back_populates="lessons_in_progress")
    chapter: Mapped["Chapters"] = relationship(foreign_keys=[chapter_id],
                                               primaryjoin="ChaptersProgresses.course_id==Chapters.id")

    repr_cols_num = 3
