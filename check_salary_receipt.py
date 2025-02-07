from datetime import datetime


def print_screen(dict):
    for key, value in dict.items():
        print(key + ": " + str(value))


def write_file(dict):
    file = open(
        datetime.today().strftime("%m-%Y") + "_salary-receipt-reference.txt",
        "w",
    )
    for key, value in dict.items():
        file.write(key + ": " + str(value) + "\n")
    file.close()


salary_in_usd = float(input("Salary in USD: "))
official_usd_value_in_ars = float(input("Official USD value in ARS: "))
unofficial_usd_value_in_ars = float(input("Unofficial USD value in ARS: "))

dict = dict()
dict["Salary in ARS"] = salary_in_usd * official_usd_value_in_ars
dict["SIJP"] = dict["Salary in ARS"] * 0.11
dict["INSSJP"] = dict["Salary in ARS"] * 0.03
dict["OSOC"] = dict["Salary in ARS"] * 0.03
dict["Deductions"] = dict["SIJP"] + dict["INSSJP"] + dict["OSOC"]
dict["Official Net"] = dict["Salary in ARS"] - dict["Deductions"]
dict["Net in ARS"] = dict["Official Net"] * 0.3
dict["Net in USD"] = dict["Official Net"] * 0.7 / official_usd_value_in_ars
dict["Unofficial Net"] = dict["Net in ARS"] + dict["Net in USD"] * unofficial_usd_value_in_ars

print_screen(dict)

with open("official_and_unofficial_USD_value_in_ARS_per_month.txt", "a") as file:
    file.write(
        str(datetime.now().year) + "{:02d}".format(datetime.now().month)
        + ": official " + str(official_usd_value_in_ars)
        + ", unofficial " + str(unofficial_usd_value_in_ars)
        + "\n"
    )
