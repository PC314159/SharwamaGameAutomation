import Action
import ActionHeap
import OrderHelper
import time
import threading

def automate():
    mouse_queue = ProcessQueue.ProcessQueue()
    order_queue = ProcessQueue.ProcessQueue()
    processes_in_queue = set()
    images = {
        "bronzecoin": "Data/bronzecoin.png",
        "fries": "Data/fries.png",
        "friestray": "Data/friestray.png",
        "oil": "Data/oil.png",
        "packed": "Data/packed.png",
        "pickles": "Data/pickles.png",
        "silvercoin": "Data/silvercoin.png",
        "sourcream": "Data/sourcream.png",
        "unpacked": "Data/unpacked.png"
    }

    oh = OrderHelper.OrderHelper()

    while True:
        oh.check_orders()
        if oh.get_current_order() is not None:
            pos, order = oh.get_current_order()

        time.sleep(0.001)


if __name__ == '__main__':
    automate()
