from typing import Any

import pytest

from woder.domain.result import Err, Ok


class TestOk:
    @pytest.mark.parametrize("value", [None, 1, "foo"])
    def test_has_value_attribute(self, value: Any) -> None:
        assert Ok(value).value == value

    def test_can_be_compared(self) -> None:
        assert Ok(None) == Ok(None)
        assert Ok(None) != Ok(1)

    def test_is_truthy(self) -> None:
        assert bool(Ok(None))


class TestErr:
    @pytest.mark.parametrize("value", [None, 1, "foo"])
    def test_has_value_attribute(self, value: Any) -> None:
        assert Err(value).value == value

    def test_can_be_compared(self) -> None:
        assert Err(None) == Err(None)
        assert Err(None) != Err(1)

    def test_is_falsy(self) -> None:
        assert not bool(Err(None))
