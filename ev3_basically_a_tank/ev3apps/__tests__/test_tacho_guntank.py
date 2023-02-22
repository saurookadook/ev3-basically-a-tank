import pytest
from ev3dev2.port import LegoPort

from ..tacho_guntank import EV3TachoTank


@pytest.fixture
def mock_tacho_guntank():
    return EV3TachoTank(
        name="basically_a_test",
        port_a=LegoPort("outA_TEST"),
        port_b=LegoPort("outB_TEST"),
    )


def test_tacho_guntank_name(mock_tacho_guntank):
    assert mock_tacho_guntank.name == "basically_a_test"
