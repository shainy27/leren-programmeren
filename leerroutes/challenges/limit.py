limit = 0.3
factor1 = float(input("nummer"))
factor2 = float(input("nummer2"))
total = round(factor1 + factor2 ,1)

if total < limit or total == limit:
    print("ja")
else:
    print("ha")

print(total)