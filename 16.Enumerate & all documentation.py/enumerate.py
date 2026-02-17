my_enum=["Y","A","N"," ","T","O","T","O","N"]

for index,my_enu in enumerate(my_enum,start=0):
   print(index,my_enum[index])
   if my_enu == " ":
       print("space")

name = "Yan Toton"
for index,name in enumerate(name,start=0):
    print(f"{index},{name}")
