from ..app import App
from ..constants import DriveDirection, TurnDirection
from ..utils import debug_logger


class AbstractEV3Tank(App):
    def __init__(self, *args, **kwargs):
        debug_logger(
            ("-" * 30) + "[ AbstractEV3Tank.__init__ ]" + ("-" * 30),
            "---| args: {}".format(args),
            "---| kwargs: {}".format(kwargs),
        )

        super().__init__(*args, **kwargs)

        self.current_drive_direction = DriveDirection.FORWARDS.value
        self.drive_direction = DriveDirection.FORWARDS.value
        self.turn_direction = TurnDirection.STRAIGHT.value
        self.cruise_speed = 80
        self.reorient_speed = 60

        for key_arg in kwargs:
            if not hasattr(self, key_arg):
                setattr(self, key_arg, kwargs[key_arg])

        debug_logger(
            dir(self),
            ("-" * 30) + "[ end of AbstractEV3Tank.__init__ ]" + ("-" * 30),
            end="\n\n",
        )

    def _configure_ports_with_mode(self, **kwargs):
        super()._configure_ports_with_mode(self, **kwargs)

    def _configure_inputs_with_mode(self, **kwargs):
        super()._configure_inputs_with_mode(self, **kwargs)
