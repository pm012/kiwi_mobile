from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def clear(self, calc): pass

    @abstractmethod
    def digit(self, calc, key): pass

    @abstractmethod
    def arifm(self, calc, key): pass

    @abstractmethod
    def equal(self, calc): pass

    @abstractmethod
    def show(self, calc): pass
