
from multiprocessing import Event

num = 30

while num >=0 and num <=30:
    print(f"{num}seconden")
    Event().wait(1)
    num = num - 1

print("Launching!")