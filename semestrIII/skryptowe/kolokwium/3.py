import numpy as np


def Transpose(matrix):
    result = np.zeros((np.shape(matrix)[1], np.shape(matrix)[0]))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]
    return result


def main():
    input = []
    try:
        with open("macierzwejsciowa.txt", "r") as f:
            input = f.read().splitlines()
            input = [x.split() for x in input]
    except Exception as e:
        print("Błąd przy wczytywaniu pliku")
        return
    try:
        output = Transpose(input)
    except Exception as e:
        print("Błąd przy transpozycji")
        return
    try:
        with open("macierzwyjsciowa.txt", "w") as f:
            for x in output:
                for y in x:
                    f.write(str(y)+" ")
                f.write("\n")
    except Exception as e:
        print("Błąd przy wpisywaniu do pliku")
        return


if __name__ == "__main__":
    main()
