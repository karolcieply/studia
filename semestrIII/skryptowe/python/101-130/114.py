import math


def polygon_box(number_of_sides, length):
    angle = 360 / number_of_sides
    area = number_of_sides * length ** 2 / (4 * math.tan(math.radians(angle / 2)))
    return area


nos = int(input())
l = float(input())

print(polygon_box(nos, l))
