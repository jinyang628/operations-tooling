from app.models.students import Student
from app.utils.boolean_clause import BooleanClause, Operator
from app.utils.database import DatabaseClient


class StudentsService:
    async def modify_teacher(self, student_id: int, teacher_id: int) -> Student:
        client = await DatabaseClient.get_instance()
        results: list = await client.patch(
            table_name="students",
            data={"teacher_id": teacher_id},
            boolean_clause=BooleanClause(column_name="id", operator=Operator.EQ, value=student_id),
        )
        students: list[Student] = [Student.model_validate(result) for result in results]
        if len(students) != 1:
            raise ValueError(
                "More than one student found while trying to modify teacher assignment"
            )
        return students[0]
