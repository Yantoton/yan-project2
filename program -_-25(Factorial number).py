def cal_fact(number):
    factorial = 1
    for x in range(1,number+1):
        factorial *= x
        print(factorial)
print()
cal_fact(7)

