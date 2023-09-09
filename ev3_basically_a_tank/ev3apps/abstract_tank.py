from ..app import App
from ..constants import DriveDirection, TurnDirection
from ..utils import debug_logger


class AbstractEV3Tank(App):
    __slots__ = [
        "_left_motor",
        "_right_motor",
        "_front_touch_sensor",
        "_back_touch_sensor",
        "_current_drive_direction",
        "_drive_direction",
        "_turn_direction",
        "_cruise_speed",
        "_reorient_speed",
        "_left_wheel_speed",
        "_right_wheel_speed",
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.current_drive_direction = DriveDirection.FORWARDS.value
        self.drive_direction = DriveDirection.FORWARDS.value
        self.turn_direction = TurnDirection.STRAIGHT.value
        self.cruise_speed = 80
        self.reorient_speed = 60

    @property
    def left_motor(self):
        return self._left_motor

    @left_motor.setter
    def left_motor(self, value):
        self._left_motor = value

    @property
    def right_motor(self):
        return self._right_motor

    @right_motor.setter
    def right_motor(self, value):
        self._right_motor = value

    @property
    def front_touch_sensor(self):
        return self._front_touch_sensor

    @front_touch_sensor.setter
    def front_touch_sensor(self, value):
        self._front_touch_sensor = value

    @property
    def back_touch_sensor(self):
        return self._back_touch_sensor

    @back_touch_sensor.setter
    def back_touch_sensor(self, value):
        self._back_touch_sensor = value

    @property
    def current_drive_direction(self):
        return self._current_drive_direction

    @current_drive_direction.setter
    def current_drive_direction(self, value):
        try:
            self._current_drive_direction = DriveDirection(value).value
        except ValueError as ve:
            debug_logger(ve)
            # raise ve

    @property
    def drive_direction(self):
        return self._drive_direction

    @drive_direction.setter
    def drive_direction(self, value):
        try:
            self._drive_direction = DriveDirection(value).value
        except ValueError as ve:
            debug_logger(ve)
            # raise ve

    @property
    def turn_direction(self):
        return self._turn_direction

    @turn_direction.setter
    def turn_direction(self, value):
        try:
            self._turn_direction = TurnDirection(value).value
        except ValueError as ve:
            debug_logger(ve)
            # raise ve

    @property
    def cruise_speed(self):
        return self._cruise_speed

    @cruise_speed.setter
    def cruise_speed(self, value):
        self._cruise_speed = value

    @property
    def reorient_speed(self):
        return self._reorient_speed

    @reorient_speed.setter
    def reorient_speed(self, value):
        self._reorient_speed = value

    @property
    def left_wheel_speed(self):
        return self._left_wheel_speed

    @left_wheel_speed.setter
    def left_wheel_speed(self, value):
        self._left_wheel_speed = value

    @property
    def right_wheel_speed(self):
        return self._right_wheel_speed

    @right_wheel_speed.setter
    def right_wheel_speed(self, value):
        self._right_wheel_speed = value

    def _configure_ports_with_mode(self, **kwargs):
        super()._configure_ports_with_mode(self, **kwargs)

    def _configure_inputs_with_mode(self, **kwargs):
        super()._configure_inputs_with_mode(self, **kwargs)
