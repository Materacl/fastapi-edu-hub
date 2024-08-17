from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/me")
def get_current_user():
    raise NotImplemented


@router.get("/{user_id}")
def get_user_by_id():
    raise NotImplemented


@router.get("/{user_email}")
def get_user_by_email():
    raise NotImplemented
