import pytest
import sys
from ev3dev2.button import Button
from ev3dev2.console import Console
from ev3dev2.motor import (
    MediumMotor,
)  # possible bug with missing setter for `duty_cycle`
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sound import Sound
from unittest import mock
from unittest.mock import Mock


#### from https://stackoverflow.com/a/68462121
def patch_all_symbol_imports(
    target_symbol, match_prefix=None, skip_substring=None, patchers=None
):
    """
    Iterate through every visible module (in sys.modules) that starts with
    `match_prefix` to find imports of `target_symbol` and return a list
    of patchers for each import.

    This is helpful when you want to patch a module, function, or object
    everywhere in your project's code, even when it is imported with an alias.

    Example:

    ::

        import datetime

        # Setup
        patchers = patch_all_symbol_imports(datetime, 'my_project.', 'test')
        for patcher in patchers:
            mock_dt = patcher.start()
            # Do stuff with the mock

        # Teardown
        for patcher in patchers:
            patcher.stop()

    :param target_symbol: the symbol to search for imports of (may be a module,
        a function, or some other object)
    :param match_prefix: if not None, only search for imports in
        modules that begin with this string
    :param skip_substring: if not None, skip any module that contains this
        substring (e.g. 'test' to skip unit test modules)
    :return: a list of patchers for each import of the target symbol
    """

    if patchers is None:
        patchers = []

    # Iterate through all currently imported modules
    # Make a copy in case it changes
    for module in list(sys.modules.values()):
        name_matches = match_prefix is None or module.__name__.startswith(match_prefix)
        should_skip = skip_substring is not None and skip_substring in module.__name__
        if not name_matches or should_skip:
            continue

        # Iterate through this module's locals
        # Again, make a copy
        for local_name, local in list(module.__dict__.items()):
            if local is target_symbol:
                # Patch this symbol local to the module
                patchers.append(
                    mock.patch(f"{module.__name__}.{local_name}", autospec=True)
                )

    return patchers


@pytest.fixture(autouse=True)
def mock_ev3dev_modules():
    all_patchers = []
    for module in [Button, Console, MediumMotor, TouchSensor, Sound]:
        patch_all_symbol_imports(module, skip_substring="test", patchers=all_patchers)

    # breakpoint()
    return all_patchers


@pytest.fixture
def mocker():
    return Mock()


# TODO: create a billion fixtures with autouse=True and which mock ev3dev2 modules
