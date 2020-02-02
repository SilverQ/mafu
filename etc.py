import pyautogui
import time
import numpy as np
import pyscreenshot as ImageGrab


def mimagegrab():
    # x = 240
    # y = 266
    # box = (x, y, x + 20, y + 20)
    box = (1246, 873, 1246+140, 873+140)
    image = ImageGrab.grab(box)
    # grayImage = imageOps.grayImage(image)
    # a = array(grayImage.getcolors())
    a = np.asanyarray(image)
    print(a)

    b = a.sum()
    print(b)

    # if (b < 296400):
    #     pressSpace()
    # print(b)


mimagegrab()

#
# def restartGame():
#     pyautogui.click(325, 444)
#
#
# def pressSpace():
#     pyautogui.keyDown('space')
#     time.sleep(0.05)
#     print("Jump")
#     pyautogui.keyUp('space')
#     time.sleep(0.05)
#
#
# while (True):
#     x, y = pyautogui.position()
#     # print(x,y,"\n")
#     # time.sleep(2)
#     mimageGrab()



# def pass_over_old():
#     # 건너뛰기
#     # x, 1601, y: 62
#     # x, 1796, y: 130
#     app = wx.App()
#     screen = wx.ScreenDC()
#     bmp = wx.Bitmap(1920, 1080)
#     mem = wx.MemoryDC(bmp)
#     # mem.Blit(0, 0, 1920, 1080, screen, 0, 0)
#     mem.Blit(1601, 62, 1796, 130, screen, 0, 0)
#     del mem
#     text = pytesseract.image_to_string(bmp, lang='kor')
#     print(text)


# def pass_over2_old():
#     screen = pag.screenshot(region=(1601, 62, 1796-1601, 130-62))
#     screen.save("button.jpg")
#
#     text = pytesseract.image_to_string(Image.open("button.jpg"), config='-psm 6')
#     # text = pytesseract.image_to_string(screen, lang='kor')
#     print(text)
#     # https: // pyautogui.readthedocs.io / en / latest / quickstart.html  # general-functions


# def pass_over3_old():
#     screen = pag.screenshot(region=(1601, 62, 1796-1601, 130-62))
#     screen.save("D:/tmp/tmp.jpg")
#     imageA = cv2.imread("D:/tmp/tmp.jpg")
#     # imageA = cv2.imread(screen)
#     # # imageA = screen.
#     imageB = cv2.imread("button.jpg")
#
#     # cv2.imshow("Screenshot", screen)
#     # cv2.imshow("SavedImage", imutils.resize(imageB, width=600))
#
#     # convert the images to grayscale
#     grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
#     grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
#
#     # images, ensuring that the difference image is returned
#     (score, diff) = structural_similarity(grayA, grayB, full=True)
#     # diff = (diff * 255).astype("uint8")
#     # print("SSIM: {}".format(score))
#     if score > 0.95:
#         mouse_click((1796+1601)/2 + random.uniform(0, (1796-1601)*0.7),
#                     (130+62)/2 + random.uniform(0, (130-62)*0.7))
#     # https://www.pyimagesearch.com/2017/06/19/image-difference-with-opencv-and-python/

# pass_over3()


# pass_over4()

# def capture_screen():
#     app = wx.App()
#     screen = wx.ScreenDC()
#     bmp = wx.Bitmap(1920, 1080)
#     mem = wx.MemoryDC(bmp)
#     # mem.Blit(0, 0, 1920, 1080, screen, 0, 0)
#     mem.Blit(100, 100, 500, 500, screen, 0, 0)
#     del mem
#     bmp.SaveFile('wx1.bmp', wx.BITMAP_TYPE_BMP)


# capture_screen()

# x, y = pag.position()
# print('x, %s, y: %s' % (x, y))
# # x, 3216, y: 244

# x, 39, y: 36

# while True:
#     time.sleep(random.uniform(2.01, 4.23))
#     x, y = pag.position()
#     print('x, %s, y: %s' % (x, y))

# but1 = {'t_l': {'x': 400, 'y': 500},
#         'b_r': {'x': 500, 'y': 600}}

# pag.moveTo(x=100, y=100)
# pag.moveTo(x=800, y=200)
# pag.moveTo(x=300, y=300)
# pag.moveTo(x=700, y=400)
# 쪽지 확인
