import pytest

import calculator


@pytest.mark.sum
def test_get_sum(numbers):
    assert calculator.get_sum(numbers) == 36
