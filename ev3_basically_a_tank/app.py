from .utils import debug_logger


class App:
    __slots__ = [
        "_brick_device",
        "_console",
        "_port_a",
        "_port_b",
        "_console",
        "_buttons",
        "_sound",
    ]

    def __init__(self, name="", brick_device=None, **kwargs):
        self.name = name

        self._brick_device = brick_device

        # TODO: better name? also, could this be neater?
        try:
            self.is_silenced = kwargs["disable_sound"]
        except KeyError:
            self.is_silenced = False

    @staticmethod
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

    def run(self):
        """Run dha app :)"""

        self._console.clear()
        self._console.text_at(
            "LOOK AT DHIS '{}' SHIT".format(self.name),
            alignment="C",
            reset_console=True,
        )

    def boot_up_greeting(self):
        self.say("Bootin up, baby")
        self._console.text_at("Bootin up . . .", alignment="C")
        sleep(1)
        self._console.text_at("BINGO BANGO!", alignment="C", reset_console=True)
        self.say("BINGO BANGO!")

    def shut_down(self):
        self._console.text_at("I am a pickle!", reset_console=True, alignment="C")
        self.say("I am a pickle!")

        self._console.text_at("Bye forever", alignment="C")
        self.say("Bye forever")

    def say(self, text, **kwargs):
        if self.is_silenced:
            debug_logger(text)
        else:
            self._sound.speak(text, **kwargs)

    @property
    def port_a(self):
        return self.port_a

    @port_a.setter
    def port_a(self, value):
        self.port_a = value

    @property
    def port_b(self):
        return self.port_b

    @port_b.setter
    def port_b(self, value):
        self.port_b = value

    @property
    def port_c(self):
        return self.port_c

    @port_c.setter
    def port_c(self, value):
        self.port_c = value

    @property
    def port_d(self):
        return self.port_d

    @port_d.setter
    def port_d(self, value):
        self.port_d = value
