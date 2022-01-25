lista = []
lista.append("test")
lista.append(1)
lista.append('c')
lista2 = []
lista2.append(1)
lista2.append("test")
lista2.append('c')
for i in range(len(lista)):
    print(lista[i] == lista2[i])
