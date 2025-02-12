import logging

from fastapi import APIRouter, HTTPException
from httpx import codes

from app.models.students import Student
from app.services.students import StudentsService

log = logging.getLogger(__name__)


class StudentsController:
    def __init__(self, service: StudentsService):
        self.router = APIRouter()
        self.service = service
        self.setup_routes()

    def setup_routes(self):
        router = self.router

        @router.patch(
            "/{student_id}/teacher/{teacher_id}",
            response_model=Student,
        )
        async def modify_teacher(student_id: int, teacher_id: int) -> Student:
            try:
                log.info("Modifying teacher for student %s...", student_id)
                response: Student = await self.service.modify_teacher(
                    student_id=student_id, teacher_id=teacher_id
                )
                log.info("Updated student record %s", response.model_dump())
                return response
            except Exception as e:
                log.error("Unexpected error in students controller.py: %s", str(e))
                raise HTTPException(
                    status_code=codes.INTERNAL_SERVER_ERROR, detail="An unexpected error occurred"
                ) from e
