from mainloop import mainloop
from print_winner import print_winner as pw

arr = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def main(arr):
    index = 0
    pw(mainloop(arr, index))

if __name__ == "__main__":
    try:
        main(arr)
    except KeyboardInterrupt:
        print("Error!, Try again later")

