import cv2
import numpy as np
import pyautogui
import hsv_filter
from PIL import Image, ImageGrab
import pytesseract

def get_bbox_dims(bbox):
    return (bbox[0], bbox[1], bbox[2], bbox[3])

def get_score_region():
    full_bbox, score_bbox, remain_bbox = hsv_filter.get_bbox()
    img = ImageGrab.grab(score_bbox)
    return np.array(img)

def get_remain_region():
    full_bbox, score_bbox, remain_bbox = hsv_filter.get_bbox()
    img = ImageGrab.grab(remain_bbox)
    return np.array(img)

def get_full_region():
    full_bbox, score_bbox, remain_bbox = hsv_filter.get_bbox()
    img = ImageGrab.grab(full_bbox)
    return np.array(img)

def get_processed_img(image):
    frame = np.array(image)
    gray = get_grayscale(frame)
    thresh = thresholding(gray)
    inverted = invert(thresh)
    no_noise = remove_noise(inverted)
    deskewed = deskew(no_noise)
    return deskewed

# preprocessing functions used are from https://bit.ly/2O8pQRT 

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def invert(image):
    return cv2.bitwise_not(image)

def remove_noise(image):
    return cv2.medianBlur(image, 7)

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