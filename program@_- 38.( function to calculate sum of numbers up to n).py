def find_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum + find_sum(sum-1)

print(find_sum(5))
