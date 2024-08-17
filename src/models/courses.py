import enum
from typing import List

from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db import Base
from src.db.custom_types import intpk, updated_at, created_at, str_128


class CourseStatus(enum.Enum):
    IN_DEVELOPMENT = "in_development"
    AVAILABLE = "available"


class Courses(Base):
    __tablename__ = "courses"

    id: Mapped[intpk]
    title: Mapped[str_128] = mapped_column(unique=True, index=True)
    description: Mapped[str] = mapped_column(Text)
    status: Mapped[CourseStatus] = mapped_column(default=CourseStatus.IN_DEVELOPMENT)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    chapters: Mapped[List["Chapters"]] = relationship(
        back_populates="course"
    )

    repr_cols_num = 3
    repr_cols = ("status", )
