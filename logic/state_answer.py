from .state import State



class StateAnswer(State):
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
            calc.x = 0
            self.typing = True
        # Transition to X state and forward digit
        calc.get_state(self.factory.get_x())
        calc.get_state().digit(calc,key)
                

    def arifm(self, calc, key):
        
        calc.set_state(self.factory.get_action())
        calc.get_state().arifm(calc, key)

    def equal(self, calc):
        if calc.op == '+':
            calc.x += calc.y
        elif calc.op == '-':
            calc.x -= calc.y
        elif calc.op == '*':
            calc.x *= calc.y
        elif calc.op == '/':
            calc.x = calc.x // calc.y if calc.y != 0 else 0        # basic error handling

    def show(self, calc):
        return "= " + str(calc.x)
