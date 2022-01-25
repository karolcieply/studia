a = input("Podaj liczbe kolumn: ")
b = input("Podaj liczbe wierszy: ")

with open("wyjsciezadanie86.txt", "w") as plik:
    for wiersz in range(int(a)):
        for kolumna in range(int(b)):
            plik.write("*")
        plik.write("\n")
