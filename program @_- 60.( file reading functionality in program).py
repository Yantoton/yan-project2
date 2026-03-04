with open("kaka.txt", 'r') as f:
    file_size = 19

    while True:
        read = f.read(file_size)

        if not read:
            print("\n___Stop_File_Reading___")
            break

        print(f"___Start_File_Reading___:'{read}'")

