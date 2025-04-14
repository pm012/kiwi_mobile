from .state_factory import StateFactory

class Calculator:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.op = '+'
        self.factory = StateFactory()
        self.state = self.factory.get_x()
        self.state.clear(self)

    def press(self, key):
        if key in 'cC':
            self.state.clear(self)
        elif key.isdigit():
            self.state.digit(self, key)
        elif key in '+-*/':
            self.state.arifm(self, key)
        elif key == '=':
            self.state.equal(self)

    def set_state(self, state): self.state = state
    def get_state(self): return self.state
    def get_factory(self): return self.factory

    def show(self): return self.state.show(self)

    def __str__(self):
        return f"x={self.x} y={self.y} op={self.op} state={type(self.state).__name__}"
