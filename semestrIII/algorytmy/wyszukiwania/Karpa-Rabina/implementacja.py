def kR(text, pattern, hPattern, f, q):
    for i in range(len(text)):
        temp = ''
        for j in range(i, len(pattern)+i, 1):
            if j < len(text):
                temp += text[j]
        hTemp = h(temp, f, q)
        if hTemp == hPattern:
            return i


def h(pattern, f, q):
    result = 0
    for i in range(len(pattern)):
        result += f[pattern[i]]*len(pattern)**(len(pattern)-1-i)
    return result % q


text = "abacdcbdacd"
pattern = "acdc"
i = 0
q = 23
f = {}
for letter in sorted(text):
    if letter not in f:
        f[letter] = i
        i += 1
hPattern = h(pattern, f, q)
print(kR(text, pattern, hPattern, f, q))
