import cv2
import numpy as np
import pyautogui

# display screen resolution, get it from your OS settings
# SCREEN_SIZE = (1920, 1080)
# # # define the codec
# fourcc = cv2.VideoWriter_fourcc(*"XVID")
# # # create the video write object
# out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))

SCORE_REGION = (800, 250, 200, 160)
REMAINING_REGION = (925, 250, 200, 160)

def get_inverted_img(image):
    frame = np.array(image)
    gray = get_grayscale(frame)
    thresh = thresholding(gray)
    inverted = invert(thresh)
    return inverted

def get_score_side():
    """returns an image of the SCORE side of the RANGE scoreboard
    Returns:
        numpy array: image of SCORE side converted into np array;
            contains the str 'SCORE' and score # (int)
    """
    img = pyautogui.screenshot(region=SCORE_REGION)
    return np.array(img)

def get_remaining_side():
    """returns an image of the SCORE side of the REMAINING scoreboard
    Returns:
        numpy array: image of REMAINING side converted into np array;
            contains the str 'REMAINING' and score # (int)
    """
    img = pyautogui.screenshot(region=REMAINING_REGION)
    return np.array(img)

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)
 
#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#dilation
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
#erosion
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

#opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)

#skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

#template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

def invert(image):
    return cv2.bitwise_not(image)

    
# # TESTING STUFF
# image_list = []
# for i in range(200):
#     # make a screenshot
#     # screenshot for score
#     img = pyautogui.screenshot(region=(800, 250, 200, 160)) # left, top, width, height
#     # 650, 200, 600, 320
#     # convert these pixels to a proper numpy array to work with OpenCV
#     image_list.append(img)
#     frame = np.array(img)
#     # convert colors from BGR to RGB
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     cv2.imshow
#     # write the frame
#     # out.write(frame)
#     # show the frame
#     cv2.imshow("RECORDING", frame)

# # make sure everything is closed when exited

# height,width,channel = np.array(img).shape
# out = cv2.VideoWriter('video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 5, (width,height))

# for images in image_list:
#     out.write(cv2.cvtColor(np.array(images),cv2.COLOR_BGR2RGB))
# out.release()
# cv2.destroyAllWindows()