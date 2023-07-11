from dataclasses import dataclass
from datetime import datetime


@dataclass
class ExerciseRecord:
    timestamp: datetime
    weight: float
    number_of_reps: int


@dataclass
class Exercise:
    name: str
    history: list[ExerciseRecord]
