n = input("enter a number?")
if int(n) %2 != 0:
    print("Weird")
elif int(n) %2 == 0 & int(n) >=2 & int(n)<=5:
    print("Not Weird")
elif int(n) %2 == 0 & int(n) >=6 & int(n)<=20:
    print("Weird")
elif int(n)>20:
    print("Not Weird")
else:
    print('Good bye')
print("hi")
