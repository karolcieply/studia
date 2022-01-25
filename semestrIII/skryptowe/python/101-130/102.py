
def silnia(n):
    return n * silnia(n-1) if n > 1 else 1
