class Symbol:
    def __init__(self, symbol, weight):
        self.symbol = symbol
        self.weight = weight

    def __repr__(self) -> str:
        return f"{self.symbol}:{self.weight}"


class Node:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    @property
    def weight(self):
        return self.left.weight + self.right.weight

    def __repr__(self) -> str:
        return f"{self.left}-{self.right}"

    def getCode(self):
        res = dict()
        if isinstance(self.right, Node):
            for k, v in self.right.getCode().items():
                res["1" + k] = v
        else:
            res["1"] = self.right.symbol
        if isinstance(self.left, Node):
            for k, v in self.left.getCode().items():
                res["0" + k] = v
        else:
            res["0"] = self.left.symbol
        return res


def huffman(Points, Probability):
    nodes = [Symbol(Points[i], Probability[i]) for i in range(len(Points))]
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.weight)
        a, b = nodes.pop(1), nodes.pop(0)
        nodes.append(Node(a, b))
    return dict((v, k) for k, v in nodes[0].getCode().items())
    # return nodes[0].getCode()


S = ["a", "b", "c", "d", "e", "f"]
P = [0.3, 0.1, 0.2, 0.1, 0.2, 0.1]
print(huffman(S, P))
S = ["a", "i", "s", "d"]
P = [0.1, 0.2, 0.3, 0.4]
print(huffman(S, P))
