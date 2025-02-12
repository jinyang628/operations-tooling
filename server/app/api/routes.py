import logging

from fastapi import APIRouter

log = logging.getLogger(__name__)

router = APIRouter()

### Health check


@router.get("/status")
async def status():
    log.info("Status endpoint called")
    return {"status": "ok"}


### Rooms


# def get_rooms_controller_router():
#     service = RoomsService()
#     return RoomsController(service=service).router


# router.include_router(
#     get_rooms_controller_router(),
#     tags=["rooms"],
#     prefix="/api/rooms",
# )
