from utils import *
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('account', type=int,
                    help='0: current, 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020')
args = parser.parse_args()
print('You selected ', args.account)

game_log = load_log('game_log.json')
# write_log(game_log)

remained_energy = 120
remained_energy = detect_energy()
print('Remained Energy = ', remained_energy)

dim_to_epic(args.account, game_log)

# def pass_over4():
#     # 버튼의 이미지가 있다면, 화면에서 해당 버튼의 좌표를 산출할 수 있다.
#     # https://pyautogui.readthedocs.io/en/latest/screenshot.html
#     # pass_over_button = pag.locateOnScreen('button_pass_over.jpg')
#     pass_over_button = pag.locateOnScreen('buttons/pass_over.jpg', grayscale=True, confidence=.7)
#     print(pass_over_button)
#     # https://automatetheboringstuff.com/chapter18/
#     # locateOnScreen은 이미지가 완벽하게 매칭되어야 함 ㅠㅠ
#     # Note that the image on the screen must match the provided image perfectly in order to be recognized.
#
#     # Box(left=1416, top=562, width=50, height=41)
#     if pass_over_button is not None:
#         print(pass_over_button[0])
#         mouse_click(pass_over_button[0] + pass_over_button[2]/2 + random.uniform(0, pass_over_button[2]*0.3),
#                     pass_over_button[1] + pass_over_button[3]/2 + random.uniform(0, pass_over_button[3]*0.3))
#         # pag.moveTo(x=pass_over_button[0], y=pass_over_button[1])
#
#
# def start_battle():
#     pag.moveTo(x=911, y=962)
#     pag.mouseDown()
#     time.sleep(random.uniform(0.01, 0.23))
#     pag.mouseUp()
#
#
# def check_status():
#     if pag.locateOnScreen('reload_button.jpg', grayscale=True, confidence=.9):
#         return True
#     else:
#         return False
#
#
# def check_att():
#     # 건너뛰기
#     # x, 1601, y: 62
#     # x, 1796, y: 130
#     app = wx.App()
#     screen = wx.ScreenDC()
#     bmp = wx.Bitmap(1920, 1080)
#     mem = wx.MemoryDC(bmp)
#     # mem.Blit(0, 0, 1920, 1080, screen, 0, 0)
#     mem.Blit(1578, 1006, 1678, 1106, screen, 0, 0)
#     del mem
#     text = pytesseract.image_to_string(bmp, lang='kor')
#     print(text)
#     # x, 1438, y: 944 ~ x, 1780, y: 1006
#     # att_1_x, att_1_y = x, 1578, y: 667
#     # att_2_x, att_2_y = x, 1466, y: 781
#     # att_3_x, att_3_y = x, 1744, y: 668
#     # att_4_x, att_4_y = x, 1474, y: 944
#     # att_5_x, att_5_y = x, 1320, y: 936
#     # 반지름은 100 정도 되는듯
#
#
# def wait(filename):
#     while True:
#         if pag.locateOnScreen(os.path.join('buttons/', filename), grayscale=True, confidence=.9):
#             break
#         else:
#             time.sleep(random.uniform(1.0, 2))
#
#
# def wait_click_v2(condition, filename):
#     while True:
#         if pag.locateOnScreen(os.path.join('buttons/', condition), grayscale=True, confidence=.9):
#             time.sleep(random.uniform(0.1, 0.5))
#             check_click(filename)
#             time.sleep(random.uniform(0.1, 0.5))
#             if pag.locateOnScreen(os.path.join('buttons/', filename), grayscale=True, confidence=.9) is None:
#                 break
#         else:
#             time.sleep(random.uniform(0.5, 1))
#
#
# def iter_battle_v2(condition):
#     while True:
#         sleep_click(1618, 977, 300, 70, 2.51, 4.23)        # start_battle
#         while True:
#             if pag.locateOnScreen('buttons/reload_button.jpg', grayscale=True, confidence=.9):
#                 time.sleep(random.uniform(3, 4))
#                 check_click('reload_button.jpg')
#                 time.sleep(random.uniform(2.5, 3.5))
#                 break
#             else:
#                 time.sleep(random.uniform(2, 3))
#
#
# def check_status_v2(filename, confidence=0.9):
#     if pag.locateOnScreen(os.path.join('buttons/', filename), grayscale=True, confidence=confidence):
#         return True
#     else:
#         return False
