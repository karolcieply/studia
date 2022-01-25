def to_int():
    try:
        a = input("Podaj liczbe: ")
        return int(a)
    except Exception:
        print("nie liczba")
