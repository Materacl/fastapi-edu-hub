from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/{user_id}")
def get_user_by_id():
    raise NotImplemented


@router.get("/{user_email}")
def get_user_by_email():
    raise NotImplemented


@router.get("/{user_id}/courses-progress/{course_id}")
def get_user_course_progress_by_id():
    raise NotImplemented


@router.get("/{user_id}/courses-progress/{status}")
def get_user_courses_progress_by_status():
    raise NotImplemented


@router.get("/{user_id}/lessons-progress/{lesson_id}")
def get_user_lesson_progress_by_id():
    raise NotImplemented


@router.get("/{user_id}/lessons-progress/{status}")
def get_user_lessons_progress_by_status():
    raise NotImplemented
