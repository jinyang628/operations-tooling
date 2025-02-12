from app.utils.boolean_clause import BooleanClause, Operator
from app.utils.database import DatabaseClient


class StudentsService:
    async def modify_teacher(self, student_id: int, teacher_id: int):
        client = await DatabaseClient.get_instance()
        await client.get(
            table_name="students",
            boolean_clause=BooleanClause(
                column_name="name", operator=Operator.NEQ, value="Jin Yang"
            ),
        )
