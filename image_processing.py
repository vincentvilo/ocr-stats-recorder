import cv2
import numpy as np
import pyautogui

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

