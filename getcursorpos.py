import pyautogui
import time


def getcursorpos():
    print(pyautogui.size())
    while True:
        time.sleep(1)
        print(pyautogui.position())

if __name__ == '__main__':
    getcursorpos()