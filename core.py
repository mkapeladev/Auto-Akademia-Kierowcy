
import cv2
import numpy as np
import pyautogui
import time

# Load the template image you want to detect
template = cv2.imread('dalejgr.png')

# Define the timeout duration in seconds (2 minutes)
timeout_duration = 120
start_time = time.time()

while True:
    # Capture the screen
    screenshot = pyautogui.screenshot()

    # Convert the screenshot to a NumPy array
    screen = np.array(screenshot)

    # Convert BGR to RGB
    screen_rgb = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)

    # Perform template matching
    result = cv2.matchTemplate(screen_rgb, template, cv2.TM_CCOEFF_NORMED)

    # Set a threshold to consider it a match
    threshold = 0.8
    loc = np.where(result >= threshold)

    if len(loc[0]) > 0:
        # Calculate the center coordinates of the match
        y, x = loc[0][0] + template.shape[0] // 2, loc[1][0] + template.shape[1] // 2

        # Click on the center of the detected image using PyAutoGUI
        pyautogui.click(x, y)
        print("Clicked on template_image.png")

        # Reset the start time
        start_time = time.time()
    else:
        # Check if the timeout duration has been reached
        if time.time() - start_time >= timeout_duration:
            # Display an alert message if the template is not found within the timeout
            pyautogui.alert("Template image not found on the screen within 2 minutes.")
            break

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
#
# #making img understandable to opencv
# ekran_img = cv.imread('test_ekr.png', cv.IMREAD_UNCHANGED)
# spec_img = cv.imread('dalejgr.png', cv.IMREAD_UNCHANGED)
# result = cv.matchTemplate(ekran_img , spec_img , cv.TM_CCOEFF_NORMED)
#
# min_val , max_value, min_loc , max_loc = cv.minMaxLoc(result)
#
# print(max_loc)
# print(max_value)
#
# treshold = 0.8
# if max_value >= treshold:
#     print("found")
#
#     dalej_w = spec_img.shape[1]
#     dalej_h = spec_img.shape[0]
#     top_l = max_loc
#     bot_r = (top_l[0] + dalej_w, top_l[1]+ dalej_h)
#     cv.rectangle(ekran_img,  top_l, bot_r , (255,255,0), 2,)
#     cv.imshow("bob", ekran_img)
#     cv.waitKey()
# else:
#     print("not found")