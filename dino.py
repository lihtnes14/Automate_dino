import cv2
import numpy as np
import pyautogui

while True:
    image = pyautogui.screenshot(region=(200, 350, 255, 250))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    black_pixel = np.sum(image < 100)
    white_pixel = np.sum(image > 100)
    print("The number of black pixel = ", black_pixel)
    print("The number of white pixel = ", white_pixel)

    if black_pixel > 4000 and black_pixel < 30000:
        pyautogui.press("up")

    cv2.imshow("image", image)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
