while True:
    play_game =input("which type of game do you want? play:")

    match play_game:

        case _ if play_game =="fortnite":

            print("you need 1 controller to play the fortnite game")
        case _ if play_game =="mortal kombat":

            print("you need 2 controller to play the mortal kombat game")
        case _ if play_game == "fifa":

            print("you need 4 controller to play the Fifa game")
        case _:

            print(play_game)
