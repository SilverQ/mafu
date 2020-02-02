import pyautogui as pag
import cv2
from pytesseract import *
from PIL import Image
from scipy.ndimage import rotate
import time


def ocr_att_button():
    # att5
    # 1291, 920, 50, 50

    screen = pag.screenshot(region=(1291, 920, 50, 50))
    screen.save("att_button_tmp.jpg")
    image = cv2.imread("att_button_tmp.jpg")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    gray = cv2.medianBlur(gray, 1)
    # rot = rotate(img, -20, reshape=False)
    gray = rotate(gray, 20, reshape=False)
    cv2.imwrite("att_button_tmp.jpg", gray)
    custom_oem_psm_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789.%'
    text = pytesseract.image_to_string(Image.open('att_button_tmp.jpg'), lang='eng',
                                       # config='--psm 7 -c tessedit_char_whitelist=0123456789.%')
                                       config=custom_oem_psm_config)
    print(text)
    # 숫자 인식률이 개그지, 파일 저장이 중간에 과다하게 들어가고, 파일 저장 없이 바로 이용하는 방법 아직 찾지 못함


while True:
    time.sleep(1)
    ocr_att_button()

# att_1_x, att_1_y = x, 1502, y: 590
# 1502, 590, 140, 140
# att_button_1.jpg

# att_2_x, att_2_y = x, 1391, y: 711
# att_button_2.jpg

# att_3_x, att_3_y = x, 1666, y: 595
# att_4_x, att_4_y = x, 1414, y: 873
# att_5_x, att_5_y = x, 1246, y: 873
# 반지름은 140 정도 되는듯

