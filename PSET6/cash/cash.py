from cs50 import get_float

# Ask for how much change is owed
while True:
    owed = get_float("Change owed: ")
    owed = round(owed * 100)
    if owed > 0:
        coins = 0
        while owed >= 25:
            owed -= 25
            coins += 1
        while owed >= 10:
            owed -= 10
            coins += 1
        while owed >= 5:
            owed -= 5
            coins += 1
        while owed >= 1:
            owed -= 1
            coins += 1
        print(f"{coins}")
        exit(0)
