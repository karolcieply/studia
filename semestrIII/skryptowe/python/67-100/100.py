plec = ["K", "M"]
kolor = ["bialy", "czarny", "zielony", "czerwony", "niebieski"]
rozmiar = ["XL", "L", "M", "S"]
with open('100.txt', 'w') as f:
    for i in plec:
        for j in kolor:
            for k in rozmiar:
                f.write(i+" "+j+" "+k+"\n")
