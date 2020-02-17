import pyautogui as pag
import cv2
from pytesseract import *
from PIL import Image
from scipy.ndimage import rotate
import time
import random
import os


# def ocr_att_button():
#     # att5
#     # 1291, 920, 50, 50
#
#     screen = pag.screenshot(region=(1291, 920, 50, 50))
#     screen.save("att_button_tmp.jpg")
#     image = cv2.imread("att_button_tmp.jpg")
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     # gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
#     gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
#     gray = cv2.medianBlur(gray, 1)
#     # rot = rotate(img, -20, reshape=False)
#     gray = rotate(gray, 20, reshape=False)
#     cv2.imwrite("att_button_tmp.jpg", gray)
#     custom_oem_psm_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789.%'
#     text = pytesseract.image_to_string(Image.open('att_button_tmp.jpg'), lang='eng',
#                                        # config='--psm 7 -c tessedit_char_whitelist=0123456789.%')
#                                        config=custom_oem_psm_config)
#     print(text)
#     # 숫자 인식률이 개그지, 파일 저장이 중간에 과다하게 들어가고, 파일 저장 없이 바로 이용하는 방법 아직 찾지 못함
#
#
# while True:
#     time.sleep(1)
#     ocr_att_button()

# att_1_x, att_1_y = x, 1502, y: 590
# 1502, 590, 140, 140
# att_button_1.jpg

# att_2_x, att_2_y = x, 1391, y: 711
# att_button_2.jpg

# att_3_x, att_3_y = x, 1666, y: 595
# att_4_x, att_4_y = x, 1414, y: 873
# att_5_x, att_5_y = x, 1246, y: 873
# 반지름은 140 정도 되는듯


def check_click_v2(filename):
    button = pag.locateOnScreen(os.path.join('buttons/', filename), grayscale=True, confidence=.9)
    print(filename, button)
    # Box(left=1416, top=562, width=50, height=41)
    if button is not None:
        try:
            mouse_click(button[0] + button[2] / 2 + random.uniform(0, button[2] * 0.3),
                        button[1] + button[3] / 2 + random.uniform(0, button[3] * 0.3))
        finally:
            pass


def go_home():
    # go to home if not home
    time.sleep(random.uniform(0.2, 0.5))
    check_click_v2('go_home.jpg')
    time.sleep(random.uniform(0.5, 1.5))


def mouse_click(pos_x, pos_y):
    x, y = pag.position()
    pag.moveTo(pos_x, pos_y)
    pag.mouseDown()
    # time.sleep(random.uniform(1.01, 2.23))
    time.sleep(random.uniform(0.21, 0.43))
    pag.mouseUp()
    pag.moveTo(x, y)


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

