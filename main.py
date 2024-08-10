#!/usr/bin/env python3
from ev3dev2.port import LegoPort

from ev3_basically_a_tank.ev3apps import EV3TachoTank


def main():
    tank_app = EV3TachoTank(
        name="basically_a_tank",
        port_a=LegoPort("outA"),
        port_b=LegoPort("outB"),
        # port_d=LegoPort("outD"),
        disable_sound=False,
    )

    tank_app.run()
    # tank_app._ultrasonic_sensor_test()


if __name__ == "__main__":
    main()
