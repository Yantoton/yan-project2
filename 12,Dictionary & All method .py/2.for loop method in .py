#2 ways use for loop 
python_basic = {
    "variables" : "2,hello,2.0",
    "data_type" : "str,int,float,complex,bool",
    "conditionals" : "if,elif,else",
    "loops" : "for,while",
    "logicals" : "and,or,not",
    "operators" : "+,-,*,/,<,>,==,!=,<=,>=",
    " function" : "def():"

}
for python in python_basic:
    print(python,"<:>",python_basic[python]) #way 1 method 1: Direct Loop (Key Indexing)

for key,value in python_basic.items():
    print(key,":",value) # way 2: Using .items()
