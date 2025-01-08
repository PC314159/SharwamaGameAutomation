import time
import pyautogui
import pydirectinput


def click(x, y):
    pydirectinput.mouseDown(x, y)
    pydirectinput.mouseUp(x, y)


def moveto(x, y, duration=0):
    pyautogui.moveTo(x, y, duration)


def holdclick(x, y):
    pydirectinput.mouseDown(x, y)


def releaseclick(x, y):
    pydirectinput.mouseUp(x, y)


def refill_pickles():
    click(258, 603)
    time.sleep(0.45)
    for i in range(10):
        click(401, 539)
    click(258, 603)


def refill_sourcream():
    click(258, 603)
    time.sleep(0.45)
    for i in range(10):
        click(401, 628)
    click(258, 603)


def chop_potato():
    moveto(1739, 708)
    holdclick(1739, 708)
    time.sleep(5)
    releaseclick(1739, 708)


def fill_fries():
    click(1550, 650)


def chop_meat():
    holdclick(384, 744)
    for i in range(12):
        moveto(455, 374)
        moveto(455, 603, 0.25)
    releaseclick(455, 603)


def make_shawarma():
    click(598, 861)
    for i in range(3):
        click(511, 745)
        click(664, 745)
        click(821, 745)
        click(969, 745)
    time.sleep(0.05)
    holdclick(949, 903)
    moveto(969, 771, 0.25)
    releaseclick(969, 771)
    time.sleep(0.3)
    holdclick(802, 846)
    moveto(1089, 814, 0.2)
    releaseclick(1089, 814)


def give_shawarma(x, y):
    holdclick(1089, 814)
    moveto(x, y, 0.1)
    releaseclick(x, y)


def collect_coins():
    holdclick(594, 627)
    moveto(1457, 627, 0.5)
    releaseclick(1457, 627)



if __name__ == '__main__':
    pydirectinput.PAUSE = 0.015
    pyautogui.MINIMUM_DURATION = 0.01
    pyautogui.FAILSAFE = True
    time.sleep(5)
    # chop_potato()
    # refill_pickles()
    # refill_sourcream()
    # chop_meat()
    # time.sleep(10)
    # fill_fries()
    # time.sleep(0.6)
    make_shawarma()
    time.sleep(5)
    collect_coins()
