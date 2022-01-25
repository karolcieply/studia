import random

a = input("Podaj poczatek przedzialu: ")
b = input("Podaj koniec przedzialu: ")

x = random.randint(int(a), int(b))

lista = []
with open("lista.txt", "r") as plik:
    for linia in plik:
        lista.append(int(linia))
y = random.choice(lista)
with open("wynikzadanie84.txt", "w") as plik:
    plik.write(str(x) + "\n")
    plik.write(str(y))
