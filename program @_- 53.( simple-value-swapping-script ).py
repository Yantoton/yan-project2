x_value = int(input("Enter x_value here!..:"))
y_value = int(input("Enter y_value here!..:"))


third_value = x_value
print("The value of third_value is:",third_value)
x_value = y_value
print("The Value of x_num is:",x_value)
y_value = third_value
print("The value of y_num is:",y_value)

print(f"The value is swap successfully") if y_value == third_value  else print(f"The value not swap successfully")
