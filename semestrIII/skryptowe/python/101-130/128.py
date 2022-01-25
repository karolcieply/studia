class matma:
    def pow(x, n):
        if n == 0:
            return 1
        elif n % 2 == 0:
            return matma.pow(x, n // 2) ** 2
        else:
            return x * matma.pow(x, n // 2) ** 2


print(matma.pow(2, 3))
