# Wczytaj dane z pliku liczby.txt i wpisz je do listy.


liczby = []
with open("liczby.txt", "r") as plik:
    for linia in plik:
        liczby.append(int(linia))

suma = 0
for element in liczby:
    suma += int(element)
print("średnia: ", suma / len(liczby))
print("suma: ", suma)

liczby.sort()
print(liczby)
if len(liczby) % 2 == 1:
    print("mediana: ", liczby[int(len(liczby) / 2)])
else:
    print(
        "mediana: ",
        (liczby[int(len(liczby) / 2) - 1] + liczby[int(len(liczby) / 2)]) / 2,
    )
