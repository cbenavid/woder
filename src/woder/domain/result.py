from typing import Any, Generic, TypeVar

T = TypeVar("T")


class Ok(Generic[T]):
    def __init__(self, value: T, /) -> None:
        self._value = value

    @property
    def value(self) -> T:
        return self._value

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Ok) and other.value == self.value
