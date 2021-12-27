class Symbol:
    def __init__(self, symbol, weight):
        self.symbol = symbol
        self.weight = weight
        self.code = ""

    def __repr__(self) -> str:
        return f"{self.symbol}, {self.code}"


def calculateSplit(symbols):
    if len(symbols) > 1:
        maxDifference, splitPoint = 1, 0
        for i in range(1, len(symbols)):
            left = symbols[:i]
            right = symbols[i:]
            leftSum = sum([x.weight for x in left])
            rightSum = sum([x.weight for x in right])
            if (x := abs(leftSum - rightSum)) < maxDifference:
                maxDifference = x
                splitPoint = i
        return (
            calculateSplit(symbols[:splitPoint]),
            calculateSplit(symbols[splitPoint:]),
        )
    else:
        return symbols


def generateCode(symbols, code=""):
    if isinstance(symbols, tuple):
        generateCode(symbols[0], code + "0")
        generateCode(symbols[1], code + "1")
    elif isinstance(symbols, list):
        generateCode(symbols[0], code)
    else:
        symbols.code = code
        return


global symbols

S = ["a", "b", "c", "d", "e"]
P = [0.3, 0.1, 0.1, 0.2, 0.3]
symbols = [Symbol(S[i], P[i]) for i in range(len(S))]
symbols.sort(key=lambda x: -x.weight)
symbols = calculateSplit(symbols)
generateCode(symbols)
print(symbols)

