import time
import random


# class sortMethod:
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


def quickSort(tab: list) -> list:
    if len(tab) <= 1:
        return tab
    else:
        pivot = tab[0]
        less = [i for i in tab[1:] if i <= pivot]
        greater = [i for i in tab[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)


def mergeSort(tab):
    if len(tab) <= 1:
        return tab
    else:
        return merge(mergeSort(tab[: len(tab) // 2]), mergeSort(tab[len(tab) // 2:]),)


def merge(tab1, tab2):
    tab3 = []
    while len(tab1) > 0 and len(tab2) > 0:
        if tab1[0] < tab2[0]:
            tab3.append(tab1[0])
            tab1.remove(tab1[0])
        else:
            tab3.append(tab2[0])
            tab2.remove(tab2[0])
    if len(tab1) == 0:
        tab3.extend(tab2)
    else:
        tab3.extend(tab1)
    return tab3


def heapify(tab, i, n):
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and tab[l] > tab[i]:
        largest = l
    else:
        largest = i
    if r < n and tab[r] > tab[largest]:
        largest = r
    if largest != i:
        tab[i], tab[largest] = tab[largest], tab[i]
        heapify(tab, largest, n)


def heapSort(tab):
    n = len(tab)
    for i in range(n // 2 - 1, -1, -1):
        heapify(tab, i, n)
    for i in range(n - 1, 0, -1):
        tab[i], tab[0] = tab[0], tab[i]
        heapify(tab, 0, i)
    return tab


def main():
    toSort = [random.randint(0, 100) for x in range(nOSamples)]
    start = time.time()
    bubbleSort(list(toSort))
    print(f"BubbleSort dla {nOSamples}: {time.time()-start}")
    start = time.time()
    insertionSort(list(toSort))
    print(f"InsertionSort dla {nOSamples}: {time.time()-start}")
    start = time.time()
    quickSort(list(toSort))
    print(f"QuickSort dla {nOSamples}: {time.time()-start}")
    start = time.time()
    mergeSort(list(toSort))
    print(f"MergeSort dla {nOSamples}: {time.time()-start}")
    start = time.time()
    heapSort(list(toSort))
    print(f"HeapSort dla {nOSamples}: {time.time()-start}")


if __name__ == "__main__":
    nOSamples = 1000
    main()
    nOSamples = 10000
    main()
