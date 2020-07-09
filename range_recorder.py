import cv2
import pytesseract
import numpy as np
from PIL import Image
import pyautogui
import image_processing as ip
import file_writer as fw
import time
import msvcrt

pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract'

output_path = "output_files/scores.csv"
out_dirname = "output_files"
out_filename = "scores.csv"
output_path = out_dirname + "/" + out_filename
valid_numbers = ["OO", "00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
for i in range(10, 31):
    valid_numbers.append(str(i))

def get_score():
    ready_to_exit = False
    final_score = 0
    print("To exit out of the program, press 'ESC' before/after starting a range session\n")
    print("RANGE NOT STARTED\n")
    fw.create_dir(out_dirname, out_filename)
    while not(ready_to_exit):
        remain_region_img = ip.get_remain_region()
        processed_remain = ip.get_processed_img(remain_region_img)
        remain_str = pytesseract.image_to_string(processed_remain)
        if msvcrt.kbhit(): # 27 -> ESC key
	        if ord(msvcrt.getch()) == 27:
	            return -1
        if "30" in remain_str or "29" in remain_str:
            print("RANGE DETECTED! WAITING TO FINISH RANGE...\n")
            while not(ready_to_exit):
                remain_region_img = ip.get_remain_region()
                processed_remain = ip.get_processed_img(remain_region_img)
                remain_str = pytesseract.image_to_string(processed_remain)
                if(("00" in remain_str) or ("OO" in remain_str)):
                    print("FINDING SCORE...\n")
                    score_region_img = ip.get_score_region()
                    processed_score = ip.get_processed_img(score_region_img)
                    score_str = pytesseract.image_to_string(processed_score)
                    for num in valid_numbers:
                        if num in score_str:
                            if not(num == "00" or num == "OO"):
                                final_score = int(num)
                            ready_to_exit = True
                            break
    print("==================================================================")
    print("RANGE COMPLETED!\n")
    print("On that trial, you scored: " + str(final_score) + "\n")
    print("==================================================================")
    return final_score

if __name__ == "__main__":
    print("RANGE RECORDER HAS STARTED!\n")
    while True:
        score = get_score()
        if score == -1:
            break
        else:
            fw.write_score(score, output_path)
    print("Recorder exiting...")
    time.sleep(2)

