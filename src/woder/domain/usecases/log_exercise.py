from dataclasses import dataclass

from woder.domain.result import Ok


@dataclass
class LogExerciseRequest:
    ...


class LogExerciseUsecase:
    async def handle(self, request: LogExerciseRequest) -> Ok[None]:
        return Ok(None)
