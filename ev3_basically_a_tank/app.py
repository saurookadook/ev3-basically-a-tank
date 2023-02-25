from time import sleep

from .utils import debug_logger


class App:

    __slots__ = [
        "_name",
        "_brick_device",
        "_buttons",
        "_console",
        "_is_silenced",
        "_input_1",
        "_input_2",
        "_input_3",
        "_input_4",
        "_port_a",
        "_port_b",
        "_port_c",
        "_port_d",
        "_sound",
    ]

    def __init__(self, name="", brick_device=None, **kwargs):
        self.name = name
        self.brick_device = brick_device

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

    @staticmethod
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
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def brick_device(self):
        return self._brick_device

    @brick_device.setter
    def brick_device(self, value):
        self._brick_device = value

    @property
    def buttons(self):
        self._buttons

    @buttons.setter
    def buttons(self, value):
        self._buttons = value

    @property
    def console(self):
        self._console

    @console.setter
    def console(self, value):
        self._console = value

    @property
    def is_silenced(self):
        self._is_silenced

    @is_silenced.setter
    def is_silenced(self, value):
        self._is_silenced = value

    @property
    def input_1(self):
        return self._input_1

    @input_1.setter
    def input_1(self, value):
        self._input_1 = value

    @property
    def input_2(self):
        return self._input_2

    @input_2.setter
    def input_2(self, value):
        self._input_2 = value

    @property
    def input_3(self):
        return self._input_3

    @input_3.setter
    def input_3(self, value):
        self._input_3 = value

    @property
    def input_4(self):
        return self._input_4

    @input_4.setter
    def input_4(self, value):
        self._input_4 = value

    @property
    def port_a(self):
        return self._port_a

    @port_a.setter
    def port_a(self, value):
        self._port_a = value

    @property
    def port_b(self):
        return self._port_b

    @port_b.setter
    def port_b(self, value):
        self._port_b = value

    @property
    def port_c(self):
        return self._port_c

    @port_c.setter
    def port_c(self, value):
        self._port_c = value

    @property
    def port_d(self):
        return self._port_d

    @port_d.setter
    def port_d(self, value):
        self._port_d = value

    @property
    def sound(self):
        self._sound

    @sound.setter
    def sound(self, value):
        self._sound = value
