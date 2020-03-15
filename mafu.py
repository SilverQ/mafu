import pyautogui as pag
import time
import random
import os
import cv2
import wx
from pytesseract import *
from skimage.metrics import structural_similarity
# import pyscreenshot as ImageGrab
from PIL import Image
import imutils
from utils import *
# import tqdm


'''
to utils

# def go_home():
#     # go to home if not home
#     time.sleep(random.uniform(0.2, 0.5))
#     check_click_v2('go_home.jpg')
#     time.sleep(random.uniform(0.5, 1.5))

# def check_click_v2(filename):
#     button = pag.locateOnScreen(os.path.join('buttons/', filename), grayscale=True, confidence=.9)
#     print(filename, button)
#     # Box(left=1416, top=562, width=50, height=41)
#     if button is not None:
#         try:
#             mouse_click(button[0] + button[2] / 2 + random.uniform(0, button[2] * 0.3),
#                         button[1] + button[3] / 2 + random.uniform(0, button[3] * 0.3))
#         finally:
#             pass

def wait_click(filename):
    while True:
        if pag.locateOnScreen(os.path.join('buttons/', filename), grayscale=True, confidence=.9):
            time.sleep(random.uniform(1.1, 1.5))
            check_click(filename)
            time.sleep(random.uniform(0.1, 0.5))
            if pag.locateOnScreen(os.path.join('buttons/', filename), grayscale=True, confidence=.9) is None:
                break
        else:
            time.sleep(random.uniform(0.5, 1))



def check_click(filename):
    # 버튼의 이미지가 있다면, 화면에서 해당 버튼의 좌표를 산출할 수 있다.
    # https://pyautogui.readthedocs.io/en/latest/screenshot.html
    # pass_over_button = pag.locateOnScreen('button_pass_over.jpg')
    button = pag.locateOnScreen(os.path.join('buttons/', filename), grayscale=True, confidence=.9)
    print(os.path.join('buttons/', filename), button)
    # https://automatetheboringstuff.com/chapter18/
    # locateOnScreen은 이미지가 완벽하게 매칭되어야 함 ㅠㅠ
    # Note that the image on the screen must match the provided image perfectly in order to be recognized.

    # Box(left=1416, top=562, width=50, height=41)
    if button is not None:
        try:
            print(button[0])
            mouse_click(button[0] + button[2]/2 + random.uniform(0, button[2]*0.3),
                        button[1] + button[3]/2 + random.uniform(0, button[3]*0.3))
            # pag.moveTo(x=pass_over_button[0], y=pass_over_button[1])
        finally:
            pass

def mouse_click(pos_x, pos_y):
    x, y = pag.position()
    pag.moveTo(pos_x, pos_y)
    pag.mouseDown()
    # time.sleep(random.uniform(1.01, 2.23))
    time.sleep(random.uniform(0.21, 0.43))
    pag.mouseUp()
    pag.moveTo(x, y)

'''
# 전체화면에서
nox_pos_x, nox_pos_y = 39, 36


def pass_over4():
    # 버튼의 이미지가 있다면, 화면에서 해당 버튼의 좌표를 산출할 수 있다.
    # https://pyautogui.readthedocs.io/en/latest/screenshot.html
    # pass_over_button = pag.locateOnScreen('button_pass_over.jpg')
    pass_over_button = pag.locateOnScreen('buttons/pass_over.jpg', grayscale=True, confidence=.7)
    print(pass_over_button)
    # https://automatetheboringstuff.com/chapter18/
    # locateOnScreen은 이미지가 완벽하게 매칭되어야 함 ㅠㅠ
    # Note that the image on the screen must match the provided image perfectly in order to be recognized.

    # Box(left=1416, top=562, width=50, height=41)
    if pass_over_button is not None:
        print(pass_over_button[0])
        mouse_click(pass_over_button[0] + pass_over_button[2]/2 + random.uniform(0, pass_over_button[2]*0.3),
                    pass_over_button[1] + pass_over_button[3]/2 + random.uniform(0, pass_over_button[3]*0.3))
        # pag.moveTo(x=pass_over_button[0], y=pass_over_button[1])


def epic_quest(quest_seq, cnt):
    # 다른 화면이라면 홈으로
    # sleep_click(pos_x, pos_y, width, height, sleep_min, sleep_max)

    print('enter battle')
    sleep_click(1645, 988, 3, 25, 1.01, 1.73)   # enter_battle

    print('epic quest')
    sleep_click_v2(982, 326, 1376, 967, 1.01, 1.93)     # select_mission

    if quest_seq == 3:  # 라이즈 오브 엑스맨
        print('select_mission')
        sleep_click_v2(1221, 215, 1712, 800, 1.01, 1.53)  # select_mission
        sleep_click_v2(767, 764, 860, 854, 1.01, 1.53)  # chasing
        for i in range(4):
            if i == 0:
                # pass
                sleep_click_v2(308, 315, 545, 674, 1.01, 2.23)  # select_mission
                sleep_click_v2(1274, 730, 1454, 784, 1.01, 2.23)  # select_battle
                iter_battle(cnt)
                check_click('back_button.jpg')
            elif i == 1:
                # pass
                sleep_click_v2(646, 317, 879, 676, 1.01, 2.23)  # select_mission
                sleep_click_v2(1274, 730, 1454, 784, 1.01, 2.23)  # select_battle
                iter_battle(cnt)
                check_click('back_button.jpg')
            elif i == 2:
                # pass
                sleep_click_v2(977, 314, 1220, 675, 1.01, 2.23)  # select_mission
                sleep_click_v2(1274, 730, 1454, 784, 1.01, 2.23)  # select_battle
                iter_battle(cnt)
                check_click('back_button.jpg')
            elif i == 3:
                # pass
                sleep_click_v2(1312, 311, 1551, 670, 2.01, 3.23)  # select_mission
                sleep_click_v2(1274, 730, 1454, 784, 2.01, 3.23)  # select_battle
                iter_battle(cnt)


def start_battle():
    pag.moveTo(x=911, y=962)
    pag.mouseDown()
    time.sleep(random.uniform(0.01, 0.23))
    pag.mouseUp()


def skip():
    pag.moveTo(x=973, y=481)
    pag.mouseDown()
    time.sleep(random.uniform(0.01, 0.23))
    pag.mouseUp()


def button_assistance():
    time.sleep(random.uniform(1.5, 2))
#     pass_over4()
    check_click('button_pass_over.jpg')
    check_click('move_to_slot.jpg')
    check_click('right_arrow.jpg')
    check_click('x_button.jpg')
    check_click('ok_button.jpg')


def check_status():
    if pag.locateOnScreen('reload_button.jpg', grayscale=True, confidence=.9):
        return True
    else:
        return False


def check_att():
    # 건너뛰기
    # x, 1601, y: 62
    # x, 1796, y: 130
    app = wx.App()
    screen = wx.ScreenDC()
    bmp = wx.Bitmap(1920, 1080)
    mem = wx.MemoryDC(bmp)
    # mem.Blit(0, 0, 1920, 1080, screen, 0, 0)
    mem.Blit(1578, 1006, 1678, 1106, screen, 0, 0)
    del mem
    text = pytesseract.image_to_string(bmp, lang='kor')
    print(text)
    # x, 1438, y: 944 ~ x, 1780, y: 1006
    # att_1_x, att_1_y = x, 1578, y: 667
    # att_2_x, att_2_y = x, 1466, y: 781
    # att_3_x, att_3_y = x, 1744, y: 668
    # att_4_x, att_4_y = x, 1474, y: 944
    # att_5_x, att_5_y = x, 1320, y: 936
    # 반지름은 100 정도 되는듯


# check_att()


def wait(filename):
    while True:
        if pag.locateOnScreen(os.path.join('buttons/', filename), grayscale=True, confidence=.9):
            break
        else:
            time.sleep(random.uniform(1.0, 2))


def wait_click_v2(condition, filename):
    while True:
        if pag.locateOnScreen(os.path.join('buttons/', condition), grayscale=True, confidence=.9):
            time.sleep(random.uniform(0.1, 0.5))
            check_click(filename)
            time.sleep(random.uniform(0.1, 0.5))
            if pag.locateOnScreen(os.path.join('buttons/', filename), grayscale=True, confidence=.9) is None:
                break
        else:
            time.sleep(random.uniform(0.5, 1))


def iter_battle_v2(condition):
    while True:
        sleep_click(1618, 977, 300, 70, 2.51, 4.23)        # start_battle
        while True:
            if pag.locateOnScreen('buttons/reload_button.jpg', grayscale=True, confidence=.9):
                time.sleep(random.uniform(3, 4))
                check_click('reload_button.jpg')
                time.sleep(random.uniform(2.5, 3.5))
                break
            else:
                time.sleep(random.uniform(2, 3))


def check_status_v2(filename, confidence=0.9):
    if pag.locateOnScreen(os.path.join('buttons/', filename), grayscale=True, confidence=confidence):
        return True
    else:
        return False


def world_boss():
    go_home()    # go to home if not home
    wait_click('enter_battle.jpg', 0.1, 0.5, 0, 0, 1)
    wait_click('mission_02.jpg', 0.1, 0.5, 0, 0, 1)
    wait_click('world_boss.jpg', 0.1, 0.5, 0, 0, 1)
    for i in range(4):
        check_click_v2('ready_mission.jpg')
    print('end iteration')


def world_boss_envasion():
    go_home()
    wait_click('enter_battle.jpg', 0.1, 0.5, 0, 0, 1)
    wait_click('mission_04.jpg', 0.1, 0.5, 0, 0, 1)
    wait_click('world_boss_envasion.jpg.jpg', 0.1, 0.5, 0, 0, 1)


# world_boss_envasion()


def ehdgml7602():
    # change_account(1)  # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020
    # check_click('x_button.jpg')

    # dimension_mission(10)
    # time.sleep(random.uniform(2.71, 3.53))
    #
    # first_family(0, 0, 3, 3, 3)        # 10, 0, 3, 3, 3
    # time.sleep(random.uniform(2.71, 3.53))

    # x_force(0, 10, 3, 3, 3)       # 10, 10, 3, 3, 3
    # time.sleep(random.uniform(2.71, 3.53))

    rise_xman(5, 10, 10, 10, 2, 2)     # 10, 10, 10, 10, 2, 2
    time.sleep(random.uniform(2.71, 3.53))

    sorcerer_supreme(3, 3)
    time.sleep(random.uniform(2.71, 3.53))


def ehdgml7604():
    # change_account(2)  # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020
    # time.sleep(random.uniform(2.71, 3.53))

    # dimension_mission(10)
    # time.sleep(random.uniform(2.71, 3.53))

    # first_family(0, 0, 0, 0, 3)        # 10, 10, 3, 3, 3
    # time.sleep(random.uniform(2.71, 3.53))

    x_force(0, 0, 0, 3, 0)         # 10, 0, 3, 3, 0
    time.sleep(random.uniform(2.71, 3.53))

    rise_xman(10, 10, 10, 10, 0, 0)
    # rise_xman(0, 0, 0, 0, 2, 2)     # 10, 10, 10, 10, 2, 2
    time.sleep(random.uniform(2.71, 3.53))

    # sorcerer_supreme(3, 3)


def handhee2020():
    # change_account(3)  # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020

    # dimension_mission(10)
    # time.sleep(random.uniform(2.71, 3.53))
    #
    # first_family(0, 0, 3, 3, 0)        # 10, 0, 3, 3, 0
    # time.sleep(random.uniform(2.71, 3.53))

    x_force(10, 0, 3, 0, 0)             # 10, 0, 3, 0, 0
    time.sleep(random.uniform(2.71, 3.53))

    rise_xman(10, 10, 10, 10, 2, 2)     # 10, 10, 10, 10, 2, 2
    time.sleep(random.uniform(2.71, 3.53))
    #
    # sorcerer_supreme(3, 3)


def test():
    # change_account(2)  # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020

    dimension_mission(0)
    time.sleep(random.uniform(2.71, 3.53))

    first_family(0, 0, 0, 0)
    time.sleep(random.uniform(2.71, 3.53))

    x_force(0, 0)
    time.sleep(random.uniform(2.71, 3.53))

    rise_xman(0, 0, 0, 0, 0, 0)
    time.sleep(random.uniform(2.71, 3.53))

    sorcerer_supreme(3, 3)


# test()
# ehdgml7602()        # 한또르(홍미)
# ehdgml7604()        # StarangeHee
# handhee2020()

# while True:
#     button_assistance()
#     # dimension_mission()
#
#     # start_battle
#     # while not pag.locateOnScreen('reload_button.jpg', grayscale=True, confidence=.9):
#     #     time.sleep(random.uniform(2.01, 5.23))
#     # check_click('reload_button.jpg')


# change_account(1)   # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020
dimension_mission(10)
# x_force(0, 9, 0, 0)
# first_family(0, 10, 0, 0, 0)

# legendary_battle(3)     # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020
