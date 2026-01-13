game_price =int(input("how many game you like to purchase?\nour starting price is 55:"))
budget = int(input("Enter your Budget here:"))

if budget - game_price >= 70:
    print("add to cart for purchase ")
elif budget - game_price <= 55:
    if budget - game_price < 50:
        print("sorry you can't get any game in this price")
    else:
        print("you can purchase 1 game")
else:
    print("come again")
