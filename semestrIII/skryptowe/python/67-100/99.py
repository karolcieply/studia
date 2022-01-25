x = int(input("Podaj x: "))
y = int(input("Podaj y: "))
for i in range(x,y,1):
    if i % 4 == 0:
        print("Rok",i,"jest przestepny.")