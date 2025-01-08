import time
import pyautogui

import TemplateMatcher


class OrderHelper:
    def __init__(self, mode: int = 3):
        self.mode = mode
        self.current_order = None
        self.orders_set = set()
        self.orders_queue = []
        self.heart_color = (205, 25, 25)
        self.order_heart_pos = {
            3: [(635, 560), (945, 560), (1255, 560)]
        }
        self.screenshot_pos = {
            3: [(740, 490), (1050, 490), (1360, 490)]
        }

    def add_order(self, pos: int):
        print(pos)
        order = []
        scx, scy = self.screenshot_pos[self.mode][pos]
        sc = pyautogui.screenshot("Data/order_temp.png", (scx, scy, scx + 80, scy + 100))

        sharwamas = len(TemplateMatcher.order_matching(sc, "Data/sharwama_order"))
        for _ in range(sharwamas):
            order.append("sharwama")

        self.orders_set.add(pos)
        self.orders_queue.append((pos, order))

    def check_order(self, pos: int):
        if pos in self.orders_set:
            return
        else:
            x, y = self.order_heart_pos[self.mode][pos]
            for i in range(-9, 10, 3):
                if pyautogui.pixelMatchesColor(x, y + i, self.heart_color, 30):
                    print("add_order", pos)
                    self.add_order(pos)
                    break

    def check_orders(self):
        for k in range(self.mode):
            self.check_order(k)

    def complete_order(self):
        if self.current_order is not None:
            self.orders_set.remove(self.current_order[0])
            self.current_order = None

    def next_order(self) -> tuple | None:
        self.complete_order()
        if len(self.orders_queue) > 0:
            self.current_order = self.orders_queue.pop(0)
            return self.current_order
        return None

    def get_current_order(self) -> tuple | None:
        return self.current_order


if __name__ == '__main__':
    time.sleep(3)
    oh = OrderHelper()
    oh.check_orders()
    print(oh.orders_queue)
