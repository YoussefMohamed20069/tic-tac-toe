from check_win import check_win as cw
from print_winner import print_winner as pw

def mainloop(arr, index):

    prev_step = "X"

    winner = None

    while index < 9:
        print(arr[0] + " | " + arr[1] + " | " + arr[2])
        print("---------")
        print(arr[3] + " | " + arr[4] + " | " + arr[5])
        print("---------")
        print(arr[6] + " | " + arr[7] + " | " + arr[8])

        if winner != None:
            break

        try:
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
                return winner

            index += 1
            

        except IndexError:
            print("You Must Put A valid Index")
            mainloop(arr, index)



