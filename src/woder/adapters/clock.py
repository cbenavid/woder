import datetime

from woder.domain.ports.clock import Clock


class FakeClock(Clock):
    def __init__(self) -> None:
        self._value: datetime | None = None

    def __call__(self) -> datetime:
        if not self._value:
            raise ValueError("No value has been set")
        return self._value

    def with_time(self, time: datetime, /) -> "FakeClock":
        self._value = time
        return self
