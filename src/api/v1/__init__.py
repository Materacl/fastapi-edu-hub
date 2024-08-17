from fastapi import APIRouter

from . import routers

# Create an API Router with a prefix for versioning
router = APIRouter(
    prefix="/v1"
)

# Include various routers for different modules
for r in routers.list_of_routers:
    router.include_router(r)
