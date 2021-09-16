def check_win(arr):
    players = ["X", "O"]
    if arr[0] == arr[1] == arr[2] and arr[0] in players:
        return arr[0]
    elif arr[0] == arr[3] == arr[6] and arr[0] in players:
        return arr[0]
    elif arr[0] == arr[4] == arr[8] and arr[0] in players:
        return arr[0]


