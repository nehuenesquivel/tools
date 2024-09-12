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


dict = dict()
dict["Salary in USD"] = float(input("Salary in USD: "))
dict["USD value in ARS"] = float(input("USD value in ARS: "))
dict["Salary in ARS"] = dict["Salary in USD"] * dict["USD value in ARS"]
dict["SIJP"] = dict["Salary in ARS"] * 0.11
dict["INSSJP"] = dict["Salary in ARS"] * 0.03
dict["OSOC"] = dict["Salary in ARS"] * 0.03
dict["Deductions"] = dict["SIJP"] + dict["INSSJP"] + dict["OSOC"]
dict["Net"] = dict["Salary in ARS"] - dict["Deductions"]
dict["Net in ARS"] = dict["Net"] * 0.3
dict["Net in USD"] = dict["Net"] * 0.7 / dict["USD value in ARS"]

print_screen(dict)
