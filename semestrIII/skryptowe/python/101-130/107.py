def code_caesar(s, k):
    return "".join(chr(((ord(c) - ord("a") + k) % 26) + ord("a")) for c in s)


def decode_caesar(s, k):
    return code_caesar(s, -k)


print(code_caesar("abc", 1))
print(decode_caesar("bcd", 1))
