with open("wyjscie.txt", "r") as plik:
    a = plik.readline()
a = list(a)
print(a)
licznik = 0
for element in a:
    if not element.isnumeric():
        print(element)
        licznik += 1

print("Liczba wystapien: ", licznik)
