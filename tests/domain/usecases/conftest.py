from collections.abc import Iterator

import pytest

from woder.adapters.exercise_repository import InMemoryFakeExerciseRepository
from woder.domain.ports.repositories.exercise import ExerciseRepository


@pytest.fixture
def exercise_repository() -> Iterator[ExerciseRepository]:
    yield InMemoryFakeExerciseRepository()
