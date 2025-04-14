from .state_x import StateX
from .state_y import StateY
from .state_action import StateAction
from .state_answer import StateAnswer

class StateFactory:
    def __init__(self):
        self.state_x = StateX(self)
        self.state_y = StateY(self)
        self.state_action = StateAction(self)
        self.state_answer = StateAnswer(self)

    def get_x(self): return self.state_x
    def get_y(self): return self.state_y
    def get_action(self): return self.state_action
    def get_answer(self): return self.state_answer
