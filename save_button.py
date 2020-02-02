import pyautogui as pag

screen = pag.screenshot(region=(1568, 930, 1784-1568, 1004-937))
screen.save('reload_button.jpg')

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
