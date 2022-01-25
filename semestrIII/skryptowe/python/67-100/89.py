text = input("Podaj ciag znakow: ")


def czy_palindrom(text):
    if text == text[::-1]:
        return print("Jest")
    else:
        return print("Nie jest")
