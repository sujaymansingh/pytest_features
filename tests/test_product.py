import pytest

import calculator


@pytest.mark.product
def test_get_product(numbers):
    assert calculator.get_product(numbers) == 40320
