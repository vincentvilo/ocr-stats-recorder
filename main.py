import cv2
import pytesseract
import numpy as np
from PIL import Image
import pyautogui
import image_processing as ip
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

valid_numbers = ["OO", "00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
for i in range(10, 31):
    valid_numbers.append(str(i))

# TODO : look for bounding box in a certain region (center of screen? center top?)

def run_score_recorder():
    print("RUNNING...")
    ready_to_exit = False
    range_finished = False
    final_score = 0
    while not(ready_to_exit):
        print("NO RANGE FOUND...")
        remain_region_img = ip.get_remain_region()
        inverted_remain = ip.get_inverted_img(remain_region_img)
        remain_str = pytesseract.image_to_string(inverted_remain)
        if "30" in remain_str or "29" in remain_str:
            print("RANGE DETECTED!")
            print("WAITING TO FINISH RANGE")
            while not(ready_to_exit):
                remain_region_img = ip.get_remain_region()
                inverted_score = ip.get_inverted_img(remain_region_img)
                remain_str = pytesseract.image_to_string(inverted_score)
                if(("00" in remain_str) or ("OO" in remain_str)):
                    print("FINDING SCORE...")
                    score_region_img = ip.get_score_region()
                    inverted_score = ip.get_inverted_img(score_region_img)
                    no_noise = ip.remove_noise(inverted_score)
                    deskewed = ip.deskew(no_noise)
                    score_str = pytesseract.image_to_string(deskewed)
                    for num in valid_numbers:
                        if num in score_str:
                            if not(num == "00" or num == "OO"):
                                final_score = int(num)
                            ready_to_exit = True
                            range_finished = True
                            break
    return final_score

print("FINAL SCORE:", run_score_recorder())
