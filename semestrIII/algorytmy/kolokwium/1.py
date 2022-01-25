def KarpRabin(text, pattern):
    alphabet = {}

    for y, x in enumerate(text):
        if x not in alphabet.keys():
            alphabet[x] = y
    result = 0

    prime = 23
    m = len(pattern)
    textH = 0
    patternH = 0

    for i in range(m):

        patternH = (patternH * len(alphabet) +
                    alphabet[pattern[i]]) % prime
        textH = (textH * len(alphabet) +
                 alphabet[text[i]]) % prime

    i = 0

    while i < len(text) - len(pattern):
        if textH == patternH:
            if text[i:i + len(pattern)] == pattern:
                result += 1

        textH = ((textH - (alphabet[text[i]] * pow(len(alphabet), len(pattern) - 1))) * len(
            alphabet) + alphabet[text[i + len(pattern)]]) % prime

        i += 1
    return result


text = "Kot sie schowal za kotara dla kota kota który się nazywa kot"
pattern = "kot"
print(KarpRabin(text, pattern))
