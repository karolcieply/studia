from math import atan


import string
path = "C:/67/dane/danezadanie95.txt"
with open(path, "r") as file:
    data = file.read()
    l = data.split(" ")
    av = []
    for i in l:
        av.append(len(i))
    avg = sum(av) / len(av)

    print("Srednia długość: ", avg)
    print("Długość poszczególnych elementów: \n", av)
    print("Ilość słów: ", len(av))
    print()

    print("Ilość liter: ")
    print()

    lst = string.ascii_lowercase
    t = data.lower()
    for i in lst:
        print(i, "->", t.count(i), end="\n")
    print()
