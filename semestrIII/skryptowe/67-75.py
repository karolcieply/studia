import random
'''
#67
imie = input("podaj imie: ")
nazwisko = input("podaj nazwisko: ")
print(f"{imie} {nazwisko}")

#68
l1 = float(input("podaj liczbe 1: "))
l2 = float(input("podaj liczbe 2: "))
print(f"suma {l1+l2}")
#69
inside = 0
noToGenerate=10000
for i in range(noToGenerate):
    x, y = random.uniform(0,1), random.uniform(0,1)
    if x*x+y*y<=1:
        inside+=1
print(f"Przyblizenie pi: {4*inside/noToGenerate}")

'''
#70
print((-23)**(1/2))
'''
#71
wynik = 31%3
wynik *= wynik+3
print(wynik)


#72
print("".join([f"{round(-0.7*2.71828+4.07, 5)}@" for n in range(10)]))

#73
lista = []
lista.append("test")
lista.append(1)
lista.append('c')
print(lista)
#74
lista2 = []
lista2.append(1)
lista2.append("test")
lista2.append('c')
for i in lista:
    print(i)
#75
for i in range(len(lista)):
    print(lista[i]==lista2[i])

'''