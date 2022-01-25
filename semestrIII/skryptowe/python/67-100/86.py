a = input("Podaj liczbe kolumn: ")
b = input("Podaj liczbe wierszy: ")

for wiersz in range(int(a)):
    for kolumna in range(int(b)):
        print("*", end="")
    print()
