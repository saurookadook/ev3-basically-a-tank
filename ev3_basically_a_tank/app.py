from time import sleep

from .utils import debug_logger


class App:
    def __init__(self, name="", brick_device=None, **kwargs):
        debug_logger(
            ("-" * 30) + "[ App.__init__ ]" + ("-" * 30),
            "---| name: {}".format(name),
            "---| brick_device: {}".format(brick_device),
            "---| kwargs: {}".format(kwargs),
        )

        self.name = name
        self.brick_device = brick_device

        self.is_silenced = (
            False if not hasattr(kwargs, "disable_sound") else kwargs["disable_sound"]
        )

        for key_arg in kwargs:
            if not hasattr(self, key_arg):
                setattr(self, key_arg, kwargs[key_arg])

        debug_logger(
            dir(self), ("-" * 30) + "[ end of App.__init__ ]" + ("-" * 30), end="\n\n"
        )

    def run(self):
        """Run dha app :)"""

        self.console.clear()
        self.console.text_at(
            "LOOK AT DHIS '{}' SHIT".format(self.name),
            alignment="C",
            reset_console=True,
        )

    def boot_up_greeting(self):
        self.say("Bootin up, baby")
        self.console.text_at("Bootin up . . .", alignment="C")
        sleep(1)
        self.console.text_at("BINGO BANGO!", alignment="C", reset_console=True)
        self.say("BINGO BANGO!")

    def shut_down(self):
        self.console.text_at("I am a pickle!", reset_console=True, alignment="C")
        self.say("I am a pickle!")

        self.console.text_at("Bye forever", alignment="C")
        self.say("Bye forever")

    def say(self, text, **kwargs):
        if self.is_silenced:
            debug_logger(text)
        else:
            self.sound.speak(text, **kwargs)

    def _configure_ports_with_mode(
        self,
        port_a=None,
        port_b=None,
        port_c=None,
        port_d=None,
        mode_for_a=None,
        mode_for_b=None,
        mode_for_c=None,
        mode_for_d=None,
    ):
        self.port_a = port_a
        if self.port_a and self.port_a.status:
            debug_logger("port_a mode: {}".format(self.port_a.mode))
            if not self.port_a.mode:
                self.port_a.mode = mode_for_a or "dc-motor"

        self.port_b = port_b
        if self.port_b and self.port_b.status:
            debug_logger("port_b mode: {}".format(self.port_b.mode))
            if not self.port_b.mode:
                self.port_b.mode = mode_for_b or "dc-motor"

        self.port_c = port_c
        if self.port_c and self.port_c.status:
            debug_logger("port_c mode: {}".format(self.port_c.mode))
            if not self.port_c.mode:
                self.port_c.mode = mode_for_c or "dc-motor"

        self.port_d = port_d
        if self.port_d and self.port_d.status:
            debug_logger("port_d mode: {}".format(self.port_d.mode))
            if not self.port_d.mode:
                self.port_d.mode = mode_for_d or "dc-motor"

        sleep(0.5)

    def _configure_inputs_with_mode(
        self,
        input_1=None,
        input_2=None,
        input_3=None,
        input_4=None,
        mode_for_1=None,
        mode_for_2=None,
        mode_for_3=None,
        mode_for_4=None,
    ):
        self.input_1 = input_1
        if self.input_1 and self.input_1.status:
            debug_logger("input_1 mode: {}".format(self.input_1.mode))
            if not self.input_1.mode:
                self.input_1.mode = mode_for_1 or "TOUCH"

        self.input_2 = input_2
        if self.input_2 and self.input_2.status:
            debug_logger("input_2 mode: {}".format(self.input_2.mode))
            if not self.input_2.mode:
                self.input_2.mode = mode_for_2 or "TOUCH"

        self.input_3 = input_3
        if self.input_3 and self.input_3.status:
            debug_logger("input_3 mode: {}".format(self.input_3.mode))
            if not self.input_3.mode:
                self.input_3.mode = mode_for_3 or "TOUCH"

        self.input_4 = input_4
        if self.input_4 and self.input_4.status:
            debug_logger("input_4 mode: {}".format(self.input_4.mode))
            if not self.input_4.mode:
                self.input_4.mode = mode_for_4 or "TOUCH"

        sleep(0.5)
