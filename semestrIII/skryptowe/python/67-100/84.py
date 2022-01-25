def check_type():
    inp = input("Wpisz liczbe: ")
    if isinstance(inp, int):
        print("Liczba jest typu int")
    elif isinstance(inp, float):
        print("Liczba jest typu float")
    elif isinstance(inp, str):
        print("Liczba jest typu string")
    else:
        print("Nieznany typ")
