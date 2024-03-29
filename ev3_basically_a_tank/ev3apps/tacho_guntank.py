from ev3dev2.button import Button
from ev3dev2.console import Console
from ev3dev2.motor import (
    MediumMotor,
)  # possible bug with missing setter for `duty_cycle`
from ev3dev2.sensor import INPUT_1, INPUT_2
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sound import Sound
from inspect import getmembers
from time import sleep, time

from .abstract_tank import AbstractEV3Tank
from ..constants import DriveDirection, TurnDirection
from ..utils import debug_logger, safe_init_port


class EV3TachoTank(AbstractEV3Tank):
    def __init__(self, *args, **kwargs):
        debug_logger(
            ("-" * 30) + "[ EV3TachoTank.__init__ ]" + ("-" * 30),
            "---| args: {}".format(args),
            "---| kwargs: {}".format(kwargs),
        )

        super().__init__(
            *args, buttons=Button(), console=Console(), sound=Sound(), **kwargs
        )

        super()._configure_ports_with_mode(
            port_a=safe_init_port("a", kwargs),
            port_b=safe_init_port("b", kwargs),
            mode_for_a="tacho-motor",
            mode_for_b="tacho-motor",
        )

        self.right_motor = MediumMotor(self.port_a.address)
        self.left_motor = MediumMotor(self.port_b.address)

        self.front_touch_sensor = TouchSensor(INPUT_1)
        self.rear_touch_sensor = TouchSensor(INPUT_2)

        debug_logger(
            dir(self),
            ("-" * 30) + "[ end of AbstractEV3Tank.__init__ ]" + ("-" * 30),
        )

    def run(
        self,
    ):
        self.boot_up_greeting()

        current_drive_direction = DriveDirection.FORWARDS.value
        start_time = int(time())

        while True:
            if self.turn_direction != TurnDirection.STRAIGHT.value:
                self.turn_in_drive_direction(
                    turn_direction=TurnDirection.STRAIGHT.value
                )
            self.drive(
                speed=self.cruise_speed,
                drive_direction=current_drive_direction,
                duration=-1,
            )

            if self.front_touch_sensor.is_pressed:
                self.stop()
                current_drive_direction = DriveDirection.REVERSE.value
                turn_direction = self._choose_turn_direction(
                    drive_direction=current_drive_direction,
                    last_turn_direction=self.turn_direction,
                )
                debug_logger(
                    "Front touch sensor pressed!\n",
                    "turn_direction: {}\ndrive_direction: {}\ncurrent_drive_direction: {}".format(
                        turn_direction, self.drive_direction, current_drive_direction
                    ),
                )
                self.say("Ouch, my face!")
                self.turn_in_drive_direction(
                    drive_direction=current_drive_direction,
                    turn_direction=turn_direction,
                )
                sleep(3)
                # self.drive(
                #     speed=self.reorient_speed,
                #     drive_direction=current_drive_direction,
                #     duration=2,
                # )
                self.say("boop bop beep")

            elif self.rear_touch_sensor.is_pressed:
                self.stop()
                current_drive_direction = DriveDirection.FORWARDS.value
                turn_direction = self._choose_turn_direction(
                    drive_direction=current_drive_direction,
                    last_turn_direction=self.turn_direction,
                )
                debug_logger(
                    "Back touch sensor pressed!\n",
                    "turn_direction: {}\ndrive_direction: {}\ncurrent_drive_direction: {}".format(
                        turn_direction, self.drive_direction, current_drive_direction
                    ),
                )
                self.say("Ouch, my butthole!")
                self.turn_in_drive_direction(
                    drive_direction=current_drive_direction,
                    turn_direction=turn_direction,
                )
                sleep(3)
                # self.drive(
                #     speed=self.reorient_speed,
                #     drive_direction=current_drive_direction,
                #     duration=2,
                # )
                self.say("beep bop boop")

            # sleep(0.01)

            if self.buttons.buttons_pressed or time() - start_time >= 20:
                debug_logger(int(time() - start_time))
                self.stop()
                break

        self.shut_down()

    def drive(
        self,
        speed=None,
        left_wheel_speed=None,
        right_wheel_speed=None,
        drive_direction="forwards",
        duration=-1,
    ):
        # debug_logger(
        #     ("-" * 30) + " top of `drive` " + ("-" * 30) + "\n",
        #     "speed: {}\n".format(speed),
        #     "left_wheel_speed: {}\n".format(left_wheel_speed),
        #     "right_wheel_speed: {}\n".format(right_wheel_speed),
        #     "drive_direction: {}\n".format(drive_direction),
        #     "self.turn_direction: {}\n".format(self.turn_direction),
        #     "self.drive_direction: {}\n".format(self.drive_direction),
        #     "self.current_drive_direction: {}\n".format(self.current_drive_direction),
        # )
        if drive_direction != self.current_drive_direction:
            self.current_drive_direction = drive_direction

        if speed and not left_wheel_speed:
            left_wheel_speed = speed if drive_direction == "forwards" else -speed
            # left_wheel_speed = speed if drive_direction == "forwards" else -speed
        if speed and not right_wheel_speed:
            right_wheel_speed = -speed if drive_direction == "forwards" else speed
            # right_wheel_speed = -speed if drive_direction == "forwards" else speed

        # debug_logger(
        #     ("-" * 30) + " wheel speeds before base_run_direct call " + ("-" * 30) + "\n",
        #     "left_wheel_speed: {}\n".format(left_wheel_speed),
        #     "right_wheel_speed: {}\n".format(right_wheel_speed),
        #     "drive_direction: {}\n".format(drive_direction),
        # )
        # self.left_motor.run_direct(duty_cycle_sp=left_wheel_speed)
        # self.right_motor.run_direct(duty_cycle_sp=right_wheel_speed)
        self._base_run_direct(
            left_wheel_speed=left_wheel_speed, right_wheel_speed=right_wheel_speed
        )

        if int(duration) > 0:
            sleep(duration)
            self.stop()

    # def forward(self, left_wheel_speed=0, right_wheel_speed=0):
    #     self.left_motor.run_direct(duty_cycle_sp=left_wheel_speed)
    #     self.right_motor.run_direct(duty_cycle_sp=-right_wheel_speed)

    # def reverse(self, left_wheel_speed=0, right_wheel_speed=0):
    #     self.left_motor.run_direct(duty_cycle_sp=-left_wheel_speed)
    #     self.right_motor.run_direct(duty_cycle_sp=right_wheel_speed)

    def _base_run_direct(self, left_wheel_speed=0, right_wheel_speed=0):
        self.left_motor.duty_cycle_sp = left_wheel_speed
        self.right_motor.duty_cycle_sp = right_wheel_speed
        sleep(0.1)
        self.left_motor.run_direct(duty_cycle_sp=left_wheel_speed)
        sleep(0.1)
        self.right_motor.run_direct(duty_cycle_sp=right_wheel_speed)

    def turn_in_drive_direction(self, drive_direction, turn_direction):
        if turn_direction == self.turn_direction:
            return

        # self.turn_direction = turn_direction
        outer_wheel_speed, inner_wheel_speed = self._get_base_wheel_speeds_for_turn(
            drive_direction=drive_direction, turn_direction=turn_direction
        )

        if drive_direction == DriveDirection.FORWARDS.value:
            debug_logger(
                ("-" * 30)
                + " turn_in_drive_direction call - FORWARDS "
                + ("-" * 30)
                + "\n",
                "self.cruise_speed: {}\n".format(self.cruise_speed),
                "left_wheel_speed: {}\n".format(outer_wheel_speed),
                "right_wheel_speed: {}\n".format(inner_wheel_speed),
                "drive_direction: {}\n".format(drive_direction),
            )
            self._base_run_direct(
                left_wheel_speed=outer_wheel_speed, right_wheel_speed=inner_wheel_speed
            )
        else:
            debug_logger(
                ("-" * 30)
                + " turn_in_drive_direction call - REVERSE "
                + ("-" * 30)
                + "\n",
                "self.cruise_speed: {}\n".format(self.cruise_speed),
                "left_wheel_speed: {}\n".format(-outer_wheel_speed),
                "right_wheel_speed: {}\n".format(-inner_wheel_speed),
                "drive_direction: {}\n".format(drive_direction),
            )
            self._base_run_direct(
                left_wheel_speed=-outer_wheel_speed,
                right_wheel_speed=-inner_wheel_speed,
            )

        # if turn_direction == "straight":
        #     debug_logger("Straightenin' out!")
        #     self.set_motor_speeds_for_turn(
        #         left_wheel_speed=left_wheel_speed, right_wheel_speed=right_wheel_speed
        #     )
        # elif turn_direction == "left":
        #     debug_logger("Turnin' left!")
        #     self.set_motor_speeds_for_turn(
        #         left_wheel_speed=left_wheel_speed, right_wheel_speed=right_wheel_speed
        #     )
        # elif turn_direction == "right":
        #     debug_logger("Turnin' right!")
        #     self.set_motor_speeds_for_turn(
        #         left_wheel_speed=left_wheel_speed, right_wheel_speed=right_wheel_speed
        #     )

    def set_motor_speeds_for_turn(self, *, left_wheel_speed=0, right_wheel_speed=0):
        self.left_motor.run_direct(left_wheel_speed)
        self.right_motor.run_direct(right_wheel_speed)

    def _choose_turn_direction(self, drive_direction, last_turn_direction):
        if drive_direction == "forward":
            return "right" if last_turn_direction == "left" else "left"
        else:
            return "left" if last_turn_direction == "right" else "right"

    def _get_base_wheel_speeds_for_turn(self, drive_direction, turn_direction):
        left_wheel_speed = 0
        right_wheel_speed = 0

        outer_wheel_speed = self.cruise_speed + 15
        inner_wheel_speed = self.cruise_speed - 15

        if drive_direction == DriveDirection.REVERSE.value:
            left_wheel_speed = (
                outer_wheel_speed
                if turn_direction == TurnDirection.LEFT.value
                else inner_wheel_speed
            )
            right_wheel_speed = (
                inner_wheel_speed
                if turn_direction == TurnDirection.RIGHT.value
                else outer_wheel_speed
            )
        else:
            left_wheel_speed = (
                inner_wheel_speed
                if turn_direction == TurnDirection.LEFT.value
                else outer_wheel_speed
            )
            right_wheel_speed = (
                outer_wheel_speed
                if turn_direction == TurnDirection.RIGHT.value
                else inner_wheel_speed
            )

        debug_logger(
            ("-" * 30) + " _get_base_wheel_speeds_for_turn call " + ("-" * 30) + "\n",
            "self.cruise_speed: {}\n".format(self.cruise_speed),
            "outer_wheel_speed: {}\n".format(outer_wheel_speed),
            "inner_wheel_speed: {}\n".format(inner_wheel_speed),
            "left_wheel_speed: {}\n".format(left_wheel_speed),
            "right_wheel_speed: {}\n".format(right_wheel_speed),
            "drive_direction: {}\n".format(drive_direction),
            "turn_direction: {}\n".format(turn_direction),
        )

        return (outer_wheel_speed, inner_wheel_speed)

    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()
