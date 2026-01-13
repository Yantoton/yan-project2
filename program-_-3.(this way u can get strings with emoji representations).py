tell1: str = 'Software engineering is my passion '

enginer = (tell1.maketrans('S','💻'))
print(tell1.translate(enginer))

tell2 =" farming is my dream busniess"

farm =(tell2.maketrans('f','🐮'))
print(tell2.translate(farm))

tell3 ="i want to be a jdm Car collector"

car =(tell3.maketrans('C','🚗'))
print(tell3.translate(car))
