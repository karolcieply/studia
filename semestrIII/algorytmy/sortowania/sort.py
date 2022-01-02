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

    def mergeSort(array):
        if len(array) <= 1:
            return array
        else:
            return sortMethod.merge(
                sortMethod.mergeSort(array[: len(array) // 2]),
                sortMethod.mergeSort(array[len(array) // 2 :]),
            )

    def merge(array1, array2):
        array3 = []
        while len(array1) > 0 and len(array2) > 0:
            if array1[0] < array2[0]:
                array3.append(array1[0])
                array1.remove(array1[0])
            else:
                array3.append(array2[0])
                array2.remove(array2[0])
        if len(array1) == 0:
            array3.extend(array2)
        else:
            array3.extend(array1)
        return array3

    def heapify(array, i, n):
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and array[l] > array[i]:
            largest = l
        else:
            largest = i
        if r < n and array[r] > array[largest]:
            largest = r
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            sortMethod.heapify(array, largest, n)

    def heapSort(array):
        n = len(array)
        for i in range(n // 2 - 1, -1, -1):
            sortMethod.heapify(array, i, n)
        for i in range(n - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            sortMethod.heapify(array, 0, i)
        return array


print(sortMethod.insertionSort([5, 2, 1, 4, 3]))
print(sortMethod.bubbleSort([5, 2, 1, 4, 3]))
print(sortMethod.quickSort([5, 2, 1, 4, 3]))
