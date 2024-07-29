import enum

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db import Base
from src.db.custom_types import intpk, updated_at, created_at, str_64, str_128


class UserRole(enum.Enum):
    SUPER_ADMIN = "super_admin"
    ADMIN = "admin"
    USER = "user"


class Users(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    firstname: Mapped[str_64]
    lastname: Mapped[str_64]
    email: Mapped[str_128] = mapped_column(unique=True, index=True)
    password_hash: Mapped[str_128]
    role: Mapped[UserRole] = mapped_column(default=UserRole.USER)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    # courses: Mapped[List["Courses"]] = relationship("Course", back_populates="teacher")
    # enrollments: Mapped[List["Enrollments"]] = relationship("Enrollment", back_populates="student")
    # comments: Mapped[List["Comments"]] = relationship("Comment", back_populates="user")

    repr_cols_num = 4
    repr_cols = tuple("role", )
