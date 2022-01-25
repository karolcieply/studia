from datetime import datetime


def convert_string_to_datatime(string):
    if string is None:
        return print("No date found")
    if string.isspace():
        return datetime.strptime(string, "%Y-%m-%d %H:%M:%S")
    else:
        return datetime.strptime(string, "%Y-%m-%d")


print(convert_string_to_datatime("2016-10-31"))
