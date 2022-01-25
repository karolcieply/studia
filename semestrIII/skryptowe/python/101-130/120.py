a = input("Wprowadź liczbe dziesietna: ")

a = a.split(".")

licznik = int(a[1])
mianownik = int(10 ** (len(a[1])))


def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return int(a)


nwd = nwd(int(licznik), int(mianownik))
print(int(licznik / nwd), "/", int(mianownik / nwd))
