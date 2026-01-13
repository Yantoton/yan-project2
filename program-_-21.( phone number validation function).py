def phone_number():
    count = 0
    while  count <= 11:
        number = input("Enter your valid phone number:")
        if len(number) != 11:
            print(f"Faild:{number} this is not a valid phone number:")

        else:
            print(f"Success:{number} we are trying to contract:{number}")
            count += 1
            break

phone_number()
