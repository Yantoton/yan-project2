import sys
sys.setrecursionlimit(8601)
print(sys.getrecursionlimit())
x = 0
def gal():
    global x
    x += 1
    print("I am going to sleep",x)
    gal()

gal()
