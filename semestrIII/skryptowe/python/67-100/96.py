path1 = "C:/67/dane/danezadanie96.txt"
path2 = "C:/67/wyniki/wyjsciezadanie96.txt"
with open(path1, "r") as f1:
    with open(path2, "w") as f2:
        f2.write(f1.read().upper())
