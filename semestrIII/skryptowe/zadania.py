def main():
    choice = input("chcesz zakodować(y) czy odkodować(n)")
    string = input("podaj słowo: ").lower()
    shift = int(input("podaj przesuniecie: "))
    if choice=="y":
        print(crypt(string, shift))
    elif choice=="n":
        print(decrypt(string, shift))

def moveChar(char, move):
    move = move % 26
    return chr(ord(char)+move-26) if ord(char)+move > 122 else chr(ord(char)+move)

def crypt(toCrypt, move=1):
    return "".join([moveChar(x, move) for x in toCrypt])

def decrypt(toDecrypt, move=1):
    return "".join([moveChar(x, -move) for x in toDecrypt])

if __name__=="__main__":
    main()