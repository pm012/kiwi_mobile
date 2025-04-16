from .state_x import StateX
from .state_y import StateY
from .state_action import StateAction
from .state_answer import StateAnswer

from .state_x import StateX
from .state_y import StateY
from .state_action import StateAction
from .state_answer import StateAnswer

class StateFactory:
    def __init__(self):
        self._x = StateX(self)
        self._y = StateY(self)
        self._action = StateAction(self)
        self._answer = StateAnswer(self)

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_action(self):
        return self._action

    def get_answer(self):
        return self._answer

