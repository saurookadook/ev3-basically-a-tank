import pytest
from unittest.mock import Mock


@pytest.fixture
def mocker():
    return Mock()


# TODO: create a billion fixtures with autouse=True and which mock ev3dev2 modules
