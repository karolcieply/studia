import random
inside = 0
noToGenerate = 10000
for i in range(noToGenerate):
    x, y = random.uniform(0, 1), random.uniform(0, 1)
    if x*x+y*y <= 1:
        inside += 1
print(f"Przyblizenie pi: {4*inside/noToGenerate}")
