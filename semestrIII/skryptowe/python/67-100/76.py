
lista1 = [2, 4, 5, 7, 8, 19, 53]


def sprawdzenie(element, tab):
    if element in tab:
        return True
    return False


sprawdzenie(lista1, input("Podaj liczbe do sprawdzenia: "))
