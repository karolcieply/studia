a = input("Podaj liczbe a: ")
b = input("Podaj liczbe b: ")

try:
    print(int(a) / int(b))
except ZeroDivisionError:
    print("Nie dziel przez zero!")
