import pytest
import sys
from ev3dev2.port import LegoPort
from unittest.mock import MagicMock

from ..tacho_guntank import EV3TachoTank


@pytest.fixture
def mock_lego_ports():
    return MagicMock(spec=LegoPort), MagicMock(spec=LegoPort)


@pytest.fixture
def mock_tacho_guntank(mock_lego_ports):
    mock_port_a, mock_port_b = mock_lego_ports

    return EV3TachoTank(
        name="basically_a_test",
        port_a=mock_port_a("outA_TEST"),
        port_b=mock_port_b("outB_TEST"),
    )


def test_tacho_guntank_name(mock_tacho_guntank):
    assert mock_tacho_guntank.name == "basically_a_test"
