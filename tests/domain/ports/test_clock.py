from datetime import datetime, timezone

import pytest

from woder.adapters.clock import FakeClock


class TestFakeClock:
    def test_given_no_set_value_when_call_then_fails(self) -> None:
        clock = FakeClock()
        with pytest.raises(ValueError, match="No value has been set"):
            clock()

    def test_given_any_set_value_when_call_then_returns_same_value(self) -> None:
        clock = FakeClock().with_time(datetime(1970, 1, 1, tzinfo=timezone.utc))
        assert clock() == datetime(1970, 1, 1, tzinfo=timezone.utc)
