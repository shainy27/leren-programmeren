birds = [{'name':'mus','key':'m','count':0},
          {'name':'duif','key':'d','count':0},
          {'name':'koolmees','key':'k','count':0},
          {'name':'kraai','key':'i','count':0},
          ]

def get_bird_by_key(birds:list,key:str):
    for bird in birds:
        if bird['key'] == key:
            return bird
    return None

# 1) print all birds with key and name
print('Birds:')
for bird in birds:
    print(f"- {bird['key']}: {bird['name']}")

# 2) define function get_bird_by_key(birds: list, key:str) returns bird or None

# 3) repeat until given '.'
while True:
    key = input("Enter bird key (or '.' to exit): ")
    if key == '.':
        break
    try:
        amount = int(key[1:])
    except:
        amount = 1
    key = key[0:1]
    bird = get_bird_by_key(birds, key)
    if bird:
        bird['count'] += amount

   
# 4) Print the list of birds
print("\n")

for bird in birds:
    print(f"{bird['name']}: {bird['count']}")
    
print("\n")

# 5) percentage
total = 0
for bird in birds:
    total += bird['count']

    
for bird in birds:
    print(f"{bird['name']}: {round(bird['count'] / total * 100)}%")





