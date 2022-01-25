def rzymski(liczba):
    liczba = int(liczba)
    wynik = ""
    while liczba > 0:
        if liczba >= 1000:
            wynik = wynik + "M"
            liczba = liczba - 1000
        elif liczba >= 900:
            wynik = wynik + "CM"
            liczba = liczba - 900
        elif liczba >= 500:
            wynik = wynik + "D"
            liczba = liczba - 500
        elif liczba >= 400:
            wynik = wynik + "CD"
            liczba = liczba - 400
        elif liczba >= 100:
            wynik = wynik + "C"
            liczba = liczba - 100
        elif liczba >= 90:
            wynik = wynik + "XC"
            liczba = liczba - 90
        elif liczba >= 50:
            wynik = wynik + "L"
            liczba = liczba - 50
        elif liczba >= 40:
            wynik = wynik + "XL"
            liczba = liczba - 40
        elif liczba >= 10:
            wynik = wynik + "X"
            liczba = liczba - 10
        elif liczba >= 9:
            wynik = wynik + "IX"
            liczba = liczba - 9
        elif liczba >= 5:
            wynik = wynik + "V"
            liczba = liczba - 5
        elif liczba >= 4:
            wynik = wynik + "IV"
            liczba = liczba - 4
        elif liczba >= 1:
            wynik = wynik + "I"
            liczba = liczba - 1
    return wynik


print(rzymski(1955))
