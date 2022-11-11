
verandering = 0
i = 50
som = i + verandering

while i <= 2200:
    if i >= 1100:
        break
    print(i)
    verandering = verandering + 1
    i = som + i + verandering
print("einde")