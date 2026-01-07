#NASTED LOOPS
for x in range (3): # OUTER LOOP
    for y in range (2): # INNER LOOP
        for z in range (2): # THIS IS ALSO INNER LOOP
         print(f'({x},{y},{z})')

cloths = ['shirt','pant','t_shirt']
sizes = ['L','M','S']
for cloth in cloths:
    for size in sizes:
        print(f"{cloth} - size {size}")

list1 = ["hy","hello",'hi']
names  = ["Rakib","Habib","Nafisa"]
for x in list1:
    for name in names:
        print(x,name)
        if x == "hi" and name == "Nafisa":
            print(f"{x} {name} sent me your programming presentation file")
            break
    print("out from inner loop")
print("out from outer loop")
