from check_win import check_win as cw
from print_winner import print_winner as pw

def mainloop():
    arr = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    i = 0

    prev_step = "X"

    game_winner = ""

    while i < 9:
        print(arr[0] + " | " + arr[1] + " | " + arr[2])
        print("---------")
        print(arr[3] + " | " + arr[4] + " | " + arr[5])
        print("---------")
        print(arr[6] + " | " + arr[7] + " | " + arr[8])

        if game_winner != "":
            break

        if prev_step == "X":
            prev_step = "O"
            position = int(input(f"Put the Position you want to put {prev_step} in [1, 9]: ")) - 1
            while arr[position] == "X" or arr[position] == "O":
                print("Sorry the Place is taken")
                position = int(input(f"Put the Position you want ot put {prev_step} in [1, 9]: ")) - 1
            arr[position] = prev_step
        elif prev_step == "O":
            prev_step = "X"
            position = int(input(f"Put the Position you want to put {prev_step} in [1, 9]: ")) - 1
            while arr[position] == "X" or arr[position] == "O":
                print("Sorry the Place is taken")
                position = int(input(f"Put the Position you want to put {prev_step} in [1, 9]: ")) - 1
            arr[position] = prev_step

        winner = cw(arr)

        if winner != None:
            game_winner = winner

        i += 1

    return game_winner


