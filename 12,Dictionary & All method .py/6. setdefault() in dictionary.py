python_basic = {
    "variables" : "2,hello,2.0",
    "data_type" : "str,int,float,complex,bool",
    "conditionals" : "if,elif,else",
    "loops" : "for,while",
    "logicals" : "and,or,not",
    "operators" : "+,-,*,/,<,>,==,!=,<=,>=",
    " function" : "def():"

}
python_basic ["list"] = "[,,,]"
python_basic.setdefault("tuple","(,,,)") # touple No, so it will be added.
python_basic.setdefault("loop","for,while") # loopYes, so it won't change.
