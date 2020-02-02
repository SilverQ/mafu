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


# 전체화면에서
nox_pos_x, nox_pos_y = 39, 36


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


def mouse_click(pos_x, pos_y):
    x, y = pag.position()
    pag.moveTo(pos_x, pos_y)
    pag.mouseDown()
    # time.sleep(random.uniform(1.01, 2.23))
    time.sleep(random.uniform(0.21, 0.43))
    pag.mouseUp()
    pag.moveTo(x, y)


def pass_over4():
    # 버튼의 이미지가 있다면, 화면에서 해당 버튼의 좌표를 산출할 수 있다.
    # https://pyautogui.readthedocs.io/en/latest/screenshot.html
    # pass_over_button = pag.locateOnScreen('button_pass_over.jpg')
    pass_over_button = pag.locateOnScreen('button_pass_over.jpg', grayscale=True, confidence=.7)
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


def sleep_click(pos_x, pos_y, width, height, sleep_min, sleep_max):
    time.sleep(random.uniform(sleep_min, sleep_max))
    start_battle_x, start_battle_y = pos_x, pos_y
    mouse_click(start_battle_x + random.uniform(-0.4*width, 0.4*width),
                start_battle_y + random.uniform(-0.4*height, 0.4*height))


def sleep_click_v2(pos_x1, pos_y1, pos_x2, pos_y2, sleep_min, sleep_max):
    time.sleep(random.uniform(sleep_min, sleep_max))
    center_x, center_y = (pos_x1+pos_x2)/2, (pos_y1+pos_y2)/2
    mouse_click(center_x + random.uniform(-0.4*(pos_x2-pos_x1), 0.4*(pos_x2-pos_x1)),
                center_y + random.uniform(-0.4*(pos_y2-pos_y1), 0.4*(pos_y2-pos_y1)))


def dimension_mission(num):
    # 다른 화면이라면 홈으로
    # sleep_click(pos_x, pos_y, width, height, sleep_min, sleep_max)

    # start_battle
    # time.sleep(random.uniform(2.01, 4.23))
    # start_battle_x, start_battle_y = 1645, 988
    # mouse_click(start_battle_x + random.uniform(-1.3, 1.2),
    #             start_battle_y + random.uniform(-10, 10))
    sleep_click(1645, 988, 3, 25, 0.31, 4.23)

    # select_mission
    # time.sleep(random.uniform(2.01, 4.23))
    # select_mission_x, select_mission_y = 729, 659
    # mouse_click(select_mission_x + random.uniform(-200, 200),
    #             select_mission_y + random.uniform(-300, 300))
    sleep_click(729, 659, 930-729, 983-329, 1.01, 2.23)
    # x, 515, y: 329 ~ x, 930, y: 983

    for i in range(num):
        # ready_battle
        # time.sleep(random.uniform(3.01, 5.23))
        # ready_battle_x, ready_battle_y = 930, 986
        # mouse_click(ready_battle_x + random.uniform(-100, 100),
        #             ready_battle_y + random.uniform(-30, 30))
        sleep_click(930, 986, 250, 70, 2.01, 4.23)
        # x, 765, y: 953 ~ x, 1082, y: 1013

        # start_battle
        # time.sleep(random.uniform(2.01, 5.23))
        # start_battle_x, start_battle_y = 1618, 977
        # mouse_click(start_battle_x + random.uniform(-150, 150),
        #             start_battle_y + random.uniform(-30, 30))
        sleep_click(1618, 977, 300, 70, 2.01, 4.23)
        # x, 1438, y: 944 ~ x, 1780, y: 1006

        # "not_use_button.jpg"
        time.sleep(random.uniform(2.01, 4.23))
        check_click('not_use_button.jpg')
        # sleep_click(pos_x, pos_y, width, height, sleep_min, sleep_max)

        while True:
            if pag.locateOnScreen('buttons/reload_button.jpg', grayscale=True, confidence=.9):
                check_click('reload_button.jpg')
                break
            else:
                time.sleep(random.uniform(4, 5))

    #     # dimension_mission()

    # time.sleep(random.uniform(2.01, 5.23))
    # att_1_x, att_1_y = 1578, 667
    # mouse_click(att_1_x + random.uniform(-50, 50),
    #             att_1_y + random.uniform(-50, 50))
    # # x, 1438, y: 944 ~ x, 1780, y: 1006
    # # att_1_x, att_1_y = x, 1578, y: 667
    # # att_2_x, att_2_y = x, 1466, y: 781
    # # att_3_x, att_3_y = x, 1744, y: 668
    # # att_4_x, att_4_y = x, 1474, y: 944
    # # att_5_x, att_5_y = x, 1320, y: 936
    # # 반지름은 100 정도 되는듯


def iter_battle(cnt):
    for i in range(cnt):
        sleep_click(1618, 977, 300, 70, 2.01, 4.23)        # start_battle
        while True:
            if pag.locateOnScreen('buttons/reload_button.jpg', grayscale=True, confidence=.9):
                time.sleep(random.uniform(2, 3))
                check_click('reload_button.jpg')
                time.sleep(random.uniform(4, 5))
                break
            else:
                time.sleep(random.uniform(4, 5))


def epic_quest(quest_seq, cnt):
    # 다른 화면이라면 홈으로
    # sleep_click(pos_x, pos_y, width, height, sleep_min, sleep_max)

    print('enter battle')
    sleep_click(1645, 988, 3, 25, 2.31, 4.23)   # enter_battle

    print('epic quest')
    sleep_click_v2(982, 326, 1376, 967, 2.01, 3.23)     # select_mission

    if quest_seq == 3:  # 라이즈 오브 엑스맨
        print('select_mission')
        sleep_click_v2(1221, 215, 1712, 800, 2.01, 3.23)  # select_mission
        sleep_click_v2(767, 764, 860, 854, 2.01, 3.23)  # chasing
        for i in range(4):
            if i == 0:
                pass
                # sleep_click_v2(308, 315, 545, 674, 2.01, 3.23)  # select_mission
                # sleep_click_v2(1274, 730, 1454, 784, 2.01, 3.23)  # select_battle
                # iter_battle(cnt)
                # check_click('back_button.jpg')
            elif i == 1:
                pass
                # sleep_click_v2(646, 317, 879, 676, 2.01, 3.23)  # select_mission
                # sleep_click_v2(1274, 730, 1454, 784, 2.01, 3.23)  # select_battle
                # iter_battle(cnt)
                # check_click('back_button.jpg')
            elif i == 2:
                pass
                # sleep_click_v2(977, 314, 1220, 675, 2.01, 3.23)  # select_mission
                # sleep_click_v2(1274, 730, 1454, 784, 2.01, 3.23)  # select_battle
                # iter_battle(cnt)
                # check_click('back_button.jpg')
            elif i == 3:
                sleep_click_v2(1312, 311, 1551, 670, 2.01, 3.23)  # select_mission
                sleep_click_v2(1274, 730, 1454, 784, 2.01, 3.23)  # select_battle
                iter_battle(cnt)

    # for i in range(cnt):
    #     sleep_click(930, 986, 250, 70, 2.01, 4.23)        # ready_battle
    #     sleep_click(1618, 977, 300, 70, 2.01, 4.23)       # start_battle
    #
    #     # "not_use_button.jpg"
    #     time.sleep(random.uniform(2.01, 4.23))
    #     check_click('not_use_button.jpg')
    #     # sleep_click(pos_x, pos_y, width, height, sleep_min, sleep_max)
    #
    #     while True:
    #         if pag.locateOnScreen('buttons/reload_button.jpg', grayscale=True, confidence=.9):
    #             check_click('reload_button.jpg')
    #             break
    #         else:
    #             time.sleep(random.uniform(4, 5))

    #     # dimension_mission()

    # time.sleep(random.uniform(2.01, 5.23))
    # att_1_x, att_1_y = 1578, 667
    # mouse_click(att_1_x + random.uniform(-50, 50),
    #             att_1_y + random.uniform(-50, 50))
    # # x, 1438, y: 944 ~ x, 1780, y: 1006
    # # att_1_x, att_1_y = x, 1578, y: 667
    # # att_2_x, att_2_y = x, 1466, y: 781
    # # att_3_x, att_3_y = x, 1744, y: 668
    # # att_4_x, att_4_y = x, 1474, y: 944
    # # att_5_x, att_5_y = x, 1320, y: 936
    # # 반지름은 100 정도 되는듯


def start_battle():
    pag.moveTo(x=911, y=962)
    pag.mouseDown()
    time.sleep(random.uniform(0.01,0.23))
    pag.mouseUp()


def skip():
    pag.moveTo(x=973, y=481)
    pag.mouseDown()
    time.sleep(random.uniform(0.01,0.23))
    pag.mouseUp()


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

# start_battle()
# skip()
# dimension_mission()


def button_assistance():
    time.sleep(random.uniform(1.5, 2))
#     pass_over4()
    check_click('button_pass_over.jpg')
    check_click('move_to_slot.jpg')
    # check_click('right_arrow.jpg')
    check_click('x_button.jpg')
    check_click('ok_button.jpg')


def check_status():
    if pag.locateOnScreen('reload_button.jpg', grayscale=True, confidence=.9):
        return True
    else:
        return False


# dimension_mission(10)
epic_quest(3, 10)

# while True:
#     button_assistance()
#     # dimension_mission()
#
#     # start_battle
#     # while not pag.locateOnScreen('reload_button.jpg', grayscale=True, confidence=.9):
#     #     time.sleep(random.uniform(2.01, 5.23))
#     # check_click('reload_button.jpg')
