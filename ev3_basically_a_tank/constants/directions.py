from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def allowed_values(cls):
        return [v.value for v in cls.__members__.values()]


class DriveDirection(BaseEnum):
    FORWARDS = "forwards"
    REVERSE = "reverse"


class TurnDirection(BaseEnum):
    LEFT = "left"
    RIGHT = "right"
    STRAIGHT = "straight"
