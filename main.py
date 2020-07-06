import cv2
import pytesseract
import numpy as np
from PIL import Image
import pyautogui
import range_recorder as rr

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

image_list = []
valid_numbers = ["OO", "00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
for j in range(10):
    valid_numbers.append("O" + str(j))
for i in range(10, 31):
    valid_numbers.append(str(i))
ready_to_exit = False
dumb_bool = False
final_score = 0

print("RUNNING...")
# while True:
    # remain_side_img = rr.get_remaining_side()
    # inverted_remain = rr.get_inverted_img(remain_side_img)
    # remain_str = pytesseract.image_to_string(inverted_remain)
    # print(remain_str)
    # if "00" in remain_str or "OO" in remain_str:
    #     print('dick')
while not(dumb_bool):
    print("NO RANGE FOUND...")
    remain_side_img = rr.get_remaining_side()
    inverted_remain = rr.get_inverted_img(remain_side_img)
    remain_str = pytesseract.image_to_string(inverted_remain)
    if "30" in remain_str:
        print("RANGE DETECTED!")
        print("WAITING TO FINISH RANGE")
        while not(ready_to_exit):
            remain_side_img = rr.get_remaining_side()
            inverted_remain = rr.get_inverted_img(remain_side_img)
            remain_str = pytesseract.image_to_string(inverted_remain)
            if "00" in remain_str or "OO" in remain_str or "01" in remain_str or "O1" in remain_str:
                score_side_img = rr.get_score_side()
                inverted_score = rr.get_inverted_img(score_side_img)
                score_str = pytesseract.image_to_string(inverted_score)
                for num in valid_numbers:
                    if num in score_str:
                        if num == "00" or num == "OO":
                            final_score = 0
                        else:
                            final_score = int(num)
                        ready_to_exit = True
                        dumb_bool = True
                        break
print("FINAL SCORE: ", final_score)



# def range_is_finished(string):
#     if "00" in string or "oo" in string.lower():
#         return True
#     valid_num_present = False
#     for num in valid_numbers:
#         if num in string:
#             valid_num_present = True
#     return not(valid)

            
    # for num in valid_numbers:
    #     if num in remain_str:



# cv2.imshow("gray", gray)
# cv2.imshow("opening", opening)
# cv2.imshow("canny", canny)
#closing all open windows  
# out_below = pytesseract.image_to_string(thresh)

# out_gray = pytesseract.image_to_string(gray)

# out_opening = pytesseract.image_to_string(opening)
# out_canny = pytesseract.image_to_string(canny)

# out_gray = pytesseract.image_to_string(gray, config="--psm 13")

# out_opening = pytesseract.image_to_string(opening, config="--psm 13")
# out_canny = pytesseract.image_to_string(canny, config="--psm 13")
# img = cv2.imread('remaining2.png')
# while True:
#     img = rr.get_remaining_side()
#     gray = get_grayscale(img)
#     thresh = thresholding(gray)
#     inverted = invert(thresh)
#     out_thresh = pytesseract.image_to_string(thresh)
#     out_invert = pytesseract.image_to_string(inverted)
#     out_thresh_config = pytesseract.image_to_string(thresh, config="--psm 13")
#     out_invert_config = pytesseract.image_to_string(inverted, config="--psm 13")
#     cv2.imshow("invert", inverted)
#     cv2.imshow("thresh", thresh)
#     cv2.waitKey(0)  



# for i in range(200):
#     # make a screenshot
#     # screenshot for score
#     img = pyautogui.screenshot(region=(925, 250, 200, 160)) # left, top, width, height
#     # 650, 200, 600, 320
#     # convert these pixels to a proper numpy array to work with OpenCV
#     image_list.append(img)
#     frame = np.array(img)
#     # convert colors from BGR to RGB
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     gray = rr.get_grayscale(frame)
#     thresh = rr.thresholding(gray)
#     inverted = rr.invert(thresh)
#     out_invert = pytesseract.image_to_string(inverted)
#     string_list = []
#     for number in valid_numbers:
#         if number in out_invert:
#             print(number)
    # out_thresh = pytesseract.image_to_string(thresh)
    # out_thresh_config = pytesseract.image_to_string(thresh, config="--psm 13")
    # out_invert_config = pytesseract.image_to_string(inverted, config="--psm 13")
    # print("================== WITHOUT CONFIG =================")
    # print("Invert output:", out_invert)
    # print("Thresh output:", out_thresh)
    # print("=================== WITH CONFIG ===================")
    # print("Invert output:", out_invert_config)
    # print("Thresh output:", out_thresh_config)
    # cv2.imshow("invert", inverted)
    # cv2.imshow("thresh", thresh)
    # write the frame
    # out.write(frame)
    # show the frame
    # cv2.imshow("RECORDING", frame)

# # make sure everything is closed when exited

# height,width,channel = np.array(img).shape
# out = cv2.VideoWriter('video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 5, (width,height))

# for images in image_list:
#     out.write(cv2.cvtColor(np.array(images),cv2.COLOR_BGR2RGB))
# out.release()
# cv2.destroyAllWindows()

# cv2.destroyAllWindows()
# img = rr.get_remaining_side()
# gray = get_grayscale(img)
# thresh = thresholding(gray)
# opening = opening(gray)
# canny = canny(gray)
# invert = invert(thresh)

# cv2.imshow("thresh", thresh)
# cv2.imshow("invert", invert)
# cv2.waitKey(0)

# Notes:
# For reading numbers + text:
# Use no config and inverted
# For reading numbers:
# Use --psm 13 and inverted

# Plan:
# 1. Split range scoreboard into SCORE and REMAINING
# 2. Find the text in the image (REMAINING or SCORE) and replace it with a white box
# 3. Search image with --psm 13 and inverted to get the number
# 4. Wait for REMAINING to be 00
# 5. Store the number under SCORE once REMAINING is 00

# print("================== WITHOUT CONFIG =================")
# print("Invert output:", out_invert)
# print("Thresh output:", out_thresh)
# print("=================== WITH CONFIG ===================")
# print("Invert output:", out_invert_config)
# print("Thresh output:", out_thresh_config)

