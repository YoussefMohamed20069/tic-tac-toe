from mainloop import mainloop
from print_winner import print_winner as pw

if __name__ == "__main__":
    try:
        pw(mainloop())
    except:
        print("Error!, Try again later")

