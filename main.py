def main():
    arr = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

    i = 0

    prev_step = "X"

    while i < 9:
        print(arr[0] + " | " + arr[1] + " | " + arr[2])
        print("---------")
        print(arr[3] + " | " + arr[4] + " | " + arr[5])
        print("---------")
        print(arr[6] + " | " + arr[7] + " | " + arr[8])

        if prev_step == "X":
            prev_step = "O"
            position = int(input(f"Put the Position you want to put {prev_step} in [1, 9]: "))
            arr[position - 1] = prev_step
        elif prev_step == "O":
            prev_step = "X"
            position = int(input(f"Put the Position you want to put {prev_step} in [1, 9]: "))
            arr[position - 1] = prev_step

        i += 1

main()

