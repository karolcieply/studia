import re
import datetime as datetime
'''
100
plec=["K","M"]
kolor=["bialy","czarny","zielony","czerwony","niebieski"]
rozmiar=["XL","L","M","S"]
with open('100.txt','w') as f:
    for i in plec:
        for j in kolor:
            for k in rozmiar:
                f.write(i+" "+j+" "+k+"\n")
101
wynik =1
for i in range(1,int(input("liczbe daj"))+1):
    wynik*=i
print(wynik)
102
def silnia(n):
    return n* silnia(n-1) if n>1 else 1
print(silnia(5))
print()

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        return qsort([x for x in arr[1:] if x < arr[0]])\
        + [arr[0]]\
        + qsort([x for x in arr[1:] if x >= arr[0]])
105
'''
arr = [1,2,3,4]
print(sum(arr)/len(arr))
print(min(arr))
print(max(arr))

print(datetime.time())