import datetime
import json

from pathlib import Path

import pytest


@pytest.fixture
def numbers():
    return [1, 2, 3, 4, 5, 6, 7, 8]


@pytest.fixture(autouse=True)
def record_times():
    # Do stuff that needs to be setup at the beginning of each test...
    with open("logfile.log", "a") as out:
        out.write(f"Started at {datetime.datetime.utcnow()}\n")

    # Run the actual tests...
    yield

    # Do anything that needs to be done at the end of each test...
    with open("logfile.log", "a") as out:
        out.write(f"Started at {datetime.datetime.utcnow()}\n")


def pytest_generate_tests(metafunc):
    if metafunc.definition.name != "test_products":
        return

    products_filename = Path(__file__).parent / "products.json"
    with open(products_filename, "r") as products_file:
        raw_data = json.load(products_file)
        arguments = []
        for item in raw_data:
            nums = item["nums"]
            expected_product = item["expected_product"]
            arguments.append((nums, expected_product))
        metafunc.parametrize("nums, expected_product", arguments)
