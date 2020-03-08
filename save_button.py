import pyautogui as pag
import time
# import random


time.sleep(1)
x1, y1 = pag.position()
print('x, %s, y: %s' % (x1, y1))
time.sleep(4)
x2, y2 = pag.position()
print('x, %s, y: %s' % (x2, y2))

screen = pag.screenshot(region=(x1, y1, x2-x1, y2-y1))
f_name = input('Filename please: ')
screen.save('buttons/' + f_name + '.jpg')

'''

screen = pag.screenshot(region=(38, 37, 447-38, 82-37))
# f_name = input('Filename please: ')
screen.save('buttons/Account02.jpg')
'''
# x, 1438, y: 944 ~ x, 1780, y: 1006

# att_1_x, att_1_y = x, 1502, y: 590
# 1502, 590, 140, 140
# att_button_1.jpg

# att_2_x, att_2_y = x, 1391, y: 711
# att_button_2.jpg

# att_3_x, att_3_y = x, 1666, y: 595
# att_4_x, att_4_y = x, 1414, y: 873
# att_5_x, att_5_y = x, 1246, y: 873
# 반지름은 140 정도 되는듯

# 계정 확인 위치
# x, 38, y: 37
# x, 447, y: 82
# Filename please: Account03

