import abc

from woder.domain.entities.exercise import Exercise


class ExerciseRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def get_one_by_name(self, name: str) -> Exercise:
        ...
