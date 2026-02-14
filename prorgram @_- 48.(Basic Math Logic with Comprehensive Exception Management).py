try:
    num = float(input("enter a number:"))
    if num > 1:
        result = num + num

        print(f"let's see the result:{result}")

    else:

        print("num is 1 or less ,program_crash(Logic)")

except ValueError:

    print(f"Invalid_Input\nThe_{ValueError}_String_Is_Not_Definded\nEnter_Only_(Integer_ OR _Float)\nPlease_Try_Again")
except Exception as error :

    print(f"This_Is_A_Unexpected_Error:{error}".format(error=repr(error)))
else:

    print("Hello Darkness @_- the  calculation complete")
finally:

    print("Exit_The_Program")
