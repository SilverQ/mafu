import pyautogui as pag
import time
import random


while True:
    time.sleep(random.uniform(2.01, 4.23))
    x, y = pag.position()
    print('x, %s, y: %s' % (x, y))

# but1 = {'t_l': {'x': 400, 'y': 500},
#         'b_r': {'x': 500, 'y': 600}}

# pag.moveTo(x=100, y=100)
# pag.moveTo(x=800, y=200)
# pag.moveTo(x=300, y=300)
# pag.moveTo(x=700, y=400)
# 쪽지 확인