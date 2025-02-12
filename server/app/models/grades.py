from enum import Enum, StrEnum, auto

from pydantic import BaseModel


class GradeValue(StrEnum):
    A_PLUS = "A+"
    A = "A"
    A_MINUS = "A-"
    B_PLUS = "B+"
    B = "B"
    B_MINUS = "B-"
    C_PLUS = "C+"
    C = "C"
    C_MINUS = "C-"
    D_PLUS = "D+"
    D = "D"
    E = "E"
    F = "F"


class SemesterValue(Enum):
    ONE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()


class Grade(BaseModel):
    id: int
    student_id: int
    grade: GradeValue
    semester: SemesterValue
