from dataclasses import dataclass

from woder.domain.result import Ok


@dataclass
class LogExerciseRequest:
    name: str
    weight: float
    number_of_reps: int


class LogExerciseUsecase:
    async def handle(self, request: LogExerciseRequest) -> Ok[None]:
        return Ok(None)
