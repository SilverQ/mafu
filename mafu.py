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
import json
import pickle
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
game_log = load_log('game_log.json')
write_log(game_log)


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


def dim_to_epic(account=1):
    go_home()
    change_account_v2(account)  # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020
    time.sleep(random.uniform(2.71, 3.53))

    dim_to_do = game_log[str(account)]['dimension_mission'] - game_log[str(account)+'_do']['dimension_mission']
    if dim_to_do > 0:
        game_log[str(account)+'_do']['dimension_mission'] = dimension_mission(dim_to_do)
        print('Done : ', game_log[str(account)+'_do']['dimension_mission'])
        write_log(game_log)
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


def first_family_all_account():
    change_account(3)
    time.sleep(random.uniform(2.71, 3.53))
    first_family(10, 10, 3, 3, 3)
    time.sleep(random.uniform(2.71, 3.53))

    change_account(2)
    time.sleep(random.uniform(2.71, 3.53))
    first_family(10, 10, 3, 3, 3)
    time.sleep(random.uniform(2.71, 3.53))

    change_account(1)  # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020
    time.sleep(random.uniform(2.71, 3.53))
    first_family(10, 0, 3, 3, 3)
    time.sleep(random.uniform(2.71, 3.53))


def x_force_all_account():
    change_account(1)  # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020
    time.sleep(random.uniform(2.71, 3.53))
    x_force(10, 10, 3, 3, 3)       # 10, 10, 3, 3, 3
    time.sleep(random.uniform(2.71, 3.53))

    change_account(2)
    time.sleep(random.uniform(2.71, 3.53))
    x_force(10, 10, 3, 3, 0)         # 10, 10, 3, 3, 0,  도미노 할 수 있는지 확인
    time.sleep(random.uniform(2.71, 3.53))

    change_account(3)
    time.sleep(random.uniform(2.71, 3.53))
    x_force(10, 0, 3, 0, 0)             # 10, 0, 3, 0, 0
    time.sleep(random.uniform(2.71, 3.53))


def rise_xman_all_account():
    change_account(3)
    time.sleep(random.uniform(2.71, 3.53))
    rise_xman(10, 10, 10, 10, 2, 2)     # 10, 10, 10, 10, 2, 2
    time.sleep(random.uniform(2.71, 3.53))

    change_account(1)  # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020
    time.sleep(random.uniform(2.71, 3.53))
    rise_xman(10, 10, 10, 10, 2, 2)     # 10, 10, 10, 10, 2, 2
    time.sleep(random.uniform(2.71, 3.53))

    change_account(2)
    time.sleep(random.uniform(2.71, 3.53))
    rise_xman(10, 10, 10, 10, 2, 2)     #
    time.sleep(random.uniform(2.71, 3.53))


def sorcerer_supreme_all_account():
    # change_account(2)
    # time.sleep(random.uniform(2.71, 3.53))
    # sorcerer_supreme(3, 3)
    # time.sleep(random.uniform(2.71, 3.53))

    change_account(1)  # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020
    time.sleep(random.uniform(2.71, 3.53))
    sorcerer_supreme(1, 3)
    time.sleep(random.uniform(2.71, 3.53))

    change_account(3)
    time.sleep(random.uniform(2.71, 3.53))
    sorcerer_supreme(3, 3)
    time.sleep(random.uniform(2.71, 3.53))


def dimension_mission_all_account():
    change_account(1)  # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020
    time.sleep(random.uniform(2.71, 3.53))
    dimension_mission(10)
    time.sleep(random.uniform(2.71, 3.53))

    change_account(2)
    time.sleep(random.uniform(2.71, 3.53))
    dimension_mission(10)
    time.sleep(random.uniform(2.71, 3.53))

    change_account(3)
    time.sleep(random.uniform(2.71, 3.53))
    dimension_mission(10)
    time.sleep(random.uniform(2.71, 3.53))


def legendary_all_account():
    change_account(1)
    time.sleep(random.uniform(2.71, 3.53))
    legendary_battle(1)     # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020
    time.sleep(random.uniform(2.71, 3.53))

    change_account(2)
    time.sleep(random.uniform(2.71, 3.53))
    legendary_battle(2)  # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020
    time.sleep(random.uniform(2.71, 3.53))

    change_account(3)
    time.sleep(random.uniform(2.71, 3.53))
    legendary_battle(3)  # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020
    time.sleep(random.uniform(2.71, 3.53))


def do_log():
    def check_current_account():
        current_account = 0
        if check_exist('Account01.jpg'):
            current_account = 1
        elif check_exist('Account02.jpg'):
            current_account = 2
        elif check_exist('Account03.jpg'):
            current_account = 3
        return current_account

    # dimension_mission
    for i in range(1, 4):
        dim_to_do = game_log[str(i)]['dimension_mission'] - game_log[str(i)+'_do']['dimension_mission']
        if dim_to_do > 0:
            print('Playing account : ', str(i))
            change_account(i)   # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020
            print('dimension mission : ', dim_to_do)
            game_log[str(i)+'_do']['dimension_mission'] = dimension_mission(dim_to_do)
            print('Done : ', game_log[str(i)+'_do']['dimension_mission'])
            write_log(game_log)

    # first_family
    for i in range(1, 4):
        first_to_do = [game_log[str(i)]['first_family_01'] - game_log[str(i)+'_do']['first_family_01'],
                       game_log[str(i)]['first_family_02'] - game_log[str(i)+'_do']['first_family_02'],
                       game_log[str(i)]['first_family_03'] - game_log[str(i)+'_do']['first_family_03'],
                       game_log[str(i)]['first_family_04'] - game_log[str(i)+'_do']['first_family_04'],
                       game_log[str(i)]['first_family_05'] - game_log[str(i)+'_do']['first_family_05'],
                       game_log[str(i)]['first_family_06'] - game_log[str(i)+'_do']['first_family_06']
                       ]
        if sum(i for i in first_to_do) > 0:
            print('Playing account : ', str(i))
            change_account(i)   # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020
            print('first_family : ', first_to_do)
            log = first_family_v2(i, game_log)
            print('Done : ', [log[str(i) + '_do']['first_family_01'],
                              log[str(i) + '_do']['first_family_02'],
                              log[str(i) + '_do']['first_family_03'],
                              log[str(i) + '_do']['first_family_04'],
                              log[str(i) + '_do']['first_family_05'],
                              log[str(i) + '_do']['first_family_06'],
                              ])
            write_log(log)

    # x_force
    for i in range(1, 4):
        x_force_to_do = [game_log[str(i)]['x_force_01'] - game_log[str(i)+'_do']['x_force_01'],
                         game_log[str(i)]['x_force_02'] - game_log[str(i)+'_do']['x_force_02'],
                         game_log[str(i)]['x_force_03'] - game_log[str(i)+'_do']['x_force_03'],
                         game_log[str(i)]['x_force_04'] - game_log[str(i)+'_do']['x_force_04'],
                         game_log[str(i)]['x_force_05'] - game_log[str(i)+'_do']['x_force_05'],
                         game_log[str(i)]['x_force_06'] - game_log[str(i)+'_do']['x_force_06']
                         ]
        if sum(i for i in x_force_to_do) > 0:
            print('Playing account : ', str(i))
            change_account(i)   # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020
            print('x_force : ', x_force_to_do)
            log = x_force_v2(i, game_log)
            print('Done : ', [log[str(i) + '_do']['x_force_01'],
                              log[str(i) + '_do']['x_force_02'],
                              log[str(i) + '_do']['x_force_03'],
                              log[str(i) + '_do']['x_force_04'],
                              log[str(i) + '_do']['x_force_05'],
                              log[str(i) + '_do']['x_force_06'],
                              ])
            write_log(log)

    # rise_xman
    for i in range(1, 4):
        rise_xman_to_do = [game_log[str(i)]['rise_xman_01'] - game_log[str(i)+'_do']['rise_xman_01'],
                           game_log[str(i)]['rise_xman_02'] - game_log[str(i)+'_do']['rise_xman_02'],
                           game_log[str(i)]['rise_xman_03'] - game_log[str(i)+'_do']['rise_xman_03'],
                           game_log[str(i)]['rise_xman_04'] - game_log[str(i)+'_do']['rise_xman_04'],
                           game_log[str(i)]['rise_xman_05'] - game_log[str(i)+'_do']['rise_xman_05'],
                           game_log[str(i)]['rise_xman_06'] - game_log[str(i)+'_do']['rise_xman_06']
                           ]
        if sum(i for i in rise_xman_to_do) > 0:
            print('Playing account : ', str(i))
            change_account(i)   # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020
            print('x_man : ', rise_xman_to_do)
            log = rise_xman_v2(i, game_log)
            print('Done : ', [log[str(i) + '_do']['rise_xman_01'],
                              log[str(i) + '_do']['rise_xman_02'],
                              log[str(i) + '_do']['rise_xman_03'],
                              log[str(i) + '_do']['rise_xman_04'],
                              log[str(i) + '_do']['rise_xman_05'],
                              log[str(i) + '_do']['rise_xman_06'],
                              ])
            write_log(log)

    # sorcerer_supreme
    for i in range(1, 4):
        sorcerer_supreme_to_do = [game_log[str(i)]['sorcerer_supreme_01'] - game_log[str(i)+'_do']['sorcerer_supreme_01'],
                                  game_log[str(i)]['sorcerer_supreme_02'] - game_log[str(i)+'_do']['sorcerer_supreme_02']
                                  ]
        if sum(i for i in sorcerer_supreme_to_do) > 0:
            print('Playing account : ', str(i))
            change_account(i)   # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020
            print('sorcerer_supreme : ', sorcerer_supreme_to_do)
            log = sorcerer_supreme_v2(i, game_log)
            print('Done : ', [log[str(i) + '_do']['sorcerer_supreme_01'],
                              log[str(i) + '_do']['sorcerer_supreme_02']
                              ])
            write_log(log)


# do_log()

# ehdgml7602()        # 한또르(홍미)
# ehdgml7604()        # StarangeHee
# handhee2020()

# dimension_mission(10)
dim_to_epic(account=1)
# dim_to_epic(account=2)
# dim_to_epic(account=3)

# legendary_battle(2, 3)     # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020

# change_account_v2(1)   # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020
# change_account_v2(2)   # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020
# change_account_v2(3)   # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020

# dimension_mission_all_account()
# time.sleep(random.uniform(2.71, 3.53))
# first_family_all_account()
# time.sleep(random.uniform(2.71, 3.53))
# x_force_all_account()
# time.sleep(random.uniform(2.71, 3.53))
# rise_xman_all_account()
# time.sleep(random.uniform(2.71, 3.53))

# sorcerer_supreme_all_account()
# time.sleep(random.uniform(2.71, 3.53))
# dimension_mission_all_account()
# legendary_all_account()
# rise_xman(10, 10, 10, 10, 2, 2)     # 10, 10, 10, 10, 2, 2

# write_log(game_log, 'game_log.json')

# ehdgml76 계정 last 2020-04-05 12:08 AM
# ehdgml76 계정 last 2020-04-25 22:39, 근데 뭐 안주는데?
