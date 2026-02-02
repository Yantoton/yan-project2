keys(), values(), items() - View data

python_basic = {
    "variables" : "2,hello,2.0",
    "data_type" : "str,int,float,complex,bool",
    "conditionals" : "if,elif,else",
    "loops" : "for,while",
    "logicals" : "and,or,not",
    "operators" : "+,-,*,/,<,>,==,!=,<=,>=",
    " function" : "def():"

}
python_basic.update({"list":"[,,,]","tuple":"(,,,)","set":"{,,,}","dictionary":"{"":""}"}) 

for key,value in python_basic.items(): #These methods are very useful for running loops.
    print(key,":",value)
