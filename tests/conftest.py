import datetime

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
