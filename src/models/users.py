import enum
from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db import Base
from src.db.custom_types import intpk, updated_at, created_at, str_64, str_128


class UserRole(enum.Enum):
    SUPER_ADMIN = "super_admin"
    ADMIN = "admin"
    MENTOR = "mentor"
    USER = "user"


class Users(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    is_active: Mapped[bool] = mapped_column(default=True)
    email: Mapped[str_128] = mapped_column(unique=True, index=True)
    role: Mapped[UserRole] = mapped_column(default=UserRole.USER)
    firstname: Mapped[str_64]
    lastname: Mapped[str_64]
    password_hash: Mapped[str_128]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    courses_in_progress: Mapped[List["Courses"]] = relationship(
        secondary="courses_progresses",
        primaryjoin="and_(Users.id == CoursesProgresses.user_id, "
                    "CoursesProgresses.status == ProgressStatus.IN_PROGRESS)",
        secondaryjoin="CoursesProgresses.course_id == Courses.id",
        order_by="CoursesProgresses.created_at.desc()",
        viewonly=True,
    )

    courses_completed: Mapped[List["Lessons"]] = relationship(
        secondary="courses_progresses",
        primaryjoin="and_(Users.id == CoursesProgresses.user_id, "
                    "CoursesProgresses.status == ProgressStatus.COMPLETED)",
        secondaryjoin="CoursesProgresses.course_id == Courses.id",
        order_by="CoursesProgresses.created_at.desc()",
        viewonly=True,
    )

    comments: Mapped[List["Comments"]] = relationship(
        back_populates="user",
        order_by="Comments.created_at.desc()"
    )

    repr_cols_num = 4
