import sys
from datetime import datetime as date_time
from ev3dev2.port import LegoPort


def create_log_file_config():
    today = date_time.now()
    log_filename = (
        "run_{t.month:0<2}-{t.day:0<2}-{t.year}_{t.hour:0<2}:{t.minute:0<2}".format(
            t=today
        )
    )
    log_mode = "w+"
    log_encoding = "utf-8"
    return log_filename, log_mode, log_encoding, today


log_file_config = create_log_file_config()


def create_log_file_for_run():
    log_filename, log_mode, log_encoding, today = log_file_config
    log_file_for_run = open(log_filename, log_mode, encoding=log_encoding)

    log_file_for_run.write("")
    log_file_for_run.close()
    return log_file_for_run


log_file_for_run = create_log_file_for_run()


def debug_logger(*args, **kwargs):
    try:
        print(*args, file=sys.stderr, **kwargs)
    except Exception:
        pass
    if getattr(kwargs, "print_to_log", None):
        with open(
            log_file_config.log_filename, "a+", encoding=log_file_config.log_mode
        ) as log_file:
            log_file.write(*args, **kwargs)


def safe_init_port(port_letter, keyword_args):
    port_x = "port_{}".format(port_letter.lower())
    outX = "out{}".format(port_letter.upper())
    return keyword_args[port_x] or LegoPort(outX)
