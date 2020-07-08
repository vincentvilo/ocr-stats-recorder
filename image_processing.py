import cv2
import numpy as np
import pyautogui
import detect_color
from PIL import Image, ImageGrab
import pytesseract

def get_inverted_img(image):
    frame = np.array(image)
    gray = get_grayscale(frame)
    thresh = thresholding(gray)
    inverted = invert(thresh)
    return inverted

def get_bbox_dims(bbox):
    return (bbox[0], bbox[1], bbox[2], bbox[3])

def get_score_region():
    """returns an image of the SCORE side of the RANGE scoreboard
    Returns:
        numpy array: image of SCORE side converted into np array;
            contains the str 'SCORE' and score # (int)
    """
    full_bbox, score_bbox, remain_bbox = detect_color.get_bbox()
    img = ImageGrab.grab(score_bbox)
    return np.array(img)

def get_remain_region():
    """returns an image of the SCORE side of the REMAINING scoreboard
    Returns:
        numpy array: image of REMAINING side converted into np array;
            contains the str 'REMAINING' and score # (int)
    """
    full_bbox, score_bbox, remain_bbox = detect_color.get_bbox()
    img = ImageGrab.grab(remain_bbox)
    return np.array(img)

def get_full_region():
    full_bbox, score_bbox, remain_bbox = detect_color.get_bbox()
    img = ImageGrab.grab(full_bbox)
    return np.array(img)

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

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

#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def invert(image):
    return cv2.bitwise_not(image)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def get_thresh_img(image):
    frame = np.array(image)
    gray = get_grayscale(frame)
    thresh = thresholding(gray)
    return thresh

def get_resized_image(filename):
    basewidth = 1000
    img = Image.open(filename)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save('RESIZED_IMAGE.jpg')
    return cv2.imread('RESIZED_IMAGE.jpg')