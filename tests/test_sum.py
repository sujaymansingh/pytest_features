import pytest

import calculator


@pytest.fixture
def numbers():
    return [1, 2, 3, 4, 5, 6, 7, 8]


@pytest.mark.sum
def test_get_sum(numbers):
    assert calculator.get_sum(numbers) == 36
