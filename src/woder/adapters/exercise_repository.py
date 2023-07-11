from datetime import datetime, timezone

from woder.domain.entities.exercise import Exercise, ExerciseRecord
from woder.domain.ports.repositories.exercise import ExerciseRepository


class InMemoryFakeExerciseRepository(ExerciseRepository):
    async def get_one_by_name(self, name: str) -> Exercise:
        return Exercise(
            name="back_squat",
            history=[
                ExerciseRecord(
                    timestamp=datetime(1970, 1, 1, tzinfo=timezone.utc),
                    weight=80,
                    number_of_reps=10,
                )
            ],
        )
