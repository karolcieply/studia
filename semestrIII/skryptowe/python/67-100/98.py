import csv
import math

path = "C:/67/dane/danezadanie98.txt"
with open(path, "r") as f:
    r = csv.reader(f, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    a, b, c = [x for x in r][0]
    de = (b ** 2) - (4 * a * c)
    if de >= 0:
        x1 = (-b - math.sqrt(de)) / (2 * a)
        x2 = (-b - math.sqrt(de)) / (2 * a)

    if de < 0:
        x1 = (-complex(b, 0) - complex(0, -math.sqrt(-de))) / (2 * a)
        x2 = (-complex(b, 0) + complex(0, -math.sqrt(-de))) / (2 * a)

print(x1, x2)
