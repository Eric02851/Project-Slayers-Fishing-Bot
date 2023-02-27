import time
import pydirectinput
import dxcam

class Circle:
    white = (255,255,255)
    blue = (125, 205, 255)

    middley = 1271
    bottomy = 1333
    x = 1280

class Bar:
    blue = (52, 201, 255)
    yellow = (255, 206, 28)

    width = 410
    x = 1075
    y = 1134

def getFrame():
    frame = cam.grab()
    while frame is None: frame = cam.grab()
    return frame

def checkBar():
    frame = getFrame()
    bluePixels = set()

    for i in range(410):
        color = tuple(frame[Bar.y, Bar.x + i])
        if color == Bar.blue: bluePixels.add(i)

    yellowOnBlue=False
    while not yellowOnBlue:
        frame = getFrame()
        for i in bluePixels:
            if tuple(frame[Bar.y, Bar.x + i]) == Bar.yellow:
                pydirectinput.click(Circle.x, Circle.bottomy)
                yellowOnBlue = True

                print(F"Detected: {Bar.x + i}")
                break

def checkFishing():
    frame = getFrame()
    color = tuple(frame[Circle.middley, Circle.x])
    return color == Circle.white or color == Circle.blue

cam = dxcam.create()
fishCount = 0
time.sleep(3)

while True:
    pydirectinput.click(1280, 720)
    while not checkFishing(): time.sleep(0.1)

    while checkFishing():
        checkBar()
        time.sleep(0.1)

    time.sleep(0.5)
    pydirectinput.press('e')
    time.sleep(0.5)

    fishCount += 1
    print(f"Caught Fish: {fishCount}\n")
