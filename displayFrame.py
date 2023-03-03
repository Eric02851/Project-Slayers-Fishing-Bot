import dxcam
from time import time
import cv2 as cv

cam = dxcam.create()

while True:
    loopTime = time()
    frame = cam.grab()
    if frame is not None:
        frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
        cv.imshow("Computer Vision", frame)

        print("FPS {}".format(1 / (time() - loopTime)))
        loopTime = time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print("Done")
