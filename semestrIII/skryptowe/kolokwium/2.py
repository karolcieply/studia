def calculate(input):
    output = []
    for number in input:
        hexn = 0x0
        decn = 0o0
        octn = 0
        if len(number) > 1:
            if number[1] == "o":  # oct
                octn = number
                decn = int(number, 0)
                hexn = hex(int(number, 8))
            elif number[1] == "x":  # hex
                hexn = number
                decn = int(number, 0)
                octn = oct(int(number, 16))
            else:  # dec
                decn = number
                octn = oct(int(number))
                hexn = hex(int(number))

            output.append(str(decn).ljust(8)+"|" +
                          str(octn).center(8)+"|"+str(hexn).rjust(8))
        else:
            decn = int(number)
            octn = oct(int(number))
            hexn = hex(int(number))

            output.append(str(decn).ljust(8) + "|" +
                          str(octn).center(8)+"|"+str(hexn).rjust(8))
    return output


def main():
    try:
        with open("danezadanie2.txt", "r") as f:
            input = f.read().splitlines()
    except Exception as e:
        print("Błąd przy wczytywaniu pliku")
        return

    try:
        output = ["liczby dziesietne | liczby osemkowe | liczby szesnastkowe",
                  "--------------------------------------------------------"]+calculate(input)
    except Exception as e:
        print("Błąd przy obliczaniu")
        return
    try:
        with open("wyjsciezadanie2.txt", "w") as f:
            for o in output:
                f.write(o+"\n")
    except Exception as e:
        print("Błąd przy wpisywaniu do pliku")
        return


if __name__ == "__main__":
    main()
