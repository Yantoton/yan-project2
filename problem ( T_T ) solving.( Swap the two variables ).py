# Solution - 1 (Using third variable)
x_value = int(input("Enter x_value here!..:"))
y_value = int(input("Enter y_value here!..:"))


third_value = x_value
print("The valu of third_value is:",third_value)
x_value = y_value
print("The Value of x_num is:",x_value)
y_value = third_value
print("The value of y_num is:",y_value)

print(f"The value is swap sucessfully") if y_value == third_value  else print(f"The value not swap sucessfully")


# Solution - 2 ( With_out using third variable)


x_num = 122
y_num = 123

x,y = y_num, x_num
print("The value of x is:",x)
print("The value of y is:",y)
