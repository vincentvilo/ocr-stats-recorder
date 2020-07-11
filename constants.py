# Path/file names
TESSERACT_PATH = r'Tesseract-OCR\tesseract'
OUT_DIRNAME = "output_files"
ALLSCORES_PATH = "output_files/_allscores.csv"

# Valid scores
VALID_NUMBERS = ["OO", "00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
for i in range(10, 31):
    VALID_NUMBERS.append(str(i))

# Keystrokes
QUIT_KEY = 27 # ESC key
ALLTIME_AVG_KEY = ord('1')
WEEK_AVG_KEY = ord('2')
GET_PREV_KEY = ord('3')
GET_GRAPH_KEY = ord('4')
