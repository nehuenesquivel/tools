import pytesseract
from PIL import ImageGrab
import cv2
import numpy as nm

pytesseract.pytesseract.tesseract_cmd = 'D:/Technologies/Tesseract-OCR/tesseract.exe'

def read(x0, y0, x1, y1, before_split_char):
    image = ImageGrab.grab(bbox = (x0, y0, x1, y1))
    #image.show()

    string = pytesseract.image_to_string(cv2.cvtColor(nm.array(image), cv2.COLOR_BGR2GRAY), lang ='eng').strip() 
    #print(string)

    if string == "":
        value = ""
        #print("empty")
    else:        
        if string[-1] == ",":
            string = string[:-1]

        if "x" in string:
            split_char = "x"
        elif "=" in string:
            split_char = "="

        value = string.split(split_char)[0 if before_split_char else 1].replace(",", ".")
        #print("-> " + value)

    return value

al30_sell_string = read(1275, 446, 1370, 463, False)
al30c_buy_string = read(1375, 508, 1470, 525, True)
al30d_sell_string = read(1275, 570, 1370, 587, False)

al30c_buy_value = float(al30c_buy_string)
al30c_price = float(al30_sell_string) / al30c_buy_value
al30d_price = float(al30d_sell_string) / al30c_buy_value

print("al30c_price: " + al30_sell_string + " / " + al30c_buy_string + " = " + str(al30c_price))
print("al30d_price: " + al30d_sell_string + " / " + al30c_buy_string + " = " + str(al30d_price))