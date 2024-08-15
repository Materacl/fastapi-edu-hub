import enum
from typing import List

from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.db import Base
from src.db.custom_types import intpk, updated_at, created_at


class QuestionType(enum.Enum):
    ONE_CHOICE = "one_choice"
    MULTIPLE_CHOICE = "multiple_choice"
    TRUE_FALSE = "true_false"
    ORDERING = "ordering"


class Questions(Base):
    __tablename__ = "questions"

    id: Mapped[intpk]
    type: Mapped[QuestionType]
    content: Mapped[str] = mapped_column(Text)
    quizz_id: Mapped[int] = mapped_column(ForeignKey("quizzes.id", ondelete="CASCADE"))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    quizz: Mapped["Quizzes"] = relationship(
        back_populates="questions"
    )

    answers: Mapped[List["Answers"]] = relationship(
        back_populates="question"
    )

    right_answers: Mapped[List["Answers"]] = relationship(
        back_populates="question",
        primaryjoin="and_(Answers.question_id==Questions.id, Answers.is_correct==True)",
        order_by="Answers.id.desc()",
    )

    repr_cols_num = 2
    repr_cols = ("quizz_id", )
