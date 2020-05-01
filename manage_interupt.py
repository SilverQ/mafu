import cv2
import imutils
import json
import os
import pickle
import pyautogui as pag
# import pyscreenshot as ImageGrab
import random
import time
import tqdm
import wx
from pytesseract import *
from skimage.metrics import structural_similarity
from PIL import Image
from utils import *
from scipy.ndimage import rotate
# from tqdm import tqdm

button_path2 = 'buttons(960x540)/'


def check_interupt(filename):
    return pag.locateOnScreen(os.path.join(button_path2, filename), grayscale=True, confidence=.9)


def manage_inventory():
    wait_click('special_items.jpg')
    # wait_click('whole_sale.jpg')
    # wait_click('iso8.jpg')
    # wait_click('comics_cards.jpg')


while True:
    pag.press('volumedown')
    if check_interupt('interupt01.jpg') is not None:
        check_click_v2('x_button.jpg')
    if check_interupt('ok_button.jpg') is not None:
        check_click_v2('ok_button.jpg')
    if check_interupt('ok_button_01.jpg') is not None:
        check_click_v2('ok_button_01.jpg')
    if check_interupt('interupt02.jpg') is not None:
        check_click_v2('x_button.jpg')
    if check_interupt('x_button_01.jpg') is not None:
        check_click_v2('x_button_01.jpg')
    if check_interupt('x_button_02.jpg') is not None:
        check_click_v2('x_button_02.jpg')
    if check_interupt('x_button_03.jpg') is not None:
        check_click_v2('x_button_03.jpg')
    if check_interupt('go_inventory.jpg') is not None:
        check_click_v2('go_inventory.jpg')
    if check_interupt('dont_show_today.jpg') is not None:
        check_click_v2('dont_show_today.jpg')
    if check_interupt('no_today.jpg') is not None:
        check_click_v2('no_today.jpg')

        # manage_inventory()
        # if 에너지 없으면
        # gain_energy()

    time.sleep(random.uniform(4, 5))
# while True:
#     if pag.locateOnScreen(os.path.join(button_path2, filename), grayscale=True, confidence=.9):
#         time.sleep(random.uniform(wait_before_min, wait_before_max))
#         check_click(filename)
#         time.sleep(random.uniform(wait_after_min, wait_after_max))
#         if pag.locateOnScreen(os.path.join(button_path2, filename), grayscale=True, confidence=.9) is None:
#             break
#     else:
#         time.sleep(random.uniform(interval/2, interval))
