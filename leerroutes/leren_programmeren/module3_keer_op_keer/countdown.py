
from multiprocessing import Event
import time

while True:
    try:
       cd = int(input("Hoelang moet de countdown zijn?"))
       break
    except:
        print("Voer een geldig aantal seconden in!")

for i in range(cd):
    if (cd - 1):
        Event().wait(1)
    print(str(cd - i), "Seconds")
    

Event().wait(1)
print("Launching!")




