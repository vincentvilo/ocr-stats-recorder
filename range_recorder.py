import cv2
import pytesseract
from PIL import Image
import pyautogui
import time
import msvcrt
import numpy as np
import image_processing as ip
import file_writer as fw
import scores_calculator as calc
import os
import constants
import console


pytesseract.pytesseract.tesseract_cmd = constants.TESSERACT_PATH

def get_ocr_str(image):
    processed_image = ip.get_processed_img(image)
    return pytesseract.image_to_string(processed_image)

def get_score():
    ready_to_exit = False
    final_score = 0
    console.print_ready()
    while not(ready_to_exit):
        if msvcrt.kbhit(): 
            keypress = ord(msvcrt.getch())
            if(keypress == constants.QUIT_KEY):
                return -1
            elif(keypress == constants.ALLTIME_AVG_KEY):
                console.reset()
                console.print_overall_average()
            elif(keypress == constants.WEEK_AVG_KEY):
                console.reset()
                console.print_weekly_average()
            elif(keypress == constants.GET_PREV_KEY):
                console.reset()
                console.print_previous_scores()
            elif(keypress == constants.GET_GRAPH_KEY):
                console.reset()
                console.plot_all_scores()
        remain_str = get_ocr_str(ip.get_remain_region())
        if "30" in remain_str:
            console.reset()
            console.print_range_found()
            while not(ready_to_exit):
                remain_str = get_ocr_str(ip.get_remain_region())
                if(("00" in remain_str) or ("OO" in remain_str)):
                    print("FINDING SCORE...")
                    score_str = get_ocr_str(ip.get_score_region())
                    for num in constants.VALID_NUMBERS:
                        if num in score_str:
                            if not(num == "00" or num == "OO"):
                                final_score = int(num)
                            ready_to_exit = True
                            break
    console.reset()
    console.print_completed_score(final_score)
    return final_score

if __name__ == "__main__":
    fw.create_dir_files()
    console.print_starting()
    console.print_instructions()
    while True:
        score = get_score()
        if score == -1:
            break
        else:
            date_score_filepath = constants.OUT_DIRNAME + "/" + fw.get_file_name()
            fw.write_score(score, date_score_filepath)
            fw.write_score(score, constants.ALLSCORES_PATH)
    console.print_exiting()
    time.sleep(1)