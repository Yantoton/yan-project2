balance = 0

def check_balance():
    global balance
    print(f"\nYour Current Account Balance Is:{balance}")

def deposite_balance():
    global balance
    amount = int(input("Enter The Amount To (Deposite):"))
    if amount > 0:
        balance += amount
        print(f"\n{amount} Your Balance Deposite Successfully:Current Balance :{balance}")
    else:
        print(f"\nInvalid Deposite Amount Must Be Greater Than 0 ")

def withdraw_balance():
    global balance
    amount = int(input("Enter The Amount To (Withdraw):"))
    if amount <= balance and amount > 0:
        balance  -= amount
        print(f"\n{amount} Your Balance Withdraw Successfulluy:Current Balance:{balance}")
    elif amount > balance:
        print(f"\nInsufficient Balance")
    else:
        print(f"\nInvalid Withdraw Amount Must Be Greater Than )")

def exit_program():
    print("Exiting Program")

if __name__ == "__main__":
    print("Welcome To < P.T.M > Online Banking")


    program_menu = {
        1:"check_balance",
        2:"deposite_balance",
        3:"withdraw_balance",
        4:"exit_program",
    }

    while True:
        print("\n$_* Choose Your Option T_T")
        for key,value in program_menu.items():
            print(f"{key} : {value}")

        try:
            option = int(input("Type Your Option Here :"))
            if option == 1:
                check_balance()
            elif option == 2:
                deposite_balance()
            elif option == 3:
                withdraw_balance()
            elif option == 4:
                exit_program()
                break
            else:
                print("\nInvalid Option Between 1 - 4")
        except ValueError:
            print(f"\nInvalid_Input__ValueError__You Can Enter Only Integer,Not String Stupid ")

        else:
            print("\nThanks For Trusting Us")

        finally:
            print("\nProgram End Successfully")
