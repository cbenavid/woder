from typing import Any, Generic, Literal, TypeVar

T = TypeVar("T")
E = TypeVar("E")


class Ok(Generic[T]):
    def __init__(self, value: T, /) -> None:
        self._value = value

    @property
    def value(self) -> T:
        return self._value

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Ok) and other.value == self.value

    def __bool__(self) -> Literal[True]:
        return True


class Err(Generic[E]):
    def __init__(self, value: E, /) -> None:
        self._value = value

    @property
    def value(self) -> E:
        return self._value

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Err) and other.value == self.value

    def __bool__(self) -> Literal[False]:
        return False
