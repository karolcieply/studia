import random


def quickSort(tab: list, chosen: int) -> list:
    if isinstance(tab, tuple) or len(tab) <= 1:
        return tab
    else:
        pivot = -1
        notChosen = 2 if chosen == 1 else 1
        pivot, index = tab[0], 0

        less, greater = [], []
        for i in tab[1:]:
            pass
        less = [i for i in tab[1:] if (i[chosen-1] < pivot[chosen-1]) or (
            i[chosen-1] == pivot[chosen-1] and (i[notChosen-1] < pivot[notChosen-1] or i[notChosen-1] == pivot[notChosen-1]))]
        greater = [i for i in tab[1:] if i[chosen-1] > pivot[chosen-1] or (
            i[chosen-1] == pivot[chosen-1] and i[notChosen-1] > pivot[notChosen-1])]
        return quickSort(less, chosen) + [pivot] + quickSort(greater, chosen)


data = []
with open("input.txt", "r") as f:
    temp = f.read().splitlines()
for i in range(0, len(temp), 2):
    data.append((int(temp[i]), int(temp[i+1])))
chosen = int(input("Według czego chcesz sortować? (1/2)"))
output = quickSort(data, chosen)
with open("output_sort_1.txt", "w") as f:
    for i in range(25):
        f.write(f"{output[i]}\n")
