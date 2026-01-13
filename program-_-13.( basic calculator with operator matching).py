operator = input("Enter the operator here:")
num1 = int(input("Enter the 1st number here:"))
num2 = int(input("Enter the 2nd number here:"))

match operator:
    case "+":

        print(f"{num1} + {num2} = {num1+num2}")

    case "-":

        print(f"{num1} - {num2} = {num1-num2}")

    case "*":
        print(f"{num1} * {num2} = {num1*num2}")
    case "**":

        print(f"{num1} ** {num2} = {num1**num2}")

    case "/":

        print(f"{num1} / {num2} = {num1/num2}")

    case "//":

        print(f"{num1} // {num2} = {num1//num2}")

    case "%":

        print(f"{num1} % {num2} = {num1%num2}")

    case _:

        print(f"hy dude {operator} is not defined")
