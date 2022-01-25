n = input("Podaj rozmiar tablicy: ")
lista = list()
suma = 0
for element in range(int(n)):
    a = input("Podaj liczbe do dodania: ")
    lista.append(int(a))
for element in lista:
    suma += int(element)
print("średnia: ", suma / int(n))
print("suma: ", suma)

lista.sort()
print(lista)
if len(lista) % 2 == 1:
    print("mediana: ", lista[int(len(lista) / 2)])
else:
    print(
        "mediana: ", (lista[int(len(lista) / 2) - 1] + lista[int(len(lista) / 2)]) / 2
    )
