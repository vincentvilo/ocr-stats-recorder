import cv2
import numpy as np
import pyautogui

# display screen resolution, get it from your OS settings
# SCREEN_SIZE = (1920, 1080)
# # # define the codec
# fourcc = cv2.VideoWriter_fourcc(*"XVID")
# # # create the video write object
# out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))

image_list = []

for i in range(200):
    # make a screenshot
    img = pyautogui.screenshot(region=(650, 200, 600, 320)) # left, top, width, height
    # 650, 200, 600, 320
    # convert these pixels to a proper numpy array to work with OpenCV
    image_list.append(img)
    frame = np.array(img)
    # convert colors from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # write the frame
    # out.write(frame)
    # show the frame
    cv2.imshow("screenshot", frame)

# make sure everything is closed when exited
cv2.destroyAllWindows()

height,width,channel = np.array(img).shape
out = cv2.VideoWriter('video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 5, (width,height))

for images in image_list:
    out.write(cv2.cvtColor(np.array(images),cv2.COLOR_BGR2RGB))
out.release()

# 10 secs if recording at 20 fps
# for i in range(200):
#     # make a screenshot
#     img = pyautogui.screenshot()
#     # the rest of the code...

# make sure everything is closed when exited
cv2.destroyAllWindows()
out.release()