from .state import State


class StateAction(State):
    def __init__(self, factory):
        self.factory = factory
        self.typing = False
    
    
    def clear(self, calc):
       calc.x = 0
       calc.y = 0
       calc.op = '+'
       self.typing = False       
        

    def digit(self, calc, key):
        next_state = self.factory.get_y()
        next_state.typing = False
        calc.set_state(next_state)
        next_state.digit(calc, key)

    def arifm(self, calc, key):
        calc.op = key

    def equal(self, calc):
        calc.y = calc.x
        calc.set_state(self.factory.get_answer())
        calc.get_state().equal(calc)

    def show(self, calc):
        return f"{calc.x} {calc.op}"
