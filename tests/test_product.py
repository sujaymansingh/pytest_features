import pytest

import calculator


@pytest.mark.product
def test_get_product(numbers):
    assert calculator.get_product(numbers) == 40320


@pytest.mark.product
def test_1_times_2():
    assert calculator.get_product([1, 2]) == 2


@pytest.mark.product
def test_3_times_4():
    assert calculator.get_product([3, 4]) == 12
