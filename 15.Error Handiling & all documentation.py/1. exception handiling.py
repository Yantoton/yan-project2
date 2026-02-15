try:
    a = int(input("enter a number:"))
    op= 10 /  a
except ZeroDivisionError:
    print("something went wrong\n  ZeroDivisionError\nDude you_can't divide by zero")
except ValueError:
    print("invalid input\n Enter only integers\ntry again")
else:
    print(f" is equal to {op}")
finally:
    print("finally this program is complete")
