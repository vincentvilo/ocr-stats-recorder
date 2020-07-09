import numpy as np
import cv2
import pyautogui

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def get_bbox():
	# HSV bounds for current patch
	lower_bound = [75, 30, 70]
	upper_bound = [150, 90, 100]

	image = np.array(pyautogui.screenshot())
	bgr_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
	# image = cv2.imread("images/valorant_range_pic4.png") # used for testing
	hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
	lower = np.array(lower_bound, dtype="uint8")
	upper = np.array(upper_bound, dtype="uint8")
	mask = cv2.inRange(hsv_image, lower, upper)
	output = cv2.bitwise_and(hsv_image, hsv_image, mask=mask)
	gray = get_grayscale(output)
	thresh = thresholding(gray)
	contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cnt = max(contours, key=cv2.contourArea)
	x,y,w,h = cv2.boundingRect(cnt)
	full_bbox = (x, y, x+w, y+h)
	score_bbox = (x, y, int(x + w / 2), y + h)
	remain_bbox = (int(x + w / 2), y, x + w, y + h)
	
	# used for testing
	# cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
	# cv2.imshow('image', hsv_image)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

	return full_bbox, score_bbox, remain_bbox