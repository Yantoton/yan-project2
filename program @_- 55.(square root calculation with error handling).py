import math
try:
    num = int(input("Enter the root num:"))
    sq_root = math.sqrt(num)
    print(f"The square root of {num} is:{sq_root}")

except ValueError:
    print("...>>> Program crash_Invalid input..!.._\n/You did not enter a valid number\nThis_not a str input Enter the right value...>\nenter a valid Positive Integer number\n<.Try again.>")
else:
    print("<.Program run successfully.>{Let's exit the program}")
finally:
    print("Thank you for give us your valuable time\nusing this program")
