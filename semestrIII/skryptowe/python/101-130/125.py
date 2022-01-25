def rzymska_na_calkowita(rzymska):
    liczba_rzymska = {"I": 1, "V": 5, "X": 10,
                      "L": 50, "C": 100, "D": 500, "M": 1000}
    liczba_calkowita = 0
    for i in range(len(rzymska)):
        if i > 0 and liczba_rzymska[rzymska[i]] > liczba_rzymska[rzymska[i - 1]]:
            liczba_calkowita += (
                liczba_rzymska[rzymska[i]] - 2 * liczba_rzymska[rzymska[i - 1]]
            )
        else:
            liczba_calkowita += liczba_rzymska[rzymska[i]]
    return liczba_calkowita


print(rzymska_na_calkowita("XX"))
print(rzymska_na_calkowita("MMMCMXCIX"))
