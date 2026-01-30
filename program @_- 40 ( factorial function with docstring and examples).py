def factorial(n):
   """this function returns the factorial of number
   let's say n is an integer"""

   if n == 0 or n == 1:
    return 1
   else:
       return n * factorial (n-1)
print(factorial.__doc__)
print(factorial(6))
print(factorial(8))
