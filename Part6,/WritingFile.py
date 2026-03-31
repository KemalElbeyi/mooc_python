while True:
    choice = int(input("1 - add an entry, 2 - read entries, 0 - quit: "))
    if choice == 0:
        break
    elif choice == 1:
        with open("../Ztext2.txt", "a") as new_files:
            sentence = input("Diary Entry: ")
            new_files.write("\n"+sentence)
        print("Diary saved")
    elif choice == 2:
        with open("../Ztext2.txt") as new_files:
            for line in new_files:
                print(line)

