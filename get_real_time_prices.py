import pytesseract
from PIL import ImageGrab
import cv2
import numpy as nm
import time
import datetime
import random

pytesseract.pytesseract.tesseract_cmd = "D:/Technologies/Tesseract-OCR/tesseract.exe"

options = {
    "al30_sell": {"enabled": True, "current_value": 0, "previous_value": 0, "coordinates": [1275, 446, 1370, 463], "position": 1},
    "al30c_sell": {"enabled": False, "current_value": 0, "previous_value": 0,"coordinates": [1275, 508, 1370, 525], "position": 1},
    "al30d_sell": {"enabled": False, "current_value": 0, "previous_value": 0,"coordinates": [1275, 570, 1370, 587], "position": 1},
    "al30_buy": {"enabled": False, "current_value": 0, "previous_value": 0,"coordinates": [1375, 446, 1470, 463], "position": 0},
    "al30c_buy": {"enabled": True, "current_value": 0, "previous_value": 0,"coordinates": [1375, 508, 1470, 525], "position": 0},
    "al30d_buy": {"enabled": True, "current_value": 0, "previous_value": 0,"coordinates": [1375, 570, 1470, 587], "position": 0},
}

chars_for_split = ["x", "=", "<", ">", "«", "*"]

def get_enabled_options():
    enabled_options = dict()
    for option, properties in options.items():
        if properties["enabled"]:
            enabled_options[option] = properties
    #print(str(enabled_options))

def update_enabled_options_property_current_value():
    for properties in enabled_options.values():
        #print(properties["current_value"])
        update_property_current_value(properties)
        #print(properties["current_value"])

def update_property_current_value(properties):
    string = ""
    while string == "":
        image = ImageGrab.grab(bbox=properties["coordinates"])
    # image.show()

        string = (
            pytesseract.image_to_string(
                cv2.cvtColor(nm.array(image), cv2.COLOR_BGR2GRAY), lang="eng"
            ).strip()
        )
    #print("string: " + string)

    string_formatted = format_string(string)

    properties["current_value"] = string_formatted.split(get_split_char(string_formatted))[properties["position"]].strip()
    # print("properties["current_value"]: " + properties["current_value"])

def format_string(string):
    string = string.replace(",", ".")

    if string[-1] == ".":
        string = string[:-1]
    
    return string

def get_split_char(string):
    for char in chars_for_split:
        if char in string:
            return char

def print_useful_values():
    useful_values = dict()
    for option, properties in enabled_options.items():
        
        current_value_string = properties["current_value"]
        previous_value_string = properties["previous_value"]

        if current_value_string != previous_value_string:
            current_value_float = float(current_value_string)

        if option == "al30c_buy":

            useful_values[option]    
            current_value_string = properties["current_value"]
            previous_value_string = properties["previous_value"]

        else:
            current_value_float = float(properties["current_value"])
            useful_values[option.split("_")[0]] = current_value_float / al30c




    # if al30_sell != previous_al30_sell or al30c_buy != previous_al30c_buy:
    #     al30c = al30_sell / al30c_buy
    
    # if al30d_sell != previous_al30d_sell or al30c_buy != previous_al30c_buy:
    #     al30d = al30d_sell / al30c_buy

    # print(
    #     datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #     + "   "
    #     + get_icon(al30c, previous_values["al30c"])
    #     + " "
    #     + f"{al30c:.3f}"
    #     + " ("
    #     + al30_sell_string
    #     + "/"
    #     + al30c_buy_string
    #     + ")   "
    #     + get_icon(al30d, previous_values["al30d"])
    #     + " "
    #     + f"{al30d:.3f}"
    #     + " ("
    #     + al30d_sell_string
    #     + "/"
    #     + al30c_buy_string
    #     + ")"
    # )






def get_icon(first_value, second_value):
    icon = ""
    if first_value == second_value:
        icon = "→"
    elif first_value < second_value:
        icon = "↓"    
    else:
        icon = "↑"

    return icon

def update_enabled_options_property_previous_value():
    for properties in enabled_options.values():
        properties["previous_value"] = properties["current_value"]



enabled_options = get_enabled_options()

seconds = int(input("refresh rate in seconds: "))
print("                           al30c                   al30d")


al30_sell_string = "840.00"
al30c_buy_string = "0.69"
al30d_sell_string = "0.685"

al30c = 1217.391 
al30d = 0.993

while True:
    update_enabled_options_property_current_value()
    print_useful_values()
    update_enabled_options_property_previous_value()
    time.sleep(seconds)