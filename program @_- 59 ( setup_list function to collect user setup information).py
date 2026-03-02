def setup_list():
     try:
        monitor = input("what monitor brand u are using :")
        print(f"In My Set_up I am using\\ {monitor}\\ monitor")

        game_device = input("Which device you are using for gaming :")
        print(f"In My Set_up I am using\\ {game_device}\\ For Gaming!")

        work_device = input("Which device you are using for working :")
        print(f"In My Set_up I am using \\{work_device}\\ For Working!")

        accessories = input("Which Accessories You Using In This Set_up :")
        print(f" I am using these items in My Set_up\\ {accessories}\\")

        with open("kaka.txt","w") as f:
          f.write(f"\nMonitor brand are using:{monitor}"
                  f"\nGaming device are using:{game_device}"
                  f"\nWorking device are using:{work_device}"
                  f"\nAccessories are using:{accessories}")
     except FileNotFoundError:
         print("Invalid_File_Error\nCannot define the file")
     except Exception as e:
         print(f"Not_Valid_Value_Error\n Enter the Valid Value{e}")
     else:
         print("\nO_> File Writing or Append Successfully...!")

     finally:
         print( """
                   _______________________________________
                  |                                       |
                  |                                       |
                  | <_> <.Program End.> *_* .>>> Here...! |
                  |                                       |
                  |_______________________________________| """)


if __name__ == "__main__":
 setup_list()
