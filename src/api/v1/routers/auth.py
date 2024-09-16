from fastapi import APIRouter

router = APIRouter(
    prefix="/users/auth",
    tags=["Users", "Auth"],
)


@router.post("/register")
def register_user():
    raise NotImplemented


@router.post("/token")
def login_user():
    raise NotImplemented
