import numpy as np
import cv2
import pyautogui

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)
 
#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def get_bbox():
	# image = cv2.imread("valorant_range_pic3.png")
	image = np.array(pyautogui.screenshot())
	hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

	# HSV bounds for gray area
	lower_bound = [20, 3, 10]
	upper_bound = [95, 50, 95]

	lower = np.array(lower_bound, dtype="uint8")
	upper = np.array(upper_bound, dtype="uint8")
	mask = cv2.inRange(hsv_image, lower, upper)
	output = cv2.bitwise_and(hsv_image, hsv_image, mask=mask)
	gray = get_grayscale(output)
	thresh = thresholding(gray)
	contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cnt = max(contours, key = cv2.contourArea)
	x,y,w,h = cv2.boundingRect(cnt)

	full_bbox = (x, y, x+w, y+h)
	score_bbox = (x, y, int(x + w / 2), y + h)
	remain_bbox = (int(x + w / 2), y, x + w, y + h)
	return (full_bbox, score_bbox, remain_bbox)


