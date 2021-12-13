def prepareTable(pattern):
    p = [0, 0]
    i = 0
    for j in range(2, len(pattern)):
        while(i > 0 and pattern[i] != pattern[j-1]):
            i = p[i]
        if pattern[i] == pattern[j-1]:
            i += 1
            p[j] = i
    return p


def kMP(text, pattern):
    p = prepareTable(pattern)
    j, i = 0, 0
    while i < len(text) - len(pattern) + 2:
        j = p[j - 1]
        while pattern[j] == text[i + j - 2]:
            if j + 1 == len(pattern):
                break
            j += 1
        if j+1 == len(pattern) and pattern[j] == text[i+j-2]:
            return "Znaleziono wzorzec na pozycji {}".format(i-1)
        i = i + max(1, j-p[j-1])

text = "test testowej funkcji"
pattern = "fun"
print(kMP(text, pattern))