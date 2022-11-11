
num = 0

while True:
    vraag = input("?").lower()
    if vraag != "quit":
        num = num + 1
    else:
        print(f"De vraag werd {num} keer gesteld")
        exit()
    
        
