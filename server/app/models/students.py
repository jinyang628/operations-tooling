from pydantic import BaseModel


class Student(BaseModel):
    id: int
    name: str
    teacher_id: int
