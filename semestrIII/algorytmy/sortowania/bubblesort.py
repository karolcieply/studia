from heapq import heapify


class sortMethod:
    def insertionSort(tab: list) -> list:
        for i in range(1, len(tab)):
            key = tab[i]
            j = i - 1
            while j >= 0 and key < tab[j]:
                tab[j + 1] = tab[j]
                j -= 1
            tab[j + 1] = key
        return tab

    def bubbleSort(tab: list) -> list:
        for i in range(len(tab)):
            for j in range(len(tab) - 1):
                if tab[j] > tab[j + 1]:
                    tab[j], tab[j + 1] = tab[j + 1], tab[j]
        return tab

    def quickSort(array):
        if len(array) <= 1:
            return array
        else:
            pivot = array[0]
            less = [i for i in array[1:] if i <= pivot]
            greater = [i for i in array[1:] if i > pivot]
            return sortMethod.quickSort(less) + [pivot] + sortMethod.quickSort(greater)


print(sortMethod.insertionSort([5, 2, 1, 4, 3]))
print(sortMethod.bubbleSort([5, 2, 1, 4, 3]))
print(sortMethod.quickSort([5, 2, 1, 4, 3]))
