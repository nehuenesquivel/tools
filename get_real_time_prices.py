import pytesseract
from PIL import ImageGrab
import cv2
import numpy as nm
import time
import datetime
import winsound

pytesseract.pytesseract.tesseract_cmd = "D:/Technologies/Tesseract-OCR/tesseract.exe"

chars_for_split = ["x", "=", "<", ">", "«", "*", "~"]

al30_sell = {
    "name": "al30_sell",
    "current_price": 0,
    "previous_price": 0,
    "current_value": 0,
    "previous_value": 0,
    "coordinates": [1275, 446, 1370, 463],
    "position": 1,
}
al30d_sell = {
    "name": "al30d_sell",
    "current_price": 0,
    "previous_price": 0,
    "current_value": 0,
    "previous_value": 0,
    "coordinates": [1275, 570, 1370, 587],
    "position": 1,
}
al30c_buy = {
    "current_value": 0,
    "previous_value": 0,
    "coordinates": [1375, 508, 1470, 525],
    "position": 0,
}


def update_values():
    update_option_values(al30_sell)
    update_option_values(al30d_sell)
    update_option_values(al30c_buy)


def update_option_values(option):
    string = ""
    while string == "":
        image = ImageGrab.grab(bbox=option["coordinates"])
        # image.show()
        string = pytesseract.image_to_string(
            cv2.cvtColor(nm.array(image), cv2.COLOR_BGR2GRAY), lang="eng"
        ).strip()
        # print("string: " + string)

    string_formatted = format_string(string)
    try:
        option["previous_value"] = option["current_value"]
        option["current_value"] = float(
            string_formatted.split(get_split_char(string_formatted))[option["position"]]
        )
        # print("option["current_value"]: " + option["current_value"])
    except Exception as exception:
        print("update exception: ", exception)
        print("* resuming *")


def format_string(string):
    string = string.replace(",", ".").replace(":", ".")
    if string[-1] == ".":
        string = string[:-1]
    return string


def get_split_char(string):
    for char in chars_for_split:
        if char in string:
            return char


def update_prices():
    update_option_prices(al30_sell)
    update_option_prices(al30d_sell)


def update_option_prices(option):
    option["previous_price"] = option["current_price"]
    option["current_price"] = round(
        option["current_value"] / al30c_buy["current_value"], 4
    )


def print_prices():
    print(
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        + "   "
        + get_recap(al30_sell)
        + "    "
        + get_recap(al30d_sell)
    )


def get_recap(option):
    return (
        get_visual_clue(option)
        + " "
        + f'{option["current_price"]:.4f}'
        + " ("
        + f'{option["current_value"]:.4f}'
        + "/"
        + f'{al30c_buy["current_value"]:.4f}'
        + ")"
    )


def get_visual_clue(option):
    name = option["name"]
    current_price = option["current_price"]
    previous_price = option["previous_price"]

    clue = ""
    if (name == "al30_sell" and current_price >= 1200) or (
        name == "al30d_sell" and current_price >= 1.015
    ):
        clue = "→"
        winsound.Beep(4250, 100)
    elif current_price == previous_price or previous_price == 0:
        clue = " "
    elif current_price < previous_price:
        clue = "↓"
    else:
        clue = "↑"
    return clue


seconds = 1  # int(input("refresh rate in seconds: "))
space = " "
print(space * 29 + "al30" + space * 25 + "al30d")
while True:
    update_values()
    update_prices()
    print_prices()
    time.sleep(seconds)
