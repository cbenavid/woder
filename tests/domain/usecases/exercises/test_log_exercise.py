import pytest

from woder.domain.result import Ok
from woder.domain.usecases.log_exercise import LogExerciseRequest, LogExerciseUsecase


@pytest.mark.asyncio
class TestLogExerciseUsecase:
    def setup(self) -> None:
        self.usecase = LogExerciseUsecase()

    async def test_given_unexisting_exercise_when_log_then_exercise_is_created_with_new_history(
        self,
    ) -> None:
        # Arrange
        request = LogExerciseRequest()

        # Act
        response = await self.usecase.handle(request)

        # Assert
        assert response == Ok(None)
