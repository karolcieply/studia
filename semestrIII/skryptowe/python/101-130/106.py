import time
import datetime
import random


def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        return quick_sort([x for x in arr[1:] if x < arr[0]])\
            + [arr[0]]\
            + quick_sort([x for x in arr[1:] if x >= arr[0]])


def sort_statistics():
    bubble_times = []
    insertion_times = []
    quick_times = []

    no_of_samples = 10
    for i in range(no_of_samples):
        numbers = [random.randint(0, 300) for i in range(200)]

        start = time.time()
        bubble_sort(numbers)
        end = time.time()
        bubble_time = end - start

        start = time.time()
        insertion_sort(numbers)
        end = time.time()
        insertion_time = end - start

        start = time.time()
        quick_sort(numbers)
        end = time.time()
        quick_time = end - start

        bubble_times.append(bubble_time)

        insertion_times.append(insertion_time)
        quick_times.append(quick_time)

    mean_bubble_time = sum(bubble_times) / no_of_samples
    mean_insertion_time = sum(insertion_times) / no_of_samples
    mean_quick_time = sum(quick_times) / no_of_samples
    standard_deviation_bubble_time = (
        sum([(x - mean_bubble_time) ** 2 for x in bubble_times]) / no_of_samples
    )
    standard_deviation_insertion_time = (
        sum([(x - mean_insertion_time) ** 2 for x in insertion_times]) / no_of_samples
    )
    standard_deviation_quick_time = (
        sum([(x - mean_quick_time) ** 2 for x in quick_times]) / no_of_samples
    )

    with open(f"106_raport_{datetime.date.today()}.txt", "w") as f:
        f.write("RAPORT ALGORYTMOW SORTOWANIA\n\n")
        f.write(
            f"Bubble sort: -- {no_of_samples} -- {mean_bubble_time}s -- {standard_deviation_bubble_time}\n"
        )
        f.write(
            f"Insertion sort: -- {no_of_samples} -- {mean_insertion_time}s -- {standard_deviation_insertion_time}\n"
        )
        f.write(
            f"Quick sort: -- {no_of_samples} -- {mean_quick_time}s -- {standard_deviation_quick_time}\n"
        )
    return


sort_statistics()
