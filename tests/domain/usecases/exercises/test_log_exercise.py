from datetime import datetime, timezone

import pytest

from woder.adapters.clock import FakeClock
from woder.domain.entities.exercise import ExerciseRecord
from woder.domain.ports.repositories.exercise import ExerciseRepository
from woder.domain.result import Ok
from woder.domain.usecases.log_exercise import LogExerciseRequest, LogExerciseUsecase


@pytest.mark.asyncio
class TestLogExerciseUsecase:
    @pytest.fixture(autouse=True)
    def setup(self, exercise_repository: ExerciseRepository) -> None:
        self.exercise_repository = exercise_repository
        self.clock = FakeClock().with_time(datetime(1970, 1, 1, tzinfo=timezone.utc))
        self.usecase = LogExerciseUsecase()

    async def test_given_unexisting_exercise_when_log_then_exercise_is_created_with_new_history(
        self,
    ) -> None:
        # Arrange
        request = LogExerciseRequest(name="back_squat", weight=80, number_of_reps=10)

        # Act
        response = await self.usecase.handle(request)

        # Assert
        assert response == Ok(None)
        exercise = await self.exercise_repository.get_one_by_name("back_squat")
        assert exercise.name == "back_squat"
        assert exercise.history == [
            ExerciseRecord(
                timestamp=datetime(1970, 1, 1, tzinfo=timezone.utc),
                weight=80,
                number_of_reps=10,
            )
        ]
