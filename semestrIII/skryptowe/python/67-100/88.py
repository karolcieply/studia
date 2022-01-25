import random

a = input("Podaj liczbe kolumn: ")
b = input("Podaj liczbe wierszy: ")
c = input("Podaj przedzial losowania liczb: ")
d = input("Podaj koniec przedzialu losowania liczb")
for wiersz in range(int(a)):
    for kolumna in range(int(b)):
        print(random.randint(int(c), int(d)), end=" ")
    print()
