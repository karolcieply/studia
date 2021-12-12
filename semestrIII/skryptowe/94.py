from math import *
import random
import numpy as np
#76
'''
a = [1,2,3] 
b = [4,5,6]
if(6 in a or 6 in b):
    print("jest")
else:
    print("nie ma")
#77
cos = int(input("wpisz liczbe"))
if cos > 0:
    print("liczba wieksza od 0")
elif cos < 0:
    print("liczba mniejsz od 0")
else:
    print("liczba rowna 0")

#78
uInput = "test"
while(uInput):
    uInput = input("podaj slowo: ")
    print(uInput)
#79
samo = ["a","e","i","o","u","y"]
uInput = input("podaj alfabet: ")
for i in uInput:
    if i in samo:
        print(i, end=",")
#80
try:
    uInput=int(input("podaj liczbe"))
except:
    print("podales nie liczbe")
userInput=np.array([])
#81
while (x:=input("podaj liczbe: "))!="exit":
    userInput=np.append(userInput, int(x))
print(np.average(userInput))
print(np.median(userInput))
#82
with open('plik.txt') as f:
    numbers = f.read().splitlines()
numbers = [int(i) for i in numbers]
print(np.average(numbers))
print(np.median(numbers))
#83
def fun():
    userInput = float(input("podaj cos"))
    print(userInput)
fun()
#84
def fun():
    userInput = input("podaj cos")
    if "." in userInput or "," in userInput:
        print("zmiennoprzecinkowa")
    else:
        print("calkowita")
fun()
#85
a = int(input('podaj a: '))
b = int(input('podaj b: '))
with open('plik.txt') as f:
    numbers = f.read().splitlines()
if a<0:
    a=0
if b > len(numbers)-1:
    b=len(numbers)-1
rand = random.randint(a,b)
with open("z85", "w") as f:
    f.write(str(rand))
    f.write("\n")
    f.write(numbers[rand])

#86
x = int(input("podaj liczbe"))
for i in range(7):
    for j in range(5):
        print(x,end="")
    print("")
    
#87
x = int(input("podaj liczbe"))
with open("z87", "w") as f:
    for i in range(7):
        for j in range(5):
            f.write(str(x))
        f.write("\n")
#88
a = int(input('podaj a: '))
b = int(input('podaj b: '))
for i in range(5):
    for j in range(5):
        print(str(random.randint(a,b))+" ",end="")
    print("")

#89
userInput = input("podaj slowo: ")
if list(userInput) == list(userInput)[::-1]:
    print("palindrom")
else:
    print("nie palindrom")
#90
silnia=1
for i in range(1, int(input("podaj liczbe: "))+1):
    silnia*=i
print(silnia)
#91
with open("z94r.txt", "r") as f:
    liczba = f.readline().splitlines()
liczba = int(liczba[0])
h = hex(liczba)
d = oct(liczba)
with open("z94", "w") as f:
    f.write(str(h))
    f.write("\n")
    f.write(str(d))
'''
#92
def silnia(n): return n*silnia(n-1) if n > 1 else 1
def a():
    alfa = radians(int(input("alfa: ")))
    beta = radians(int(input("beta: ")))
    print(sin(alfa)+sin(beta))
    print(2*sin(1/2*(alfa+beta))*cos(1/2*(alfa-beta)))
def b():
    x = int(input("x: "))
    n = int(input("n: "))
    result = 1+((n*x)/silnia(1))
    for i in range(2, 10):
        result+=((n*(n-i)*(x**i))/silnia(i))
    print((1+x)**n)
    print(result)

def c():
    a,b,c=int(input("a: ")),int(input("b: ")),int(input("c: "))
    print((-b+sqrt(b*b-4*a*c))/2*a)
def d():
    result = 1
    x = int(input("x: "))
    for i in range(1,20):
        result = result+ (x**i)/silnia(i)
    print(result)
    print(exp(x))


c()
#93
with open("wyjscie.txt", "r") as plik:
    a = plik.readline()
a = list(a)
print(a)
licznik=0
for element in a:
    if not element.isnumeric():
        print(element)
        licznik+=1

print("Liczba wystapien: ", licznik)