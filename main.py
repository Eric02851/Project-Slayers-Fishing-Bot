import time
import pydirectinput
import pyautogui

class Circle:
    white = (255,255,255)
    blue = (125, 205, 255)
    x = 1280
    y = 1335
    bottomy = 1385

class fishingBar:
    blue = (52, 201, 255)
    yellow = (255, 206, 28)
    cords = (1075, 1179, 410, 1)

def checkBar():
    img = pyautogui.screenshot(region=fishingBar.cords)

    bluePixels = []
    for i in range(410):
        color = img.getpixel((i,0))
        if color == fishingBar.blue:
            bluePixels.append(i)

    #bluePixels = bluePixels[int(len(bluePixels)/2) -2:int(len(bluePixels)/2) +2]
    yellowOnBlue=False
    while not yellowOnBlue:
        img = pyautogui.screenshot(region=fishingBar.cords)
        for i in bluePixels:
            if img.getpixel((i,0)) == fishingBar.yellow:
                pydirectinput.click(Circle.x, Circle.bottomy)
                yellowOnBlue = True
                break

def checkfishon():
    pixelwhite = pyautogui.pixelMatchesColor(Circle.x, Circle.y, Circle.white)
    pixelblue = pyautogui.pixelMatchesColor(Circle.x, Circle.y, Circle.blue)
    return pixelwhite or pixelblue

time.sleep(3)
while True:
    pydirectinput.click(1280, 720)

    while not checkfishon():
        time.sleep(0.1)

    while checkfishon():
        checkBar()
        time.sleep(0.1)

    time.sleep(0.5)
    pydirectinput.press('e')
    time.sleep(0.5)
