samogloski = ["a", "e", "i", "o", "u", "y"]

string = input("Podaj ciag znakow: ")

for element in string:
    if element in samogloski:
        print(element)
