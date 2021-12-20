def bM(text, pattern):
    last = {}
    for i, v in enumerate(pattern):
        last[v] = i
    i = len(pattern) - 1
    j = len(pattern) - 1
    while i < len(text):
        if text[i] == pattern[j]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            i = i + len(pattern) - min(j, 1 + last.get(text[i], 0))
            j = len(pattern) - 1
    return -1


print(bM("csfbadxbcabdzabdabc", "abdabc"))