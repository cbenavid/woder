from typing import Any

import pytest

from woder.domain.result import Ok


class TestOk:
    @pytest.mark.parametrize("value", [None, 1, "foo"])
    def test_has_value_attribute(self, value: Any) -> None:
        assert Ok(value).value == value

    def test_can_be_compared(self) -> None:
        assert Ok(None) == Ok(None)
        assert Ok(None) != Ok(1)
