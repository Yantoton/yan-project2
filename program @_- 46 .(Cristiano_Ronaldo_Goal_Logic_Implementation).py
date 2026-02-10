 try:
 cr7 = int(input("Enter the goal:"))
 print(" yes Ronaldo give 2 goal") if cr7 == 2 else print(f"Ronaldo assist him to give {cr7} goal")

except ValueError:
    print("Invalid _Input!>... _Please_ Enter_A__Valid _Integer_Number\nThis_Is_Not_A_String_Input_Idiot_ValueError_You_Can_Enter_1_Or_2/Program_Crash_Handled")
else:
    print("I never tried to hide the fact that my only goal is to be the best")
finally:
    print("Siuuuuu.......!")
