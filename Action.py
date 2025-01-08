from functools import total_ordering
from typing import Callable

from overrides import overrides


@total_ordering
class Action:
    def __init__(self, priority: int = 0, func: Callable = None, params: tuple = None):
        self.priority = priority
        self.func = func
        self.params = params

    def get_priority(self):
        return self.priority

    def get_func(self):
        return self.func

    def get_params(self):
        return self.params

    def execute(self):
        try:
            return self.func(*self.params)
        except NameError:
            print("---")
            print("NameError while performing action")
            print("func: ", self.func)
            print("params: ", self.params)
            print("---")
        except TypeError:
            print("---")
            print("TypeError while performing action")
            print("func: ", self.func)
            print("params: ", self.params)
            print("---")

    def __lt__(self, other):
        if other is Action:
            return self.priority < other.get_priority()
        raise TypeError("Comparing Action to Non-Action")

    @overrides
    def __eq__(self, other):
        if other is Action:
            return self.priority == other.get_priority()
        raise TypeError("Comparing Action to Non-Action")
