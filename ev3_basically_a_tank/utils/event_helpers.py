"""
Minimal implementations of helpers for handling event-driven operations

derived from the following:
- https://stackoverflow.com/questions/1092531/which-python-packages-offer-a-stand-alone-event-system
    - _specifically: https://stackoverflow.com/a/28479007_
- https://github.com/riga/pymitter
"""


class Observer:
    _observers = (
        []
    )  # maybe implement as dictionary instead so that observers can be named?
    _observed_events = []

    def __init__(self):
        self.observers.append(self)
        self.observed_events = []

    def observe(self, event_name="", callback_fn=None):
        try:
            self.observed_events.append(
                {"event_name": event_name, "callback_fn": callback_fn}
            )
        except Exception as e:
            raise e

    @property
    def observers(self):
        return self._observers

    @observers.setter
    def observers(self, value):
        self._observers = value

    @property
    def observed_events(self):
        return self._observed_events

    @observed_events.setter
    def observed_events(self, value):
        self._observed_events = value


def fire_event(event_name, *callback_args):
    if event_name is not str or event_name is None:
        raise ValueError(
            "'event_name' must be a non-empty string; a value of {} was given".format(
                event_name
            )
        )

    for observer in Observer._observers:
        for observable in observer._observed_events:
            if observable["event_name"] == event_name:
                observable["callback_fn"](*callback_args)
