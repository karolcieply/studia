lista = input("Podaj rozmiar tablicy: ")
for element in range(int(lista)):
    lista.append(input("Podaj liczbe do dodania: "))
for element in lista:
    print(element)
