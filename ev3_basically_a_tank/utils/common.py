import sys
from ev3dev2.port import LegoPort


def debug_logger(*args, **kwargs):
    try:
        print(*args, file=sys.stderr, **kwargs)
    except Exception:
        pass


def safe_init_port(port_letter, keyword_args):
    port_x = "port_{}".format(port_letter.lower())
    outX = "out{}".format(port_letter.upper())
    return keyword_args[port_x] or LegoPort(outX)
