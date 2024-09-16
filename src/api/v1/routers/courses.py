from fastapi import APIRouter

from src.models.courses import CourseStatus

router = APIRouter(
    prefix="/courses",
    tags=["Courses"],
)


@router.get("/")
def get_courses(title: str = None,
                status: CourseStatus = None,
                desc: bool = True,
                skip: int = 0,
                limit: int = 10):
    raise NotImplemented


@router.get("/{course_id}")
def get_course_by_id(course_id: int):
    raise NotImplemented



