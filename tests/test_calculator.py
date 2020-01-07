import pytest

import calculator


@pytest.fixture
def numbers():
    return [1, 2, 3, 4, 5, 6, 7, 8]


def test_get_sum(numbers):
    assert calculator.get_sum(numbers) == 36


def test_get_product(numbers):
    assert calculator.get_product(numbers) == 40320
