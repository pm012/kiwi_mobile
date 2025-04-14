from .state import State


class StateY(State):
    def __init__(self, factory):
        self.factory = factory
        self.typing = False

    def clear(self, calc):
        calc.x = 0
        calc.y = 0
        calc.op = '+'
        self.typing = False

    def digit(self, calc, key):
        if not self.typing:
            calc.y = 0
            self.typing = True
        calc.y = calc.y * 10 + int(key)

    def arifm(self, calc, key):
        calc.op = key
        calc.set_state(self.factory.get_action())

    def equal(self, calc):
        calc.set_state(self.factory.get_answer())
        calc.get_state().equal(calc)

    def show(self, calc):
        return str(calc.y)
