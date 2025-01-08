import heapq
import Action


class ActionHeap:
    def __init__(self):
        self.h = []

    def add(self, act: Action):
        heapq.heappush(self.h, act)

    def pop(self) -> Action:
        return heapq.heappop(self.h)
