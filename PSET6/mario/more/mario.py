from cs50 import get_int

# ask for height between 1 and 8
while True:
    height = get_int("Height: ")
    if height in range(1, 9):
        y = 0
        for y in range(height):
            length = 0
            spaces = 0
            x = 0
            for spaces in range(height - y - 1):
                print(" ", end="")
                spaces += 1
            for length in range(y + 1):
                print("#", end="")
                length += 1
            print("  ", end="")
            for x in range(y + 1):
                print("#", end="")
            print()
            y += 1
        exit(0)