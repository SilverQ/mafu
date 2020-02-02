import pyautogui as pag
import time
import random
import cv2
import wx
from pytesseract import *
from skimage.metrics import structural_similarity
# import pyscreenshot as ImageGrab
from PIL import Image
import imutils


# 전체화면에서
nox_pos_x, nox_pos_y = 39, 36
# x, 39, y: 36

# while True:
#     time.sleep(random.uniform(2.01, 4.23))
#     x, y = pag.position()
#     print('x, %s, y: %s' % (x, y))

# but1 = {'t_l': {'x': 400, 'y': 500},
#         'b_r': {'x': 500, 'y': 600}}

# pag.moveTo(x=100, y=100)
# pag.moveTo(x=800, y=200)
# pag.moveTo(x=300, y=300)
# pag.moveTo(x=700, y=400)
# 쪽지 확인


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


# def pass_over_old():
#     # 건너뛰기
#     # x, 1601, y: 62
#     # x, 1796, y: 130
#     app = wx.App()
#     screen = wx.ScreenDC()
#     bmp = wx.Bitmap(1920, 1080)
#     mem = wx.MemoryDC(bmp)
#     # mem.Blit(0, 0, 1920, 1080, screen, 0, 0)
#     mem.Blit(1601, 62, 1796, 130, screen, 0, 0)
#     del mem
#     text = pytesseract.image_to_string(bmp, lang='kor')
#     print(text)


# def pass_over2_old():
#     screen = pag.screenshot(region=(1601, 62, 1796-1601, 130-62))
#     screen.save("button.jpg")
#
#     text = pytesseract.image_to_string(Image.open("button.jpg"), config='-psm 6')
#     # text = pytesseract.image_to_string(screen, lang='kor')
#     print(text)
#     # https: // pyautogui.readthedocs.io / en / latest / quickstart.html  # general-functions


# def pass_over3_old():
#     screen = pag.screenshot(region=(1601, 62, 1796-1601, 130-62))
#     screen.save("D:/tmp/tmp.jpg")
#     imageA = cv2.imread("D:/tmp/tmp.jpg")
#     # imageA = cv2.imread(screen)
#     # # imageA = screen.
#     imageB = cv2.imread("button.jpg")
#
#     # cv2.imshow("Screenshot", screen)
#     # cv2.imshow("SavedImage", imutils.resize(imageB, width=600))
#
#     # convert the images to grayscale
#     grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
#     grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
#
#     # images, ensuring that the difference image is returned
#     (score, diff) = structural_similarity(grayA, grayB, full=True)
#     # diff = (diff * 255).astype("uint8")
#     # print("SSIM: {}".format(score))
#     if score > 0.95:
#         mouse_click((1796+1601)/2 + random.uniform(0, (1796-1601)*0.7),
#                     (130+62)/2 + random.uniform(0, (130-62)*0.7))
#     # https://www.pyimagesearch.com/2017/06/19/image-difference-with-opencv-and-python/

# pass_over3()


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

# pass_over4()

# def capture_screen():
#     app = wx.App()
#     screen = wx.ScreenDC()
#     bmp = wx.Bitmap(1920, 1080)
#     mem = wx.MemoryDC(bmp)
#     # mem.Blit(0, 0, 1920, 1080, screen, 0, 0)
#     mem.Blit(100, 100, 500, 500, screen, 0, 0)
#     del mem
#     bmp.SaveFile('wx1.bmp', wx.BITMAP_TYPE_BMP)


# capture_screen()

# x, y = pag.position()
# print('x, %s, y: %s' % (x, y))
# # x, 3216, y: 244

def sleep_click(pos_x, pos_y, width, height, sleep_min, sleep_max):
    time.sleep(random.uniform(sleep_min, sleep_max))
    start_battle_x, start_battle_y = pos_x, pos_y
    mouse_click(start_battle_x + random.uniform(-0.4*width, 0.4*width),
                start_battle_y + random.uniform(-0.4*height, 0.4*height))


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
            if pag.locateOnScreen('reload_button.jpg', grayscale=True, confidence=.9):
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
    button = pag.locateOnScreen(filename, grayscale=True, confidence=.9)
    print(button)
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


dimension_mission(10)

# while True:
#     button_assistance()
#     # dimension_mission()
#
#     # start_battle
#     # while not pag.locateOnScreen('reload_button.jpg', grayscale=True, confidence=.9):
#     #     time.sleep(random.uniform(2.01, 5.23))
#     # check_click('reload_button.jpg')
