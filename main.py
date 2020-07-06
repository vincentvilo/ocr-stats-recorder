import cv2
import pytesseract
import numpy as np
from PIL import Image
import pyautogui
import image_processing as ip

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

valid_numbers = ["OO", "00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
for j in range(10):
    valid_numbers.append("O" + str(j))
for i in range(10, 31):
    valid_numbers.append(str(i))
ready_to_exit = False
range_finished = False
final_score = 0

print("RUNNING...")

while not(ready_to_exit):
    print("NO RANGE FOUND...")
    remain_side_img = ip.get_remaining_side()
    inverted_remain = ip.get_inverted_img(remain_side_img)
    remain_str = pytesseract.image_to_string(inverted_remain)
    if "30" in remain_str:
        print("RANGE DETECTED!")
        print("WAITING TO FINISH RANGE")
        while not(ready_to_exit):
            remain_side_img = ip.get_remaining_side()
            inverted_remain = ip.get_inverted_img(remain_side_img)
            remain_str = pytesseract.image_to_string(inverted_remain)
            if "00" in remain_str or "OO" in remain_str or "01" in remain_str or "O1" in remain_str:
                score_side_img = ip.get_score_side()
                inverted_score = ip.get_inverted_img(score_side_img)
                score_str = pytesseract.image_to_string(inverted_score)
                for num in valid_numbers:
                    if num in score_str:
                        if num == "00" or num == "OO":
                            final_score = 0
                        else:
                            final_score = int(num)
                        ready_to_exit = True
                        range_finished = True
                        break
print("FINAL SCORE: ", final_score)