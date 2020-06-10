from tqdm import tqdm
import pyautogui as pag
import time
import random
import os
import json
import numpy as np
from pytesseract import *
# import mss
import cv2
from pytesseract import *
from PIL import Image
from scipy.ndimage import rotate
import pickle
from skimage.metrics import structural_similarity
# import pyscreenshot as ImageGrab
from PIL import Image
import imutils
# from manage_interupt import pass_interupt
# import threading


button_path = 'buttons/'
button_path2 = 'buttons(960x540)/'
run_daemon = False


def check_interupt(filename):
    return pag.locateOnScreen(os.path.join(button_path2, filename), grayscale=True, confidence=.9)


def check_current_account():
    current_account = 0
    if check_exist('Account01.jpg'):
        current_account = 1
    elif check_exist('Account02.jpg'):
        current_account = 2
    elif check_exist('Account03.jpg'):
        current_account = 3
    return current_account


def pass_interupt(prev=True):
    while True:
        # prev = True
        if prev:
            pag.press('volumeup')
            prev = False
        else:
            pag.press('volumedown')
            prev = True
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
        if check_interupt('reload_button.jpg') is not None:
            time.sleep(10)
            if check_interupt('reload_button.jpg') is not None:
                check_click_v2('reload_button.jpg')

        # manage_inventory()
            # if 에너지 없으면
            # gain_energy()

        time.sleep(random.uniform(10, 20))


def dim_to_epic(account, game_log):
    if check_exist('launch_game.jpg'):
        print('game start')
        check_click_v2('launch_game.jpg', 0.01, 0.11)
        time.sleep(60)

    go_home()
    cur_account = check_current_account()
    if account is None or account == 0:
        account = cur_account
        print('Current account is ', cur_account)
        print("You didn't select account, starting with current account")
    elif account == cur_account:
        print('current account ', account, ' is identified.')
    else:
        change_account_v2(account)  # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020

    import threading
    time.sleep(random.uniform(2.71, 3.53))
    interupt_thread = threading.Thread(target=pass_interupt, name='pass_interupt', daemon=True)
    # interupt_thread.daemon = True
    interupt_thread.start()
    #
    # from utils import pass_interupt
    # pass_interupt()
    dim_to_do = game_log[str(account)]['dimension_mission'] - game_log[str(account)+'_do']['dimension_mission']
    if dim_to_do > 0:
        game_log[str(account)+'_do']['dimension_mission'] = dimension_mission(dim_to_do)
        print('Done : ', game_log[str(account)+'_do']['dimension_mission'])
        write_log(game_log)
        time.sleep(random.uniform(2.71, 3.53))

    galaxy(account, game_log)
    time.sleep(random.uniform(2.71, 3.53))

    first_family_v2(account, game_log)        # 10, 10, 3, 3, 3
    time.sleep(random.uniform(2.71, 3.53))

    x_force_v2(account, game_log)       # 10, 10, 3, 3, 3
    time.sleep(random.uniform(2.71, 3.53))

    rise_xman_v2(account, game_log)     # 10, 10, 10, 10, 2, 2
    time.sleep(random.uniform(2.71, 3.53))

    log = sorcerer_supreme_v2(account, game_log)
    time.sleep(random.uniform(2.71, 3.53))
    write_log(log)
    time.sleep(random.uniform(2.71, 3.53))

    # interupt_thread.join()//.


def check_exist(filename, gray=True, confidence=.9):
    if pag.locateOnScreen(os.path.join(button_path2, filename), grayscale=gray, confidence=confidence):
        return True
    else:
        return False


def check_click_v2(filename, click_min=0.21, click_max=0.53):
    button = pag.locateOnScreen(os.path.join(button_path2, filename), grayscale=True, confidence=.9)
    # Box(left=1416, top=562, width=50, height=41)
    # print(filename, button)
    if button is not None:
        try:
            mouse_click(button[0] + button[2] / 2 + random.uniform(0, button[2] * 0.3),
                        button[1] + button[3] / 2 + random.uniform(0, button[3] * 0.3),
                        click_min, click_max)
        finally:
            pass


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


def go_home():
    # go to home if not home
    time.sleep(random.uniform(0.2, 0.5))
    check_click_v2('go_home.jpg')
    time.sleep(random.uniform(0.5, 1.5))


def mouse_click(pos_x, pos_y, click_min=0.21, click_max=0.53):
    x, y = pag.position()
    pag.moveTo(pos_x, pos_y)
    # pag.doubleClick(pos_x, pos_y)
    pag.mouseDown()
    time.sleep(random.uniform(click_min, click_max))
    pag.mouseUp()
    pag.moveTo(x, y)


def check_click(filename):
    # 버튼의 이미지가 있다면, 화면에서 해당 버튼의 좌표를 산출할 수 있다.
    # https://pyautogui.readthedocs.io/en/latest/screenshot.html
    # pass_over_button = pag.locateOnScreen('button_pass_over.jpg')
    button = pag.locateOnScreen(os.path.join(button_path2, filename), grayscale=True, confidence=.9)
    # print(os.path.join(button_path2, filename), button)
    # https://automatetheboringstuff.com/chapter18/
    # locateOnScreen은 이미지가 완벽하게 매칭되어야 함 ㅠㅠ
    # Note that the image on the screen must match the provided image perfectly in order to be recognized.

    # Box(left=1416, top=562, width=50, height=41)
    if button is not None:
        try:
            # print(button[0])
            mouse_click(button[0] + button[2]/2 + random.uniform(0, button[2]*0.3),
                        button[1] + button[3]/2 + random.uniform(0, button[3]*0.3))
            # pag.moveTo(x=pass_over_button[0], y=pass_over_button[1])
        finally:
            pass


def check_click_in(filename, region):
    button = pag.locateOnScreen(os.path.join(button_path2, filename), region=region, grayscale=True, confidence=.99)
    # print(os.path.join(button_path2, filename), button)
    if button is not None:
        try:
            mouse_click(button[0] + button[2]/2 + random.uniform(0, button[2]*0.3),
                        button[1] + button[3]/2 + random.uniform(0, button[3]*0.3))
        finally:
            pass


def wait_click(filename, wait_before_min=0.3, wait_before_max=0.8, wait_after_min=0.1, wait_after_max=0.5, interval=1.0):
    print('waiting for ', filename)
    while True:
        button = pag.locateOnScreen(os.path.join(button_path2, filename),
                                    grayscale=True, confidence=.9)
        if button is not None:
            time.sleep(random.uniform(wait_before_min, wait_before_max))
            try:
                # print(os.path.join(button_path2, filename), button)
                mouse_click(button[0] + button[2] / 2 + random.uniform(0, button[2] * 0.3),
                            button[1] + button[3] / 2 + random.uniform(0, button[3] * 0.3))
                # time.sleep(random.uniform(0.2, 0.5))
                # mouse_click(button[0] + button[2] / 2 + random.uniform(0, button[2] * 0.3),
                #             button[1] + button[3] / 2 + random.uniform(0, button[3] * 0.3))
            finally:
                time.sleep(random.uniform(wait_after_min, wait_after_max))
                # pass
            # if button is None:
                break
        else:
            time.sleep(random.uniform(interval/2, interval))
    # while True:
    #     if pag.locateOnScreen(os.path.join(button_path2, filename), grayscale=True, confidence=.9):
    #         time.sleep(random.uniform(wait_before_min, wait_before_max))
    #         check_click(filename)
    #         time.sleep(random.uniform(wait_after_min, wait_after_max))
    #         if pag.locateOnScreen(os.path.join(button_path2, filename), grayscale=True, confidence=.9) is None:
    #             break
    #     else:
    #         time.sleep(random.uniform(interval/2, interval))


def change_account(account_num):
    file_to_check = 'Account0' + str(account_num) + '.jpg'
    file_to_change = 'setting_account_03_acc0' + str(account_num) + '.jpg'

    def enter_setting01():
        check_click('setting_button.jpg')
        time.sleep(random.uniform(0.91, 1.53))
        check_click('setting_account.jpg')
        time.sleep(random.uniform(0.91, 1.53))
        check_click('setting_account_01.jpg')
        time.sleep(random.uniform(0.91, 1.53))
        check_click('setting_account_02.jpg')
        time.sleep(random.uniform(4.91, 6.53))
        wait_click(file_to_change, 4.91, 6.5, 0.1, 0.5, 0.5)
        time.sleep(random.uniform(2.71, 3.53))
        check_click('setting_account_04.jpg')
        time.sleep(random.uniform(4.71, 5.53))
        check_click('ok_button.jpg')
        time.sleep(random.uniform(4.71, 5.53))
        check_click('ok_button.jpg')
        time.sleep(random.uniform(4.71, 5.53))
        check_click('x_button.jpg')
        time.sleep(random.uniform(1.71, 2.53))
        check_click('ok_button.jpg')
        time.sleep(random.uniform(9.71, 12.53))
        check_click('x_button.jpg')
        time.sleep(random.uniform(1.71, 2.53))
        check_click('ok_button.jpg')

    def enter_setting02():
        wait_click('setting_button.jpg', 0.9, 1.5, 0.1, 0.5, 0.5)
        wait_click('setting_account.jpg', 0.9, 1.5, 0.4, 0.9, 0.5)
        wait_click('setting_account_01.jpg', 0.9, 1.5, 0.1, 0.5, 0.5)
        wait_click('setting_account_02.jpg', 0.9, 1.5, 0.1, 0.5, 0.5)
        wait_click(file_to_change, 4.91, 6.5, 0.1, 0.5, 0.5)
        time.sleep(random.uniform(2.71, 3.53))
        check_click('setting_account_04.jpg')
        time.sleep(random.uniform(4.71, 5.53))
        check_click('ok_button.jpg')
        time.sleep(random.uniform(4.71, 5.53))
        check_click('ok_button.jpg')
        time.sleep(random.uniform(4.71, 5.53))
        check_click('x_button.jpg')
        time.sleep(random.uniform(1.71, 2.53))
        check_click('ok_button.jpg')
        time.sleep(random.uniform(9.71, 12.53))
        check_click('x_button.jpg')
        time.sleep(random.uniform(1.71, 2.53))
        check_click('ok_button.jpg')

    def enter_setting03():
        wait_click('setting_button.jpg', 0.9, 1.5, 2.1, 2.5, 0.5)

        if check_exist('setting_account.jpg'):
            print('Select Account Tab')
            wait_click('setting_account.jpg', 0.1, 0.5, 0.4, 0.9, 0.5)
        elif check_exist('setting_account2.jpg'):
            print('Current Tab is Account')

        time.sleep(random.uniform(2.71, 3.53))

        if check_exist('setting_account_02.jpg'):
            print('Account is not connected to Google Play')
            wait_click('setting_account_02.jpg', 0.9, 1.5, 4.1, 5.5, 0.5)
        elif check_exist('setting_account_01.jpg'):
            print('Account is connected to Google Play')
            wait_click('setting_account_01.jpg', 0.9, 1.5, 0.1, 0.5, 0.5)
            wait_click('setting_account_02.jpg', 0.9, 1.5, 4.1, 5.5, 0.5)

        time.sleep(random.uniform(4.71, 5.53))
        if check_exist(file_to_change):
            wait_click(file_to_change, 4.91, 6.5, 0.1, 0.5, 0.5)
        elif check_exist('setting_account_done.jpg'):
            wait_click('ok_button.jpg', 4.91, 6.5, 0.1, 0.5, 0.5)
            wait_click('ok_button.jpg', 4.91, 6.5, 0.1, 0.5, 0.5)
            return True

        wait_click('setting_account_04.jpg', 4.91, 6.5, 0.1, 0.5, 0.5)
        wait_click('ok_button.jpg', 4.91, 6.5, 4.71, 5.53, 0.5)
        wait_click('ok_button.jpg')
        time.sleep(random.uniform(4.71, 5.53))
        check_click('x_button.jpg')
        time.sleep(random.uniform(1.71, 2.53))
        check_click('ok_button.jpg')
        time.sleep(random.uniform(9.71, 12.53))
        check_click('x_button.jpg')
        time.sleep(random.uniform(1.71, 2.53))
        check_click('ok_button.jpg')
        return False

    def check_current_account(account_num):
        current_account = 0
        if check_exist('Account01.jpg'):
            current_account = 1
        elif check_exist('Account02.jpg'):
            current_account = 2
        elif check_exist('Account03.jpg'):
            current_account = 3
        return True if account_num == current_account else False

    if pag.locateOnScreen(os.path.join(button_path2, 'setting_button.jpg'), grayscale=True, confidence=.9):
        print('setting button is identified')
    else:
        print('setting button is not identified, go to home')
        go_home()

    # print('current account is no need to change' if check_current_account(account_num) else 'change account start')
    if check_current_account(account_num):
        print('current account is no need to change')
    else:
        print('change account start')
        # enter_setting02()
        while True:
            change_acc = enter_setting03()
            if change_acc is False:
                break
        pass
    # print(file_to_check, file_to_change)

    # enter_setting01()

    # if account_num == 1:
    #     if pag.locateOnScreen(os.path.join(button_path2, 'Account01.jpg'), grayscale=True, confidence=.9):
    #         print('current account is ', account_num, ', there is no need to change')
    #         pass
    #     else:
    #         # enter_setting01()
    #         enter_setting02()     # 비교용... 뭐가 나을까
    #         # check_click('setting_account_03_acc01.jpg')
    #         wait_click('setting_account_03_acc01.jpg', 4.91, 6.5, 0.1, 0.5, 0.5)
    # elif account_num == 2:
    #     if pag.locateOnScreen(os.path.join(button_path2, 'Account02.jpg'), grayscale=True, confidence=.9):
    #         print('current account is ', account_num, ', there is no need to change')
    #         pass
    #     else:
    #         enter_setting01()
    #         check_click('setting_account_03_acc02.jpg')
    # elif account_num == 3:
    #     if pag.locateOnScreen(os.path.join(button_path2, 'Account03.jpg'), grayscale=True, confidence=.9):
    #         print('current account is ', account_num, ', there is no need to change')
    #         pass
    #     else:
    #         time.sleep(random.uniform(0.91, 1.53))
    #         check_click('setting_button.jpg')
    #         time.sleep(random.uniform(0.91, 1.53))
    #         check_click('setting_account.jpg')
    #         time.sleep(random.uniform(0.91, 1.53))
    #         check_click('setting_account_01.jpg')
    #         time.sleep(random.uniform(0.91, 1.53))
    #         check_click('setting_account_02.jpg')
    #         time.sleep(random.uniform(4.91, 6.53))
    #         check_click('setting_account_03_acc03.jpg')
    #
    # time.sleep(random.uniform(2.71, 3.53))
    # check_click('setting_account_04.jpg')
    # time.sleep(random.uniform(4.71, 5.53))
    # check_click('ok_button.jpg')
    # time.sleep(random.uniform(4.71, 5.53))
    # check_click('ok_button.jpg')
    # time.sleep(random.uniform(4.71, 5.53))
    # check_click('x_button.jpg')
    # time.sleep(random.uniform(1.71, 2.53))
    # check_click('ok_button.jpg')
    # time.sleep(random.uniform(9.71, 12.53))
    # check_click('x_button.jpg')
    # time.sleep(random.uniform(1.71, 2.53))
    # check_click('ok_button.jpg')


def change_account_v2(account_num):

    def enter_setting01(account_num):
        file_to_change = 'setting_account_03_acc0' + str(account_num) + '.jpg'
        check_click('setting_button.jpg')
        time.sleep(random.uniform(0.91, 1.53))
        check_click('setting_account.jpg')
        time.sleep(random.uniform(0.91, 1.53))
        check_click('setting_account_01.jpg')
        time.sleep(random.uniform(0.91, 1.53))
        check_click('setting_account_02.jpg')
        time.sleep(random.uniform(4.91, 6.53))
        wait_click(file_to_change, 4.91, 6.5, 0.1, 0.5, 0.5)
        time.sleep(random.uniform(2.71, 3.53))
        check_click('setting_account_04.jpg')
        time.sleep(random.uniform(4.71, 5.53))
        check_click('ok_button.jpg')
        time.sleep(random.uniform(4.71, 5.53))
        check_click('ok_button.jpg')
        time.sleep(random.uniform(4.71, 5.53))
        check_click('x_button.jpg')
        time.sleep(random.uniform(1.71, 2.53))
        check_click('ok_button.jpg')
        time.sleep(random.uniform(9.71, 12.53))
        check_click('x_button.jpg')
        time.sleep(random.uniform(1.71, 2.53))
        check_click('ok_button.jpg')

    def enter_setting02(account_num):
        file_to_change = 'setting_account_03_acc0' + str(account_num) + '.jpg'
        wait_click('setting_button.jpg', 0.9, 1.5, 0.1, 0.5, 0.5)
        wait_click('setting_account.jpg', 0.9, 1.5, 0.4, 0.9, 0.5)
        wait_click('setting_account_01.jpg', 1.9, 2.5, 0.1, 0.5, 0.5)
        wait_click('setting_account_02.jpg', 1.9, 2.5, 0.1, 0.5, 0.5)
        wait_click(file_to_change, 4.91, 6.5, 0.1, 0.5, 0.5)
        wait_click('setting_account_04.jpg', 2.71, 3.53, 0.1, 0.5, 0.5)
        wait_click('ok_button.jpg', 4.71, 5.53, 0.1, 0.5, 0.5)
        wait_click('ok_button.jpg', 4.71, 5.53, 0.1, 0.5, 0.5)
        time.sleep(random.uniform(13.71, 16.53))
        if pag.locateOnScreen('buttons(960x540)/x_button_01.jpg'):
            wait_click('x_button_01.jpg', 0.71, 0.93, 0.1, 0.5, 0.5)
            wait_click('ok_button.jpg', 1.71, 2.53, 0.1, 0.5, 0.5)
        time.sleep(random.uniform(2.71, 3.53))
        if pag.locateOnScreen('buttons(960x540)/x_button.jpg'):
            wait_click('x_button.jpg', 0.71, 0.93, 0.1, 0.5, 0.5)
            wait_click('ok_button.jpg', 1.71, 2.53, 0.1, 0.5, 0.5)
        time.sleep(random.uniform(9.71, 12.53))
        if pag.locateOnScreen('buttons(960x540)/x_button.jpg'):
            wait_click('x_button.jpg', 0.71, 0.93, 0.1, 0.5, 0.5)
            wait_click('ok_button.jpg', 1.71, 2.53, 0.1, 0.5, 0.5)

    def check_current_account(account_num):
        current_account = 0
        if check_exist('Account01.jpg'):
            current_account = 1
        elif check_exist('Account02.jpg'):
            current_account = 2
        elif check_exist('Account03.jpg'):
            current_account = 3
        return True if account_num == current_account else False

    if pag.locateOnScreen(os.path.join(button_path2, 'setting_button.jpg'), grayscale=True, confidence=.9):
        print('setting button is identified')
    else:
        print('setting button is not identified, go to home')
        go_home()

    # print('current account is no need to change' if check_current_account(account_num) else 'change account start')
    if check_current_account(account_num):
        print('current account is no need to change')
    else:
        print('change account start')
        enter_setting02(account_num)
        # while True:
        # if enter_setting02(account_num):
        #     break


def iter_battle(cnt):
    # 전투가 시작됐는데 리로드를 대기하지 않고 계속 전투시작 버튼을 기다리는걸 해결하기 위해
    # 만들어봤는데, iter_battle_v2로 만들었다가 기존의 iter_battle랑 이름을 바꿔치기함
    for i in tqdm(range(cnt)):
        pag.press('volumedown')
        time.sleep(random.uniform(1.3, 2.1))
        wait_click('start_battle.jpg', 1.9, 2.6, 2.7, 3.3, 3)
        print('Now, waiting for the end of the ', i+1, "'th battle")
        while True:
            if pag.locateOnScreen(os.path.join(button_path2, 'reload_button.jpg'), grayscale=True, confidence=.9):
                time.sleep(random.uniform(2, 3))
                if pag.locateOnScreen(os.path.join(button_path2, 'ok_button.jpg'), grayscale=True, confidence=.9):
                    check_click('ok_button.jpg')
                    wait_click('reload_button.jpg', 0.9, 1.4, 0.9, 1.3, 2)
                    break
                else:
                    wait_click('reload_button.jpg', 0.9, 1.4, 0.9, 1.3, 2)
                    break
            else:
                time.sleep(random.uniform(2, 3))
    time.sleep(random.uniform(2.5, 3))
    print('end iteration')
    return cnt


def iter_battle_v2(cnt):
    # time.sleep(random.uniform(1, 1.5))
    for i in tqdm(range(cnt)):
        # pag.keyDown('alt')
        # pag.press('tab')
        # pag.keyUp('alt')
        pag.press('volumedown')
        time.sleep(random.uniform(0.4, 0.9))
        # pag.press('q')
        # print('iteration : ', i+1, ' / ', cnt)
        # 1'st 시도
        # sleep_click(1618, 977, 300, 70, 2.01, 4.23)        # start_battle
        # while True:
        #     if pag.locateOnScreen('buttons/reload_button.jpg', grayscale=True, confidence=.9):
        #         time.sleep(random.uniform(3, 4))
        #         check_click('reload_button.jpg')
        #         time.sleep(random.uniform(2, 3.5))
        #         break
        #     else:
        #         time.sleep(random.uniform(2, 3))
        # 2'nd 시도
        wait_click('start_battle.jpg', 0.9, 1.7, 1.5, 2, 3)
        # if i < cnt:
        #     wait_click('reload_button.jpg', 0.1, 0.5, 0.5, 1, 1)
        # else:
        #     # time.sleep(random.uniform(3.71, 4.53))
        #     wait_click('ok_button.jpg', 0.1, 0.5, 0.5, 1, 1)
        #     wait_click('reload_button.jpg', 0.1, 0.5, 0.5, 1, 1)
        # 3'rd 시도
        while True:
            if pag.locateOnScreen(os.path.join(button_path2, 'reload_button.jpg'), grayscale=True, confidence=.9):
                time.sleep(random.uniform(2, 3))
                if pag.locateOnScreen(os.path.join(button_path2, 'ok_button.jpg'), grayscale=True, confidence=.9):
                    check_click('ok_button.jpg')
                    wait_click('reload_button.jpg', 0.9, 1.4, 0.5, 1, 2)
                    break
                else:
                    wait_click('reload_button.jpg', 0.9, 1.4, 0.5, 1, 2)
                    break
            else:
                time.sleep(random.uniform(2, 3))
        # while True:
        #     if pag.locateOnScreen(os.path.join(button_path2, 'reload_button.jpg'), grayscale=True, confidence=.9):
        #         time.sleep(random.uniform(2, 3))
        #         if pag.locateOnScreen(os.path.join(button_path2, 'ok_button.jpg'), grayscale=True, confidence=.9):
        #             wait_click('ok_button.jpg', 0.1, 0.5, 0.5, 1, 2)
        #             wait_click('reload_button.jpg', 0.4, 0.8, 0.5, 1, 2)
        #             break
        #         else:
        #             wait_click('reload_button.jpg', 0.4, 0.8, 0.5, 1, 2)
        #             break
        #     else:
        #         time.sleep(random.uniform(2, 3))
    time.sleep(random.uniform(2.5, 3))
    print('end iteration')
    return cnt


# 직접 좌표 지정 사용 중이므로 고쳐야 함
def legendary_battle(account, cnt=5):
    print('Starting Legendary Battle')

    go_home()    # go to home if not home
    wait_click('enter_battle.jpg', 0.1, 0.5, 0, 0, 1)
    wait_click('mission_02.jpg', 0.1, 0.5, 0, 0, 1)     # 도전
    wait_click('legendary_battle.jpg', 0.1, 0.5, 0.5, 1, 1)     # 레전더리 배틀
    if account == 1:
        check_click('legendary_01_03.jpg')              # 캡틴 마블
        wait_click('legendary_02.jpg', 0.1, 0.5, 1, 2, 1)   # 노멀
        for i in range(cnt):
            check_click_in('enter_button.jpg',
                           pag.locateOnScreen(os.path.join(button_path2, 'legendary_01_03_01.jpg')))
            wait_click('legendary_03.jpg', 0.1, 0.5, 1, 2, 1)   # 전투 시작
            wait_click('pass_over.jpg', 0.1, 0.5, 0, 0, 1)      # 건너 뛰기
            wait_click('reload_button.jpg', 0.1, 0.5, 0, 0, 1)
    elif account == 3 or account == 2:
        drag_from = pag.locateOnScreen(os.path.join('buttons(960x540)/', 'legendary_01_04.jpg'),
                                       grayscale=True, confidence=.9)
        drag_to = pag.locateOnScreen(os.path.join('buttons(960x540)/', 'legendary_01_01.jpg'),
                                     grayscale=True, confidence=.9)
        pag.moveTo(random.uniform(drag_from[0], drag_from[0]+drag_from[2]),
                   random.uniform(drag_from[1], drag_from[1]+drag_from[3]))
        pag.dragTo(random.uniform(drag_to[0], drag_to[0]+drag_to[2]), random.uniform(drag_to[1], drag_to[1]+drag_to[3]),
                   random.uniform(0.7, 1.2), button='left')
        pag.moveTo(random.uniform(drag_from[0], drag_from[0]+drag_from[2]),
                   random.uniform(drag_from[1], drag_from[1]+drag_from[3]))
        pag.dragTo(random.uniform(drag_to[0], drag_to[0]+drag_to[2]), random.uniform(drag_to[1], drag_to[1]+drag_to[3]),
                   random.uniform(0.7, 1.2), button='left')
        time.sleep(random.uniform(1.9, 2.3))
        wait_click('legendary_01_06.jpg', 0.4, 0.8, 1, 2, 1)              # 캡틴 마블
        time.sleep(random.uniform(1.71, 2.53))
        wait_click('legendary_02.jpg', 0.1, 0.5, 1, 2, 1)   # 노멀
        for i in tqdm(range(cnt)):
            check_click_in('enter_button.jpg',
                           pag.locateOnScreen(os.path.join(button_path2, 'legendary_01_06_01.jpg')))
            wait_click('legendary_03.jpg', 0.1, 0.5, 1, 2, 1)   # 전투 시작
            wait_click('pass_over.jpg', 0.1, 0.5, 0, 0, 1)      # 건너 뛰기
            wait_click('reload_button.jpg', 0.1, 0.5, 1, 2, 1)


def dimension_mission(num):
    print('Starting Dimension Mission')

    go_home()    # go to home if not home
    # sleep_click(1645, 988, 3, 25, 0.31, 4.23)    # start_battle
    wait_click('enter_battle.jpg', 0.1, 0.5, 0, 0, 1)
    wait_click('dimension_mission.jpg', 0.1, 0.5, 0, 0, 1)
    # sleep_click(729, 659, 930-729, 983-329, 2.01, 3.23)    # select_mission
    # x, 515, y: 329 ~ x, 930, y: 983
    # wait_click('dimension_mission.jpg', 0.1, 0.5, 0, 0, 1)    # 이미지가 바뀌네 ㅠㅠ

    time.sleep(random.uniform(1.8, 2.3))
    check_click_v2('x_button.jpg')  # 첫 실행에서 가끔 이벤트 안내 페이지가 뜸

    time.sleep(random.uniform(1, 2))
    check_click_v2('ok_button.jpg')

    for i in tqdm(range(num)):
        wait_click('ready_battle.jpg', 0.1, 0.5, 0.5, 1, 1)
        wait_click('start_battle.jpg', 2.1, 3.5, 0.5, 1, 1)
        # check_click_v2('start_battle.jpg')
        # time.sleep(random.uniform(2.01, 3.23))
        # check_click('not_use_button.jpg')        # "not_use_button.jpg"
        wait_click('not_use_button.jpg', 0.1, 0.5, 0, 0, 1)

        # while True:
        #     if pag.locateOnScreen('buttons/reload_button.jpg', grayscale=True, confidence=.9):
        #         time.sleep(random.uniform(3.01, 4.23))
        #         check_click('reload_button.jpg')
        #         time.sleep(random.uniform(2.01, 3.23))
        #         break
        #     else:
        #         time.sleep(random.uniform(2, 3))
        if i < num:
            wait_click('reload_button.jpg', 1.1, 1.5, 0, 0, 1.7)

    print('end dimension_mission')
    time.sleep(random.uniform(2.71, 3.53))

    return num


def get_pos(file):
    return pag.locateOnScreen(os.path.join('buttons(960x540)/', file), grayscale=True, confidence=.9)


def detect_energy():
    energy_pos1 = pag.locateOnScreen(os.path.join(button_path2, 'energy_icon.jpg'), grayscale=True, confidence=.9)
    energy_pos2 = pag.locateOnScreen(os.path.join(button_path2, 'energy_icon2.jpg'), grayscale=True, confidence=.9)
    # print(energy_pos1, energy_pos2)   # Box(left=289, top=339, width=27, height=31)
    adj = 8
    im = pag.screenshot(region=(energy_pos1[0]+energy_pos1[2]+adj, energy_pos2[1],
                                (energy_pos2[0]-energy_pos1[0]-energy_pos1[2])*0.49-adj, energy_pos2[3]))
    im = np.array(im)
    # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # cv2.imwrite(os.path.join(button_path2, 'energy.png'), im)
    # im = cv2.imread(os.path.join(button_path2, 'energy.png'))
    text = pytesseract.image_to_string(im, config='--psm 10 tessedit_char_whitelist=/0123456789')
    # cv2.imshow('output', im)
    print(text.replace(',', ''))
    # print(int(text))
    try:
        energy = int(text.replace(',', ''))
    except:
        energy = 20
    finally:
        pass
    return energy


def galaxy(i, game_log):
    galaxy_to_do = [game_log[str(i)]['galaxy_01'] - game_log[str(i) + '_do']['galaxy_01'],
                    game_log[str(i)]['galaxy_02'] - game_log[str(i) + '_do']['galaxy_02'],
                    game_log[str(i)]['galaxy_03'] - game_log[str(i) + '_do']['galaxy_03'],
                    game_log[str(i)]['galaxy_04'] - game_log[str(i) + '_do']['galaxy_04'],
                    game_log[str(i)]['galaxy_05'] - game_log[str(i) + '_do']['galaxy_05']
                    ]
    if sum(i for i in galaxy_to_do) > 0:
        print('Starting galaxy: ', galaxy_to_do)
        go_home()

        wait_click('enter_battle.jpg')
        wait_click('epic_quest.jpg')
        wait_click('galaxy.jpg')

        def galaxy_iter(but1, but2, but3, cnt):
            wait_click(but1)  # 사이좋은 형제
            wait_click(but2)  # 사이좋은 형제
            if but3 is not None:
                check_click_in('battle.jpg', pag.locateOnScreen(os.path.join(button_path2, but3)))
                time.sleep(random.uniform(1, 1.5))
            else:
                pass
            iter_battle(cnt)
            time.sleep(random.uniform(2.71, 3.53))
            check_click('back_button.jpg')
            time.sleep(random.uniform(0.71, 1.53))
            check_click('back_button.jpg')
            time.sleep(random.uniform(0.71, 1.53))
            return cnt

        if galaxy_to_do[0] > 0 and detect_energy() > 30:
            game_log[str(i) + '_do']['galaxy_01'] += galaxy_iter('galaxy_01.jpg',
                                                                 'galaxy_01_01.jpg',
                                                                 'galaxy_01_01_04.jpg',
                                                                 galaxy_to_do[0])
            write_log(game_log)
        if galaxy_to_do[1] > 0 and detect_energy() > 30:
            game_log[str(i) + '_do']['galaxy_02'] += galaxy_iter('galaxy_01.jpg',
                                                                 'galaxy_01_02.jpg',
                                                                 'galaxy_01_02_04.jpg',
                                                                 galaxy_to_do[1])
            write_log(game_log)
        if galaxy_to_do[2] > 0 and detect_energy() > 30:
            game_log[str(i) + '_do']['galaxy_03'] += galaxy_iter('galaxy_02.jpg',
                                                                 'galaxy_02_01.jpg',
                                                                 None,
                                                                 galaxy_to_do[2])
            write_log(game_log)
        time.sleep(random.uniform(2.71, 3.53))
        print('end galaxy')
        return game_log
    else:
        pass


def first_family_v2(i, game_log):
    first_to_do = [game_log[str(i)]['first_family_01'] - game_log[str(i) + '_do']['first_family_01'],
                   game_log[str(i)]['first_family_02'] - game_log[str(i) + '_do']['first_family_02'],
                   game_log[str(i)]['first_family_03'] - game_log[str(i) + '_do']['first_family_03'],
                   game_log[str(i)]['first_family_04'] - game_log[str(i) + '_do']['first_family_04'],
                   game_log[str(i)]['first_family_05'] - game_log[str(i) + '_do']['first_family_05'],
                   game_log[str(i)]['first_family_06'] - game_log[str(i) + '_do']['first_family_06']
                   ]
    if sum(i for i in first_to_do) > 0:
        print('Starting First Family: ', first_to_do)
        go_home()

        wait_click('enter_battle.jpg')
        wait_click('epic_quest.jpg')
        wait_click('first_family.jpg')

        def first_falimy_iter(but1, but2, but3, cnt):
            wait_click(but1)  # 사이좋은 형제
            wait_click(but2)  # 사이좋은 형제
            if but3 is not None:
                check_click_in('battle.jpg', pag.locateOnScreen(os.path.join(button_path2, but3)))
                time.sleep(random.uniform(1, 1.5))
            else:
                pass
            iter_battle(cnt)
            time.sleep(random.uniform(2.71, 3.53))
            check_click('back_button.jpg')
            time.sleep(random.uniform(0.71, 1.53))
            check_click('back_button.jpg')
            time.sleep(random.uniform(0.71, 1.53))
            return cnt

        if first_to_do[0] > 0 and detect_energy() > 30:
            game_log[str(i) + '_do']['first_family_01'] = first_falimy_iter('first_family_01.jpg',
                                                                            'first_family_01_01.jpg',
                                                                            'first_family_01_01_04.jpg',
                                                                            first_to_do[0])
            write_log(game_log)
        if first_to_do[1] > 0 and detect_energy() > 30:
            game_log[str(i) + '_do']['first_family_02'] = first_falimy_iter('first_family_01.jpg',
                                                                            'first_family_01_02.jpg',
                                                                            'first_family_01_02_04.jpg',
                                                                            first_to_do[1])
            write_log(game_log)
        if first_to_do[2] > 0 and detect_energy() > 30:
            wait_click('first_family_02.jpg')  # 뉴 페이스
            wait_click('first_family_02_01.jpg')  # 인휴먼 공주
            game_log[str(i) + '_do']['first_family_03'] = iter_battle(first_to_do[2])
            time.sleep(random.uniform(2.71, 3.53))
            check_click('back_button.jpg')
            time.sleep(random.uniform(0.71, 1.53))
            check_click('back_button.jpg')
            time.sleep(random.uniform(0.71, 1.53))
            write_log(game_log)

        if first_to_do[3] > 0 and detect_energy() > 30:
            wait_click('first_family_02.jpg')  # 뉴 페이스
            wait_click('first_family_02_02.jpg')  # 사나운 초록색
            game_log[str(i) + '_do']['first_family_04'] = iter_battle(first_to_do[3])
            time.sleep(random.uniform(2.71, 3.53))
            check_click('back_button.jpg')
            time.sleep(random.uniform(0.71, 1.53))
            check_click('back_button.jpg')
            time.sleep(random.uniform(0.71, 1.53))
            write_log(game_log)
        if first_to_do[4] > 0 and detect_energy() > 12:
            wait_click('first_family_03.jpg')  # 뒤틀린 세계
            wait_click('first_family_03_01.jpg')  # 라트베리아
            game_log[str(i) + '_do']['first_family_05'] = iter_battle(first_to_do[4])
            time.sleep(random.uniform(0.71, 1.53))
            check_click('back_button.jpg')
            time.sleep(random.uniform(0.71, 1.53))
            check_click('back_button.jpg')
            time.sleep(random.uniform(0.71, 1.53))
            write_log(game_log)
        if first_to_do[5] > 0 and detect_energy() > 12:
            wait_click('first_family_03.jpg')  # 뒤틀린 세계
            wait_click('first_family_03_02.jpg')  # 파멸의 그늘
            game_log[str(i) + '_do']['first_family_06'] = iter_battle(first_to_do[5])
            time.sleep(random.uniform(0.71, 1.53))
            check_click('back_button.jpg')
            time.sleep(random.uniform(0.71, 1.53))
            check_click('back_button.jpg')
            time.sleep(random.uniform(0.71, 1.53))
            write_log(game_log)
        time.sleep(random.uniform(2.71, 3.53))
        print('end first_family')
        return game_log
    else:
        pass


def hero_quest(i, game_log):
    print('Starting Hero Quest')
    go_home()

    wait_click('enter_battle.jpg')
    wait_click('hero_quest.jpg')

    time.sleep(random.uniform(2.71, 3.53))
    check_click('cancel.jpg')
    time.sleep(random.uniform(2.71, 3.53))
    check_click('ok_button.jpg')
    time.sleep(random.uniform(2.71, 3.53))
    check_click('goto_mission.jpg')


def x_force_v2(i, game_log):
    x_force_to_do = [game_log[str(i)]['x_force_01'] - game_log[str(i) + '_do']['x_force_01'],
                     game_log[str(i)]['x_force_02'] - game_log[str(i) + '_do']['x_force_02'],
                     game_log[str(i)]['x_force_03'] - game_log[str(i) + '_do']['x_force_03'],
                     game_log[str(i)]['x_force_04'] - game_log[str(i) + '_do']['x_force_04'],
                     game_log[str(i)]['x_force_05'] - game_log[str(i) + '_do']['x_force_05'],
                     game_log[str(i)]['x_force_06'] - game_log[str(i) + '_do']['x_force_06']]

    if sum(i for i in x_force_to_do) > 0:
        print('Starting X Force')
        go_home()

        wait_click('enter_battle.jpg')
        wait_click('epic_quest.jpg')

        wait_click('x_force.jpg')

        def x_force_iter(but1, but2, but3, cnt):
            wait_click(but1)  # 엉망인 친구들
            wait_click(but2)  # 이런 세상에

            if but3 is not None:
                check_click_in('battle.jpg', pag.locateOnScreen(os.path.join(button_path2, but3)))
            else:
                pass
            iter_battle(cnt)
            time.sleep(random.uniform(2.71, 3.53))

            check_click('back_button.jpg')
            time.sleep(random.uniform(0.71, 1.53))
            check_click('back_button.jpg')
            time.sleep(random.uniform(0.71, 1.53))
            return cnt

        if x_force_to_do[0] > 0 and detect_energy() > 30:
            game_log[str(i) + '_do']['x_force_01'] = x_force_iter('x_force_01.jpg', 'x_force_01_01.jpg', 'x_force_01_01_04.jpg', x_force_to_do[0])
            write_log(game_log)
        if x_force_to_do[1] > 0 and detect_energy() > 30:
            game_log[str(i) + '_do']['x_force_02'] = x_force_iter('x_force_01.jpg', 'x_force_01_02.jpg', 'x_force_01_02_04.jpg', x_force_to_do[1])
            write_log(game_log)
        if x_force_to_do[2] > 0 and detect_energy() > 12:
            game_log[str(i) + '_do']['x_force_03'] = x_force_iter('x_force_02.jpg', 'x_force_02_01.jpg', None, x_force_to_do[2])
            write_log(game_log)
        if x_force_to_do[3] > 0 and detect_energy() > 12:
            game_log[str(i) + '_do']['x_force_04'] = x_force_iter('x_force_02.jpg', 'x_force_02_02.jpg', None, x_force_to_do[3])
            write_log(game_log)
        if x_force_to_do[4] > 0 and detect_energy() > 12:    # 케이블 자르기
            game_log[str(i) + '_do']['x_force_05'] = x_force_iter('x_force_03.jpg', 'x_force_03_01.jpg', None, x_force_to_do[4])
            write_log(game_log)
        if x_force_to_do[5] > 0 and detect_energy() > 12:    # 케이블 자르기
            game_log[str(i) + '_do']['x_force_06'] = x_force_iter('x_force_03.jpg', 'x_force_03_02.jpg', None, x_force_to_do[5])
            write_log(game_log)

        time.sleep(random.uniform(2.71, 3.53))
        print('end x_force')
    return game_log


def rise_xman_v2(i, game_log):
    rise_xman_to_do = [game_log[str(i)]['rise_xman_01'] - game_log[str(i) + '_do']['rise_xman_01'],
                       game_log[str(i)]['rise_xman_02'] - game_log[str(i) + '_do']['rise_xman_02'],
                       game_log[str(i)]['rise_xman_03'] - game_log[str(i) + '_do']['rise_xman_03'],
                       game_log[str(i)]['rise_xman_04'] - game_log[str(i) + '_do']['rise_xman_04'],
                       game_log[str(i)]['rise_xman_05'] - game_log[str(i) + '_do']['rise_xman_05'],
                       game_log[str(i)]['rise_xman_06'] - game_log[str(i) + '_do']['rise_xman_06'],
                       game_log[str(i)]['rise_xman_07'] - game_log[str(i) + '_do']['rise_xman_07']]
    if sum(i for i in rise_xman_to_do) > 0:
        print('Starting Rise X man')
        go_home()

        wait_click('enter_battle.jpg')
        wait_click('epic_quest.jpg', 1, 2, 1, 2)

        # drag_from = pag.locateOnScreen(os.path.join('buttons(960x540)/', 'x_force.jpg'),
        #                                grayscale=True, confidence=.9)
        # drag_to = pag.locateOnScreen(os.path.join('buttons(960x540)/', 'galaxy.jpg'),
        #                              grayscale=True, confidence=.9)
        drag_from = get_pos('x_force.jpg')
        drag_to = get_pos('galaxy.jpg')

        pag.moveTo(random.uniform(drag_from[0], drag_from[0]+drag_from[2]*0.5),
                   random.uniform(drag_from[1], drag_from[1]+drag_from[3]))
        pag.dragTo(random.uniform(drag_to[0], drag_to[0]+drag_to[2]*0.5),
                   random.uniform(drag_to[1], drag_to[1]+drag_to[3]),
                   random.uniform(0.7, 1.2), button='left')

        time.sleep(random.uniform(2.01, 4.53))
        wait_click('rise_xman.jpg')    # select_mission

        def rise_xman_iter(but1, but2, but3, cnt):
            wait_click(but1)  # chasing
            time.sleep(random.uniform(1.01, 1.53))
            if but2 is not None:
                wait_click(but2)
            if but3 is not None:
                check_click_in('battle.jpg', pag.locateOnScreen(os.path.join(button_path2, but3)))
            iter_battle(cnt)
            time.sleep(random.uniform(2.71, 3.53))
            check_click('back_button.jpg')
            time.sleep(random.uniform(1.71, 2.53))
            check_click('back_button.jpg')
            return cnt

        if rise_xman_to_do[0] > 0 and detect_energy() > 30:
            game_log[str(i) + '_do']['rise_xman_01'] = rise_xman_iter('rise_xman_01.jpg', 'rise_xman_01_01.jpg',
                                                                      'rise_xman_01_01_04.jpg', rise_xman_to_do[0])
            write_log(game_log)
        if rise_xman_to_do[1] > 0 and detect_energy() > 30:
            game_log[str(i) + '_do']['rise_xman_02'] = rise_xman_iter('rise_xman_01.jpg', 'rise_xman_01_02.jpg',
                                                                      'rise_xman_01_02_04.jpg', rise_xman_to_do[1])
            write_log(game_log)
        if rise_xman_to_do[2] > 0 and detect_energy() > 30:
            game_log[str(i) + '_do']['rise_xman_03'] = rise_xman_iter('rise_xman_01.jpg', 'rise_xman_01_03.jpg',
                                                                      'rise_xman_01_03_04.jpg', rise_xman_to_do[2])
            write_log(game_log)
        if rise_xman_to_do[3] > 0 and detect_energy() > 30:
            game_log[str(i) + '_do']['rise_xman_04'] = rise_xman_iter('rise_xman_01.jpg', 'rise_xman_01_04.jpg',
                                                                      None, rise_xman_to_do[3])
            write_log(game_log)
        if rise_xman_to_do[4] > 0 and detect_energy() > 8:
            game_log[str(i) + '_do']['rise_xman_04'] = rise_xman_iter('rise_xman_02.jpg', 'rise_xman_02_01.jpg',
                                                                      None, rise_xman_to_do[4])
            write_log(game_log)
            # wait_click('rise_xman_02.jpg')
            # wait_click('rise_xman_02_01.jpg')
            # iter_battle(rise_xman_to_do[4])
            # time.sleep(random.uniform(2.71, 3.53))
            # check_click('ok_button.jpg')
            # time.sleep(random.uniform(1.71, 2.53))
            # check_click('reload_button.jpg')
            # time.sleep(random.uniform(1.71, 2.53))
            # check_click('back_button.jpg')
            # time.sleep(random.uniform(1.71, 2.53))
            # check_click('back_button.jpg')
            # time.sleep(random.uniform(1.71, 2.53))
            # game_log[str(i) + '_do']['rise_xman_05'] = rise_xman_to_do[4]
            # write_log(game_log)
        if rise_xman_to_do[5] > 0 and detect_energy() > 8:
            game_log[str(i) + '_do']['rise_xman_04'] = rise_xman_iter('rise_xman_02.jpg', 'rise_xman_02_02.jpg',
                                                                      None, rise_xman_to_do[5])
            write_log(game_log)
            # wait_click('rise_xman_02.jpg')
            # wait_click('rise_xman_02_02.jpg')
            # iter_battle(rise_xman_to_do[5])
            # time.sleep(random.uniform(2.71, 3.53))
            # check_click('ok_button.jpg')
            # time.sleep(random.uniform(1.71, 2.53))
            # check_click('reload_button.jpg')
            # time.sleep(random.uniform(1.71, 2.53))
            # check_click('back_button.jpg')
            # time.sleep(random.uniform(1.71, 2.53))
            # check_click('back_button.jpg')
            # time.sleep(random.uniform(1.71, 2.53))
            # game_log[str(i) + '_do']['rise_xman_06'] = rise_xman_to_do[5]
            # write_log(game_log)
        time.sleep(random.uniform(2.71, 3.53))
        if rise_xman_to_do[6] > 0 and detect_energy() > 8:
            game_log[str(i) + '_do']['rise_xman_04'] = rise_xman_iter('rise_xman_03.jpg', None,
                                                                      None, rise_xman_to_do[5])
            write_log(game_log)
            # wait_click('rise_xman_03.jpg')
            # iter_battle(rise_xman_to_do[6])
            # time.sleep(random.uniform(2.71, 3.53))
            # check_click('ok_button.jpg')
            # time.sleep(random.uniform(1.71, 2.53))
            # check_click('reload_button.jpg')
            # time.sleep(random.uniform(1.71, 2.53))
            # game_log[str(i) + '_do']['rise_xman_07'] = rise_xman_to_do[6]
            # write_log(game_log)
        time.sleep(random.uniform(2.71, 3.53))
        print('end rise_xman')
    return game_log


def sorcerer_supreme_v2(i, game_log):
    sorcerer_to_do = [game_log[str(i)]['sorcerer_supreme_01'] - game_log[str(i) + '_do']['sorcerer_supreme_01'],
                      game_log[str(i)]['sorcerer_supreme_02'] - game_log[str(i) + '_do']['sorcerer_supreme_02'],
                      game_log[str(i)]['sorcerer_supreme_03'] - game_log[str(i) + '_do']['sorcerer_supreme_03'],
                      game_log[str(i)]['sorcerer_supreme_04'] - game_log[str(i) + '_do']['sorcerer_supreme_04'],
                      game_log[str(i)]['sorcerer_supreme_05'] - game_log[str(i) + '_do']['sorcerer_supreme_05'],
                      game_log[str(i)]['sorcerer_supreme_06'] - game_log[str(i) + '_do']['sorcerer_supreme_06']
                      ]
    if sum(i for i in sorcerer_to_do) > 0:
        print('Starting Sorcerer Supreme: ', sorcerer_to_do)
        go_home()

        wait_click('enter_battle.jpg')
        wait_click('epic_quest.jpg', 1, 2, 1, 2)

        # drag_from = pag.locateOnScreen(os.path.join('buttons(960x540)/', 'x_force.jpg'),
        #                                grayscale=True, confidence=.9)
        # drag_to = pag.locateOnScreen(os.path.join('buttons(960x540)/', 'galaxy.jpg'),
        #                              grayscale=True, confidence=.9)
        drag_from = get_pos('x_force.jpg')
        drag_to = get_pos('galaxy.jpg')

        pag.moveTo(random.uniform(drag_from[0], drag_from[0]+drag_from[2]*0.5),
                   random.uniform(drag_from[1], drag_from[1]+drag_from[3]))
        pag.dragTo(random.uniform(drag_to[0], drag_to[0]+drag_to[2]*0.5),
                   random.uniform(drag_to[1], drag_to[1]+drag_to[3]),
                   random.uniform(0.7, 1.2), button='left')

        time.sleep(random.uniform(2, 4.5))
        wait_click('sorcerer_supreme.jpg')

        def Sorcerer_iter(but1, but2, but3, cnt):
            wait_click(but1)
            wait_click(but2)
            if but3 is not None:
                drag_from2 = pag.locateOnScreen(os.path.join('buttons(960x540)/', 'sorcerer_supreme_01_01_04.jpg'),
                                                grayscale=True, confidence=.99)
                drag_to2 = pag.locateOnScreen(os.path.join('buttons(960x540)/', 'sorcerer_supreme_01_01_01.jpg'),
                                              grayscale=True, confidence=.99)
                pag.moveTo(random.uniform(drag_from2[0], drag_from2[0] + drag_from2[2] * 0.5),
                           random.uniform(drag_from2[1], drag_from2[1] + drag_from2[3]))
                pag.dragTo(random.uniform(drag_to2[0], drag_to2[0] + drag_to2[2] * 0.5),
                           random.uniform(drag_to2[1], drag_to2[1] + drag_to2[3]),
                           random.uniform(0.7, 1.2), button='left')
                time.sleep(random.uniform(2, 3.5))
                check_click_in('battle.jpg', pag.locateOnScreen(os.path.join(button_path2, but3)))
                time.sleep(random.uniform(1, 1.5))
            else:
                pass
            iter_battle(cnt)
            time.sleep(random.uniform(2.71, 3.53))
            check_click('back_button.jpg')
            time.sleep(random.uniform(0.71, 1.53))
            check_click('back_button.jpg')
            time.sleep(random.uniform(0.71, 1.53))
            return cnt

        if sorcerer_to_do[0] > 0:
            game_log[str(i) + '_do']['sorcerer_supreme_01'] += Sorcerer_iter('sorcerer_supreme_01.jpg',
                                                                             'sorcerer_supreme_01_01.jpg',
                                                                             'sorcerer_supreme_01_01_06.jpg',
                                                                             sorcerer_to_do[0])
            write_log(game_log)

        if sorcerer_to_do[1] > 0:
            game_log[str(i) + '_do']['sorcerer_supreme_02'] += Sorcerer_iter('sorcerer_supreme_01.jpg',
                                                                             'sorcerer_supreme_01_02.jpg',
                                                                             'sorcerer_supreme_01_02_06.jpg',
                                                                             sorcerer_to_do[1])
            write_log(game_log)

        if sorcerer_to_do[2] > 0:
            game_log[str(i) + '_do']['sorcerer_supreme_03'] += Sorcerer_iter('sorcerer_supreme_01.jpg',
                                                                             'sorcerer_supreme_01_03.jpg',
                                                                             'sorcerer_supreme_01_03_06.jpg',
                                                                             sorcerer_to_do[2])
            write_log(game_log)

        if sorcerer_to_do[3] > 0:
            game_log[str(i) + '_do']['sorcerer_supreme_04'] += Sorcerer_iter('sorcerer_supreme_01.jpg',
                                                                             'sorcerer_supreme_01_04.jpg',
                                                                             'sorcerer_supreme_01_04_06.jpg',
                                                                             sorcerer_to_do[3])
            write_log(game_log)

        if sorcerer_to_do[4] > 0:
            game_log[str(i) + '_do']['sorcerer_supreme_05'] += Sorcerer_iter('sorcerer_supreme_01.jpg',
                                                                             'sorcerer_supreme_01_05.jpg',
                                                                             'sorcerer_supreme_01_05_06.jpg',
                                                                             sorcerer_to_do[4])
            write_log(game_log)

        if sorcerer_to_do[5] > 0:
            game_log[str(i) + '_do']['sorcerer_supreme_06'] += Sorcerer_iter('sorcerer_supreme_01.jpg',
                                                                             'sorcerer_supreme_01_06.jpg',
                                                                             'sorcerer_supreme_01_06_06.jpg',
                                                                             sorcerer_to_do[5])
            write_log(game_log)

    # cnt1 = game_log[str(i)]['sorcerer_supreme_01'] - game_log[str(i) + '_do']['sorcerer_supreme_01']
    # cnt2 = game_log[str(i)]['sorcerer_supreme_02'] - game_log[str(i) + '_do']['sorcerer_supreme_02']
    # print('Starting Sorcerer Supreme')
    # go_home()
    #
    # wait_click('enter_battle.jpg')
    # wait_click('epic_quest.jpg')
    # wait_click('sorcerer_supreme.jpg')
    #
    # if cnt1 > 0:
    #     wait_click('sorcerer_supreme_01.jpg')  # 회상 임무
    #     time.sleep(random.uniform(0.71, 1.53))
    #     wait_click('sorcerer_supreme_01_04.jpg')  # 어둠의 힘
    #     time.sleep(random.uniform(0.71, 1.53))
    #     drag_from = pag.locateOnScreen(os.path.join('buttons(960x540)/', 'sorcerer_supreme_01_04_04.jpg'),
    #                                    grayscale=True, confidence=.99)
    #     drag_to = pag.locateOnScreen(os.path.join('buttons(960x540)/', 'sorcerer_supreme_01_04_01.jpg'),
    #                                  grayscale=True, confidence=.99)
    #     pag.moveTo(random.uniform(drag_from[0], drag_from[0]+drag_from[2]*0.5),
    #                random.uniform(drag_from[1], drag_from[1]+drag_from[3]))
    #     pag.dragTo(random.uniform(drag_to[0], drag_to[0]+drag_to[2]*0.5),
    #                random.uniform(drag_to[1], drag_to[1]+drag_to[3]),
    #                random.uniform(0.7, 1.2), button='left')
    #     time.sleep(random.uniform(1.71, 2.53))
    #     check_click_in('battle.jpg',
    #                    pag.locateOnScreen(os.path.join(button_path2, 'sorcerer_supreme_01_04_06.jpg')))
    #     iter_battle(cnt1)
    #     time.sleep(random.uniform(3.71, 4.53))
    #     check_click('back_button.jpg')
    #     time.sleep(random.uniform(0.71, 1.53))
    #     check_click('back_button.jpg')
    #     time.sleep(random.uniform(0.71, 1.53))
    # if cnt2 > 0:
    #     check_click_v2('sorcerer_supreme_02.jpg')
    #     time.sleep(random.uniform(1.71, 2.53))
    #     if pag.locateOnScreen(os.path.join(button_path2, 'sorcerer_supreme_02_02.jpg'), grayscale=True, confidence=.9):
    #         check_click_v2('sorcerer_supreme_02_02.jpg')  # 회상 임무
    #     else:
    #         check_click_v2('sorcerer_supreme_02_01.jpg')  # 회상 임무
    #     time.sleep(random.uniform(3.71, 4.53))
    #     iter_battle(cnt2)
    #     time.sleep(random.uniform(3.71, 4.53))
    # time.sleep(random.uniform(2.71, 3.53))
    # print('end sorcerer_supreme')
    return game_log


def gain_energy():
    pass


def write_log(data, file='game_log.json'):
    with open(file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file)
    print('log writing finished')


def load_log(file='game_log.json'):
    last_modified = os.path.getmtime(file) if os.path.exists(file) else -1
    print('last modified date is ', time.localtime(last_modified).tm_yday,
          'today is ', time.localtime(time.time()).tm_yday)
    print(time.time(), time.localtime(time.time()).tm_mday)
    if time.localtime(time.time()).tm_yday == time.localtime(last_modified).tm_yday:
        # game_log = pickle.load(open(file, 'rb'))
        # game_log = json.load(file)
        log_file = open(file)
        game_log = json.load(log_file)
        print('Game Log is loaded successfully')
    else:
        print('Game Log is initiated')
        game_log = {'max': {'dimension_mission': 10,
                            'galaxy_01': 10, 'galaxy_02': 10, 'galaxy_03': 10, 'galaxy_04': 0, 'galaxy_05': 0,
                            'first_family_01': 10, 'first_family_02': 10, 'first_family_03': 10, 'first_family_04': 10,
                            'first_family_05': 3, 'first_family_06': 3,
                            'x_force_01': 10, 'x_force_02': 10, 'x_force_03': 3, 'x_force_04': 3,
                            'x_force_05': 3, 'x_force_06': 3,
                            'rise_xman_01': 10, 'rise_xman_02': 10, 'rise_xman_03': 10, 'rise_xman_04': 10,
                            'rise_xman_05': 2, 'rise_xman_06': 2, 'rise_xman_07': 2,
                            "sorcerer_supreme_01": 10, "sorcerer_supreme_02": 10, "sorcerer_supreme_03": 10, "sorcerer_supreme_04": 10,
                            "sorcerer_supreme_05": 10, "sorcerer_supreme_06": 10
                            },
                    '1': {'dimension_mission': 10,
                          'galaxy_01': 10, 'galaxy_02': 10, 'galaxy_03': 10, 'galaxy_04': 0, 'galaxy_05': 0,
                          'first_family_01': 10, 'first_family_02': 10, 'first_family_03': 10, 'first_family_04': 10,
                          'first_family_05': 3, 'first_family_06': 3,
                          'x_force_01': 10, 'x_force_02': 10, 'x_force_03': 3, 'x_force_04': 3,
                          'x_force_05': 3, 'x_force_06': 3,
                          'rise_xman_01': 10, 'rise_xman_02': 10, 'rise_xman_03': 10, 'rise_xman_04': 10,
                          'rise_xman_05': 2, 'rise_xman_06': 2, 'rise_xman_07': 2,
                          "sorcerer_supreme_01": 10, "sorcerer_supreme_02": 10, "sorcerer_supreme_03": 10,
                          "sorcerer_supreme_04": 10,
                          "sorcerer_supreme_05": 10, "sorcerer_supreme_06": 10
                          },
                    '2': {'dimension_mission': 10,
                          'galaxy_01': 10, 'galaxy_02': 10, 'galaxy_03': 10, 'galaxy_04': 0, 'galaxy_05': 0,
                          'first_family_01': 10, 'first_family_02': 10, 'first_family_03': 10, 'first_family_04': 10,
                          'first_family_05': 3, 'first_family_06': 0,
                          'x_force_01': 10, 'x_force_02': 10, 'x_force_03': 3, 'x_force_04': 3,
                          'x_force_05': 3, 'x_force_06': 0,
                          'rise_xman_01': 10, 'rise_xman_02': 10, 'rise_xman_03': 10, 'rise_xman_04': 10,
                          'rise_xman_05': 2, 'rise_xman_06': 2, 'rise_xman_07': 2,
                          "sorcerer_supreme_01": 10, "sorcerer_supreme_02": 10, "sorcerer_supreme_03": 10,
                          "sorcerer_supreme_04": 10,
                          "sorcerer_supreme_05": 10, "sorcerer_supreme_06": 10
                          },
                    '3': {'dimension_mission': 10,
                          'galaxy_01': 0, 'galaxy_02': 0, 'galaxy_03': 0, 'galaxy_04': 0, 'galaxy_05': 0,
                          'first_family_01': 10, 'first_family_02': 10, 'first_family_03': 10, 'first_family_04': 10,
                          'first_family_05': 3, 'first_family_06': 3,
                          'x_force_01': 10, 'x_force_02': 10, 'x_force_03': 3, 'x_force_04': 3,
                          'x_force_05': 3, 'x_force_06': 0,
                          'rise_xman_01': 10, 'rise_xman_02': 10, 'rise_xman_03': 10, 'rise_xman_04': 10,
                          'rise_xman_05': 2, 'rise_xman_06': 2, 'rise_xman_07': 0,
                          "sorcerer_supreme_01": 10, "sorcerer_supreme_02": 10, "sorcerer_supreme_03": 10,
                          "sorcerer_supreme_04": 10,
                          "sorcerer_supreme_05": 10, "sorcerer_supreme_06": 3
                          },
                    '1_do': {'dimension_mission': 0,
                             'galaxy_01': 0, 'galaxy_02': 0, 'galaxy_03': 0, 'galaxy_04': 0, 'galaxy_05': 0,
                             'first_family_01': 0, 'first_family_02': 0, 'first_family_03': 0, 'first_family_04': 0,
                             'first_family_05': 0, 'first_family_06': 0,
                             'x_force_01': 0, 'x_force_02': 0, 'x_force_03': 0, 'x_force_04': 0,
                             'x_force_05': 0, 'x_force_06': 0,
                             'rise_xman_01': 0, 'rise_xman_02': 0, 'rise_xman_03': 0, 'rise_xman_04': 0,
                             'rise_xman_05': 0, 'rise_xman_06': 0, 'rise_xman_07': 0,
                             "sorcerer_supreme_01": 0, "sorcerer_supreme_02": 0, "sorcerer_supreme_03": 0,
                             "sorcerer_supreme_04": 0,
                             "sorcerer_supreme_05": 0, "sorcerer_supreme_06": 0
                             },
                    '2_do': {'dimension_mission': 0,
                             'galaxy_01': 0, 'galaxy_02': 0, 'galaxy_03': 0, 'galaxy_04': 0, 'galaxy_05': 0,
                             'first_family_01': 0, 'first_family_02': 0, 'first_family_03': 0, 'first_family_04': 0,
                             'first_family_05': 0, 'first_family_06': 0,
                             'x_force_01': 0, 'x_force_02': 0, 'x_force_03': 0, 'x_force_04': 0,
                             'x_force_05': 0, 'x_force_06': 0,
                             'rise_xman_01': 0, 'rise_xman_02': 0, 'rise_xman_03': 0, 'rise_xman_04': 0,
                             'rise_xman_05': 0, 'rise_xman_06': 0, 'rise_xman_07': 0,
                             "sorcerer_supreme_01": 0, "sorcerer_supreme_02": 0, "sorcerer_supreme_03": 0,
                             "sorcerer_supreme_04": 0,
                             "sorcerer_supreme_05": 0, "sorcerer_supreme_06": 0
                             },
                    '3_do': {'dimension_mission': 0,
                             'galaxy_01': 0, 'galaxy_02': 0, 'galaxy_03': 0, 'galaxy_04': 0, 'galaxy_05': 0,
                             'first_family_01': 0, 'first_family_02': 0, 'first_family_03': 0, 'first_family_04': 0,
                             'first_family_05': 0, 'first_family_06': 0,
                             'x_force_01': 0, 'x_force_02': 0, 'x_force_03': 0, 'x_force_04': 0,
                             'x_force_05': 0, 'x_force_06': 0,
                             'rise_xman_01': 0, 'rise_xman_02': 0, 'rise_xman_03': 0, 'rise_xman_04': 0,
                             'rise_xman_05': 0, 'rise_xman_06': 0, 'rise_xman_07': 0,
                             "sorcerer_supreme_01": 0, "sorcerer_supreme_02": 0, "sorcerer_supreme_03": 0,
                             "sorcerer_supreme_04": 0,
                             "sorcerer_supreme_05": 0, "sorcerer_supreme_06": 0
                             },
                    }
        write_log(game_log)
    # print('game_log: ', game_log)
    return game_log
