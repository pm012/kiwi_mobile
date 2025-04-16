from .state import State



class StateAnswer(State):
    def __init__(self, factory):
        self.factory = factory
        self.typing = False
        self.last_op = None
        self.last_y = None
        
    
    def clear(self, calc):
        calc.x = 0
        calc.y = 0
        calc.op = '+'
        self.typing = False

    def digit(self, calc, key):
        # if not self.typing:
        #     calc.x = 0
        #     self.typing = True
        # Transition to X state and forward digit
        next_state=self.factory.get_x()
        next_state.typing = False
        calc.set_state(next_state)
        next_state.digit(calc, key)
                

    def arifm(self, calc, key):
        calc.op = key
        calc.y = 0
        self.typing = False 
        next_state = self.factory.get_action()
        next_state.typing = False
        calc.set_state(next_state)       
        # calc.set_state(self.factory.get_action())
        # calc.get_state().arifm(calc, key)

    def equal(self, calc):
        if calc.last_op is None or calc.last_y is None:
            return  # No operation to repeat

        if calc.last_op == '+':
            calc.x += calc.last_y
        elif calc.last_op == '-':
            calc.x -= calc.last_y
        elif calc.last_op == '*':
            calc.x *= calc.last_y
        elif calc.last_op == '/':
            calc.x = calc.x // calc.last_y if calc.last_y != 0 else 0




    def show(self, calc):
        return "= " + str(calc.x)
