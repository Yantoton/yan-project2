price = int(input("Enter your price:"))
tk = f"This way you can use f-string:the price is only {price:.2f} Taka!!"
print(tk)

print(price.format(price=20000))

rate = "way-2 you can also use f-string like this :the rate is {rate:.2f} only"
print(rate.format(rate=24223))
