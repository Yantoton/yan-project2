while True:
    leap_year= int(input("Enter the leap year:"))

    if leap_year % 400 == 0 and  leap_year % 100 == 0:
        print(f"{leap_year} This is a leap year")

    elif leap_year % 4 == 0  and leap_year % 100 != 0:
        print(f"{leap_year} This is a leap year")

    else:
        print(f"{leap_year} This is not a leap year")
