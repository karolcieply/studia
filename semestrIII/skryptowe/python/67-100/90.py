def silnia(x):
    if x == 0:
        return 1
    return x * silnia(x - 1)


print(silnia(30))
