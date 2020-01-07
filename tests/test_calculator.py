import calculator


def test_get_sum():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    assert calculator.get_sum(numbers) == 36


def test_get_product():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    assert calculator.get_product(numbers) == 40320
