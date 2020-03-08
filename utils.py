import pyautogui as pag
import cv2
from pytesseract import *
from PIL import Image
from scipy.ndimage import rotate
import time
import random
import os
import tqdm


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
    # Box(left=1416, top=562, width=50, height=41)
    print(filename, button)
    if button is not None:
        try:
            mouse_click(button[0] + button[2] / 2 + random.uniform(0, button[2] * 0.3),
                        button[1] + button[3] / 2 + random.uniform(0, button[3] * 0.3))
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


def change_account(account_num):
    go_home()

    # check_current_account
    if account_num == 1:
        if pag.locateOnScreen('buttons/Account01.jpg', grayscale=True, confidence=.9):
            pass
        else:
            check_click('setting_button.jpg')
            time.sleep(random.uniform(0.71, 1.53))
            check_click('setting_account.jpg')
            time.sleep(random.uniform(0.71, 1.53))
            check_click('setting_account_01.jpg')
            time.sleep(random.uniform(0.71, 1.53))
            check_click('setting_account_02.jpg')
            time.sleep(random.uniform(4.71, 6.53))
            check_click('setting_account_03_acc01.jpg')
            time.sleep(random.uniform(2.71, 3.53))
            check_click('setting_account_04.jpg')
            # time.sleep(random.uniform(4.71, 5.53))
            # check_click('ok_button.jpg')
            # time.sleep(random.uniform(2.71, 3.53))
            # check_click('ok_button.jpg')
            # time.sleep(random.uniform(4.71, 5.53))
            # check_click('x_button.jpg')
            # time.sleep(random.uniform(2.71, 3.53))
            # check_click('ok_button.jpg')
            # time.sleep(random.uniform(2.71, 3.53))
    elif account_num == 2:
        if pag.locateOnScreen('buttons/Account02.jpg', grayscale=True, confidence=.9):
            pass
        else:
            check_click('setting_button.jpg')
            time.sleep(random.uniform(0.71, 1.53))
            check_click('setting_account.jpg')
            time.sleep(random.uniform(0.71, 1.53))
            check_click('setting_account_01.jpg')
            time.sleep(random.uniform(0.71, 1.53))
            check_click('setting_account_02.jpg')
            time.sleep(random.uniform(4.71, 6.53))
            check_click('setting_account_03_acc02.jpg')
            time.sleep(random.uniform(2.71, 3.53))
            check_click('setting_account_04.jpg')
            # time.sleep(random.uniform(4.71, 5.53))
            # check_click('ok_button.jpg')
            # time.sleep(random.uniform(2.71, 3.53))
            # check_click('ok_button.jpg')
            # time.sleep(random.uniform(4.71, 5.53))
            # check_click('x_button.jpg')
            # time.sleep(random.uniform(2.71, 3.53))
            # check_click('ok_button.jpg')
            # time.sleep(random.uniform(2.71, 3.53))
    elif account_num == 3:
        if pag.locateOnScreen('buttons/Account03.jpg', grayscale=True, confidence=.9):
            pass
        else:
            check_click('setting_button.jpg')
            time.sleep(random.uniform(0.71, 1.53))
            check_click('setting_account.jpg')
            time.sleep(random.uniform(0.71, 1.53))
            check_click('setting_account_01.jpg')
            time.sleep(random.uniform(0.71, 1.53))
            check_click('setting_account_02.jpg')
            time.sleep(random.uniform(4.71, 6.53))
            check_click('setting_account_03_acc03.jpg')
            time.sleep(random.uniform(2.71, 3.53))
            check_click('setting_account_04.jpg')
            # time.sleep(random.uniform(4.71, 5.53))
            # check_click('ok_button.jpg')
            # time.sleep(random.uniform(2.71, 3.53))
            # check_click('ok_button.jpg')
            # time.sleep(random.uniform(4.71, 5.53))
            # check_click('x_button.jpg')
            # time.sleep(random.uniform(2.71, 3.53))
            # check_click('ok_button.jpg')
            # time.sleep(random.uniform(2.71, 3.53))

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
    # while True:
    #     if pag.locateOnScreen('buttons/setting_account_05.jpg', grayscale=True, confidence=.9):
    #         check_click('x_button.jpg')
    #         break
    #     else:
    #         time.sleep(random.uniform(2.71, 3.53))

    # time.sleep(random.uniform(4.71, 5.53))
    # if pag.locateOnScreen('buttons/setting_account_06.jpg', grayscale=True, confidence=.9):
    #     check_click('ok_button.jpg')
    # time.sleep(random.uniform(2.71, 3.53))
    # if pag.locateOnScreen('buttons/setting_account_07.jpg', grayscale=True, confidence=.9):
    #     check_click('x_button.jpg')
    #     time.sleep(random.uniform(1.71, 2.53))
    #     check_click('ok_button.jpg')
    #
    # time.sleep(random.uniform(1.71, 2.53))
    #
    # def clan():
    #     go_home()
    #     check_click('main_menu.jpg')
    #     wait_click('clan_01.jpg')
    #     wait_click('clan_02.jpg')
    #     check_click('ok_button.jpg')
    #     wait_click('clan_03.jpg')
    #     check_click('plus_button.jpg')
    #     check_click('clan_04.jpg')
    #
    # # clan()


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
    # print(os.path.join('buttons/', filename), button)
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


def wait_click(filename, wait_before_min=0.3, wait_before_max=0.8, wait_after_min=0.1, wait_after_max=0.5, interval=1.0):
    while True:
        button = pag.locateOnScreen(os.path.join('buttons/', filename), grayscale=True, confidence=.9)
        if button is not None:
            time.sleep(random.uniform(wait_before_min, wait_before_max))
            try:
                print(os.path.join('buttons/', filename), button)
                mouse_click(button[0] + button[2] / 2 + random.uniform(0, button[2] * 0.3),
                            button[1] + button[3] / 2 + random.uniform(0, button[3] * 0.3))
            finally:
                pass
            time.sleep(random.uniform(wait_after_min, wait_after_max))
            if pag.locateOnScreen(os.path.join('buttons/', filename), grayscale=True, confidence=.9) is None:
                break
        else:
            time.sleep(random.uniform(interval/2, interval))
    # while True:
    #     if pag.locateOnScreen(os.path.join('buttons/', filename), grayscale=True, confidence=.9):
    #         time.sleep(random.uniform(wait_before_min, wait_before_max))
    #         check_click(filename)
    #         time.sleep(random.uniform(wait_after_min, wait_after_max))
    #         if pag.locateOnScreen(os.path.join('buttons/', filename), grayscale=True, confidence=.9) is None:
    #             break
    #     else:
    #         time.sleep(random.uniform(interval/2, interval))


def iter_battle(cnt):
    for i in range(cnt):
        print('iteration : ', i+1, ' / ', cnt)
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
        wait_click('start_battle.jpg', 0.1, 0.5, 1.5, 2, 3)
        # if i < cnt:
        #     wait_click('reload_button.jpg', 0.1, 0.5, 0.5, 1, 1)
        # else:
        #     # time.sleep(random.uniform(3.71, 4.53))
        #     wait_click('ok_button.jpg', 0.1, 0.5, 0.5, 1, 1)
        #     wait_click('reload_button.jpg', 0.1, 0.5, 0.5, 1, 1)
        # 3'rd 시도
        while True:
            if pag.locateOnScreen('buttons/reload_button.jpg', grayscale=True, confidence=.9):
                time.sleep(random.uniform(2, 3))
                if pag.locateOnScreen('buttons/ok_button.jpg', grayscale=True, confidence=.9):
                    wait_click('ok_button.jpg', 0.1, 0.5, 0.5, 1, 2)
                    wait_click('reload_button.jpg', 0.4, 0.8, 0.5, 1, 2)
                    break
                else:
                    wait_click('reload_button.jpg', 0.4, 0.8, 0.5, 1, 2)
                    break
            else:
                time.sleep(random.uniform(2, 3))
    time.sleep(random.uniform(2.5, 3))
    print('end iteration')


def legendary_battle(account):
    go_home()    # go to home if not home
    wait_click('enter_battle.jpg', 0.1, 0.5, 0, 0, 1)
    wait_click('mission_02.jpg', 0.1, 0.5, 0, 0, 1)     # 도전
    sleep_click_v2(68, 329, 464, 916, 2.01, 3.23)       # 레전더리 배틀
    time.sleep(random.uniform(2.71, 3.53))
    if account == 1:
        check_click('legendary_01_03.jpg')              # 캡틴 마블
        wait_click('legendary_02.jpg', 0.1, 0.5, 0, 0, 1)   # 노멀
        for i in range(5):
            sleep_click_v2(135, 778, 491, 851, 3.01, 4.23)  # 입장
            wait_click('legendary_03.jpg', 0.1, 0.5, 1, 2, 1)   # 전투 시작
            wait_click('pass_over.jpg', 0.1, 0.5, 0, 0, 1)      # 건너 뛰기
            wait_click('reload_button.jpg', 0.1, 0.5, 0, 0, 1)
        # x, 135, y: 778
        # x, 491, y: 851
    elif account == 3 or account ==2:
        pag.moveTo(random.uniform(234, 245), random.uniform(800, 889))
        pag.dragTo(random.uniform(234, 245), random.uniform(294, 330),
                   random.uniform(0.7, 1.2), button='left')
# x, 234, y: 889
# x, 245, y: 294
        check_click('legendary_01_06.jpg')              # 캡틴 마블
        wait_click('legendary_02.jpg', 0.1, 0.5, 0, 0, 1)   # 노멀
        for i in tqdm(range(5)):
            sleep_click_v2(135, 778, 491, 851, 3.01, 4.23)  # 입장
            wait_click('legendary_03.jpg', 0.1, 0.5, 1, 2, 1)   # 전투 시작
            wait_click('pass_over.jpg', 0.1, 0.5, 0, 0, 1)      # 건너 뛰기
            wait_click('reload_button.jpg', 0.1, 0.5, 0, 0, 1)


def dimension_mission(num):
    go_home()    # go to home if not home
    # sleep_click(1645, 988, 3, 25, 0.31, 4.23)    # start_battle
    wait_click('enter_battle.jpg', 0.1, 0.5, 0, 0, 1)
    sleep_click(729, 659, 930-729, 983-329, 2.01, 3.23)    # select_mission
    # x, 515, y: 329 ~ x, 930, y: 983
    # wait_click('dimension_mission.jpg', 0.1, 0.5, 0, 0, 1)    # 이미지가 바뀌네 ㅠㅠ

    time.sleep(random.uniform(1.2, 2.3))
    check_click_v2('x_button.jpg')  # 첫 실행에서 가끔 이벤트 안내 페이지가 뜸

    time.sleep(random.uniform(1, 2))
    check_click_v2('ok_button.jpg')

    for i in range(num):
        print('iteration : ', i+1, ' / ', num)
        # sleep_click(930, 986, 250, 70, 3.01, 4.23)        # ready_battle
        wait_click('ready_battle.jpg', 0.1, 0.5, 0.5, 1, 1)
        # sleep_click(1618, 977, 300, 70, 2.01, 3.23)        # start_battle
        check_click_v2('start_battle.jpg')

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


def sorcerer_supreme(cnt1=3, cnt2=3):
    go_home()

    wait_click('enter_battle.jpg')
    wait_click('epic_quest.jpg')
    # time.sleep(random.uniform(0.71, 1.53))
    wait_click('sorcerer_supreme.jpg')
    # time.sleep(random.uniform(0.71, 1.53))

    if True:
        wait_click('sorcerer_supreme_01.jpg')  # 회상 임무
        time.sleep(random.uniform(0.71, 1.53))
        # wait_click('sorcerer_supreme_01_01.jpg')  # 수도원으로 가는 길
        # wait_click('sorcerer_supreme_01_02.jpg')  # 의문의 습격자
        # wait_click('sorcerer_supreme_01_03.jpg')  # 위기의 수도원
        wait_click('sorcerer_supreme_01_04.jpg')  # 어둠의 힘
        time.sleep(random.uniform(0.71, 1.53))

        # x, 665, y: 245
        # x, 1251, y: 783
        pag.moveTo(random.uniform(851, 1024), random.uniform(673, 752))
        pag.dragTo(random.uniform(851, 1024), random.uniform(302, 346),
                   random.uniform(0.4, 1.2), button='left')
        # x, 1272, y: 692
        # x, 1462, y: 751
        sleep_click_v2(1272, 692, 1462, 751, 1.01, 2.23)  # 어둠의 힘 #6

        iter_battle(cnt1)
        time.sleep(random.uniform(3.71, 4.53))

        check_click('back_button.jpg')
        time.sleep(random.uniform(0.71, 1.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(0.71, 1.53))

    if pag.locateOnScreen('buttons/sorcerer_supreme_02.jpg', grayscale=True, confidence=.9):
        check_click_v2('sorcerer_supreme_02.jpg')
        time.sleep(random.uniform(1.71, 2.53))
        if pag.locateOnScreen('buttons/sorcerer_supreme_02_02_locked.jpg', grayscale=True, confidence=.9):
            check_click_v2('sorcerer_supreme_02_01.jpg')  # 회상 임무
        elif pag.locateOnScreen('buttons/sorcerer_supreme_02_02.jpg', grayscale=True, confidence=.9):
            check_click_v2('sorcerer_supreme_02_02.jpg')  # 회상 임무
        time.sleep(random.uniform(3.71, 4.53))
        iter_battle(cnt2)
        time.sleep(random.uniform(3.71, 4.53))
    else:
        pass
    time.sleep(random.uniform(2.71, 3.53))
    print('end sorcerer_supreme')


def first_family(cnt1=10, cnt2=10, cnt3=3, cnt4=3, cnt5=3):
    go_home()

    wait_click('enter_battle.jpg')
    wait_click('epic_quest.jpg')
    wait_click('first_family.jpg')

    def first_falimy_iter(but1, but2, cnt):
        wait_click(but1)  # 사이좋은 형제
        wait_click(but2)  # 사이좋은 형제
        sleep_click_v2(1274, 730, 1454, 784, 1.01, 2.23)  # 때려 부술 시간_4
        iter_battle(cnt)
        time.sleep(random.uniform(2.71, 3.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(0.71, 1.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(0.71, 1.53))

    if cnt1 > 0:
        first_falimy_iter('first_family_01.jpg', 'first_family_01_01.jpg', cnt1)
        # wait_click('first_family_01.jpg')  # 사이좋은 형제
        # wait_click('first_family_01_01.jpg')  # 사이좋은 형제
        # sleep_click_v2(1274, 730, 1454, 784, 1.01, 2.23)  # 때려 부술 시간_4
        # iter_battle(cnt1)
        #
        # time.sleep(random.uniform(2.71, 3.53))
        # check_click('back_button.jpg')
        # time.sleep(random.uniform(0.71, 1.53))
        # check_click('back_button.jpg')
        # time.sleep(random.uniform(0.71, 1.53))

    if cnt2 > 0:
        first_falimy_iter('first_family_01.jpg', 'first_family_01_02.jpg', cnt2)

    if cnt3 > 0:
        wait_click('first_family_02.jpg')  # 뉴 페이스
        wait_click('first_family_02_01.jpg')  # 인휴먼 공주
        iter_battle(cnt3)

        # time.sleep(random.uniform(2.71, 3.53))
        # wait_click('ok_button.jpg')
        # time.sleep(random.uniform(0.71, 1.53))
        # check_click('reload_button.jpg')
        time.sleep(random.uniform(2.71, 3.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(0.71, 1.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(0.71, 1.53))

    if cnt4 > 0:
        wait_click('first_family_02.jpg')  # 뉴 페이스
        wait_click('first_family_02_02.jpg')  # 사나운 초록색
        iter_battle(cnt4)
        # time.sleep(random.uniform(3.71, 4.53))
        # check_click('ok_button.jpg')
        # time.sleep(random.uniform(0.71, 1.53))
        # check_click('reload_button.jpg')
        time.sleep(random.uniform(2.71, 3.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(0.71, 1.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(0.71, 1.53))

    if cnt5 > 0:
        wait_click('first_family_03.jpg')  # 뉴 페이스
        wait_click('first_family_03_01.jpg')  # 라트베리아
        iter_battle(cnt5)
        # time.sleep(random.uniform(3.71, 4.53))
        # check_click('ok_button.jpg')
        # time.sleep(random.uniform(0.71, 1.53))
        # check_click('reload_button.jpg')
        time.sleep(random.uniform(0.71, 1.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(0.71, 1.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(0.71, 1.53))
    time.sleep(random.uniform(2.71, 3.53))
    print('end first_family')


def x_force(cnt1=10, cnt2=10, cnt3=3, cnt4=3, cnt5=3):
    go_home()

    wait_click('enter_battle.jpg')
    wait_click('epic_quest.jpg')

    wait_click('x_force.jpg')

    def x_force_iter(but1, but2, cnt):
        wait_click(but1)  # 엉망인 친구들
        wait_click(but2)  # 이런 세상에

        sleep_click_v2(1274, 730, 1454, 784, 1.01, 2.23)  # 이런 세상에 #4

        iter_battle(cnt)
        time.sleep(random.uniform(2.71, 3.53))

        check_click('back_button.jpg')
        time.sleep(random.uniform(0.71, 1.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(0.71, 1.53))

    if cnt1 > 0:
        wait_click('x_force_01.jpg')  # 엉망인 친구들
        wait_click('x_force_01_01.jpg')  # 이런 세상에

        sleep_click_v2(1274, 730, 1454, 784, 1.01, 2.23)  # 이런 세상에 #4

        iter_battle(cnt1)
        time.sleep(random.uniform(2.71, 3.53))

        check_click('back_button.jpg')
        time.sleep(random.uniform(0.71, 1.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(0.71, 1.53))

    if cnt2 > 0:
        x_force_iter('x_force_01.jpg', 'x_force_01_02.jpg', cnt2)

    if cnt3 > 0:
        wait_click('x_force_02.jpg')  # 머저리
        wait_click('x_force_02_01.jpg')  # 크롬 덩어리
        iter_battle(cnt3)
        time.sleep(random.uniform(2.71, 3.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(0.71, 1.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(0.71, 1.53))

    if cnt4 > 0:
        wait_click('x_force_02.jpg')  # 머저리
        wait_click('x_force_02_02.jpg')  # 사이 로그 아웃
        iter_battle(cnt4)
        time.sleep(random.uniform(2.71, 3.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(0.71, 1.53))
    if cnt5 > 0:    # 케이블 자르기
        x_force_iter('x_force_03.jpg', 'x_force_03_01.jpg', cnt5)

    time.sleep(random.uniform(2.71, 3.53))
    print('end x_force')


def rise_xman(cnt1=10, cnt2=10, cnt3=10, cnt4=10, cnt5=2, cnt6=2):
    go_home()

    wait_click('enter_battle.jpg')
    wait_click('epic_quest.jpg')

    sleep_click_v2(1221, 215, 1712, 800, 1.01, 1.53)  # select_mission

    if cnt1 > 0:
        sleep_click_v2(767, 764, 860, 854, 1.01, 1.53)  # chasing
        time.sleep(random.uniform(1.01, 1.53))
        wait_click('rise_xman_01_01.jpg')
        # sleep_click_v2(308, 315, 545, 674, 1.01, 2.23)  # 악당이되다
        sleep_click_v2(1274, 730, 1454, 784, 1.01, 2.23)  # select_battle
        iter_battle(cnt1)
        time.sleep(random.uniform(2.71, 3.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(1.71, 2.53))
        check_click('back_button.jpg')

    if cnt2 > 0:
        sleep_click_v2(767, 764, 860, 854, 1.01, 1.53)  # chasing
        time.sleep(random.uniform(1.01, 1.53))
        wait_click('rise_xman_01_02.jpg')
        # sleep_click_v2(646, 317, 879, 676, 1.01, 2.23)  # 친구와 적
        sleep_click_v2(1274, 730, 1454, 784, 1.01, 2.23)  # select_battle
        iter_battle(cnt2)
        time.sleep(random.uniform(2.71, 3.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(1.71, 2.53))
        check_click('back_button.jpg')
    else:
        pass

    if cnt3 > 0:
        sleep_click_v2(767, 764, 860, 854, 1.01, 1.53)  # chasing
        time.sleep(random.uniform(1.01, 1.53))
        wait_click('rise_xman_01_03.jpg')
        # sleep_click_v2(977, 314, 1220, 675, 1.01, 2.23)  # 몰아치는 폭풍
        sleep_click_v2(1274, 730, 1454, 784, 1.01, 2.23)  # select_battle
        iter_battle(cnt3)
        time.sleep(random.uniform(2.71, 3.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(1.71, 2.53))
        check_click('back_button.jpg')
    else:
        pass

    if cnt4 > 0:
        sleep_click_v2(767, 764, 860, 854, 1.01, 1.53)  # chasing
        time.sleep(random.uniform(1.01, 1.53))
        wait_click('rise_xman_01_04.jpg')
        # sleep_click_v2(1312, 311, 1551, 670, 2.01, 3.23)  # 맹목적 전투
        sleep_click_v2(1274, 730, 1454, 784, 2.01, 3.23)  # select_battle
        iter_battle(cnt4)
        time.sleep(random.uniform(2.71, 3.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(1.71, 2.53))
        check_click('back_button.jpg')
        # time.sleep(random.uniform(1.71, 2.53))
        # check_click('back_button.jpg')
    else:
        pass

    if cnt5 > 0:
        wait_click('rise_xman_02.jpg')
        wait_click('rise_xman_02_01.jpg')
        # sleep_click_v2(1312, 311, 1551, 670, 2.01, 3.23)  # 매그니토의 힘
        sleep_click_v2(1274, 730, 1454, 784, 2.01, 3.23)  # select_battle
        iter_battle(cnt5)
        time.sleep(random.uniform(2.71, 3.53))
        check_click('ok_button.jpg')
        time.sleep(random.uniform(1.71, 2.53))
        check_click('reload_button.jpg')
        time.sleep(random.uniform(1.71, 2.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(1.71, 2.53))
        # time.sleep(random.uniform(1.71, 2.53))
        # check_click('back_button.jpg')
    else:
        pass

    if cnt6 > 0:
        # wait_click('rise_xman_02.jpg')
        wait_click('rise_xman_02_02.jpg')
        # sleep_click_v2(1312, 311, 1551, 670, 2.01, 3.23)  # 되살아난 피닉스
        sleep_click_v2(1274, 730, 1454, 784, 2.01, 3.23)  # select_battle
        iter_battle(cnt6)
        time.sleep(random.uniform(2.71, 3.53))
        check_click('ok_button.jpg')
        time.sleep(random.uniform(1.71, 2.53))
        check_click('reload_button.jpg')
        time.sleep(random.uniform(1.71, 2.53))
    else:
        pass
    time.sleep(random.uniform(2.71, 3.53))
    print('end rise_xman')

    # time.sleep(random.uniform(0.71, 1.53))
    # wait_click('back_button.jpg')


