def average(*num):
    sum = 0
    for n in num:
        sum += n
    print("average is =:", sum/len(num))
average(5,6,7,1)
