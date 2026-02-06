
print("Welcome To Game_Bazzar")
while True:
    print("Sir we have all of these items in our shop")

    items_name = {
        1 : "Gaming Pc",
        2 : "X_Box",
        3 : "Ps4",
        4 : "Nintendo Switch ",
        5 : "Steam Deck",
        6 : "Ps5",
        7 : "Gaming Laptop",
        8 : "Gaming Accessories"
    }
    for key, value in items_name.items():
        print(key,value)
    try:
         select_items=int(input(" Select your Gaming_weapon_(1:8)_:"))
         if select_items == 1:
             print("Ok sir you like to purchese gaming pc")

         elif select_items == 2:
             print("Ok sir you like to purchase X_Box")

         elif select_items == 3:
             print("Ok sir you like to purchase Ps4")

         elif select_items == 4:
             print("ok sir you like to purchase Nintendo Switch")

         elif select_items == 5:
             print("Ok sir you like to purchase Steam Deck")

         elif select_items == 6:
             print("Ok sir you like to purchase Ps5")

         elif select_items == 7:
             print("Ok sir you like to purchase Gaming laptop")

         elif select_items == 8:
             print("Ok sir you like to purchase Gaming Accessories")

         else:
             print("Sorry you have not selected any item")
         add_items = input("IF you want to purchase more Items_(yes / no):")
         if add_items == "yes":
             print("Sir you like add more items",select_items)
         elif add_items == "no":
             print("thank you sir have a nice gametrip & keep gaming")
             break
         else:
             print("Tell me Sir how can I help you")

    except ValueError:
        print(f"Invalid_Input\nThe_{ValueError}_String_Is_Not_Definded\nEnter_Only_Integer\nPlease_Try_Again")
    except ExceptionError as error:
     print(f"This_Is_A_Unexpected_:{error}".format(error=repr(error)))
    else:
        print("Thank you Come again Game_Bazzar")
    finally:
        print("Follow Our Facebook & Youtube side")
