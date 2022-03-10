import time, sys, random

"""
http://ascii-table.com/ansi-escape-sequences.php
Console control:
Clear Screen: \u001b[2J"
Home Cursor: \u001b[0,0H"
Up: \u001b[{n}A
Down: \u001b[{n}B
Right: \u001b[{n}C
Left: \u001b[{n}D

8 Colors:
Reset: \u001b[0m  #default
Black: \u001b[30m
Red: \u001b[31m
Green: \u001b[32m
Yellow: \u001b[33m
Blue: \u001b[34m
Magenta: \u001b[35m
Cyan: \u001b[36m
White: \u001b[37m

8 Backgrounds:
Black: \u001b[40m
Red: \u001b[41m
Green: \u001b[42m
Yellow: \u001b[43m
Blue: \u001b[44m
Magenta: \u001b[45m
Cyan: \u001b[46m
White: \u001b[47m
"""

BUILDER_ESCAPE = "\033["
SAVE_CURSOR = "\033[s"
RESTORE_CURSOR = "\033[u"

ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H"
ANSI_CURSOR_UP = u"\u001B[1A"
ANSI_CURSOR_DOWN = u"\u001B[1B"
ANSI_CURSOR_FORWARD = u"\u001B[1C"
ANSI_CURSOR_BACKWARD = u"\u001B[1D"
ANSI_END_OF_LINE = u"\u001B[1000C"  # big number
ANSI_BEGINNING_OF_LINE = u"\u001B[1000D"  # big number

ANSI_RESET = u"\u001B[0m"
ANSI_BLACK = u"\u001B[30m"
ANSI_RED = u"\u001B[31m"
ANSI_GREEN = u"\u001B[32m"
ANSI_YELLOW = u"\u001B[33m"
ANSI_BLUE = u"\u001B[34m"
ANSI_PURPLE = u"\u001B[35m"
ANSI_CYAN = u"\u001B[36m"
ANSI_WHITE = u"\u001B[37m"

ANSI_BLACK_BACK = u"\u001B[40m"
ANSI_RED_BACK = u"\u001B[41m"
ANSI_GREEN_BACK = u"\u001B[42m"
ANSI_YELLOW_BACK = u"\u001B[43m"
ANSI_BLUE_BACK = u"\u001B[44m"
ANSI_PURPLE_BACK = u"\u001B[45m"
ANSI_CYAN_BACK = u"\u001B[46m"
ANSI_WHITE_BACK = u"\u001B[47m"


def colors():
    # color options
    print(ANSI_BLACK, ANSI_WHITE_BACK, "Black", ANSI_RESET)
    print(ANSI_GREEN, "Green")
    print(ANSI_YELLOW, "Yellow")
    print(ANSI_BLUE, "Blue")
    print(ANSI_PURPLE, "Purple")
    print(ANSI_CYAN, "Cyan")
    print(ANSI_WHITE, "White")

    # position print: print("\033[4;15HHello")
    # variable used to show posible adaptation to reusable function
    print(SAVE_CURSOR)
    row = str(6)
    col = str(20)
    message_move = "r" + row + ";" + "c" + col
    cursor_move = BUILDER_ESCAPE + row + ";" + col + "H"
    print(cursor_move, message_move)
    print(RESTORE_CURSOR)


def load():
    print("Loading...")
    for i in range(0, 100):
        time.sleep(0.1)
        width = (i + 1) / 4
        bar = "[" + "#" * int(width) + " " * int(25 - width) + "]"
        sys.stdout.write(ANSI_BEGINNING_OF_LINE)
        print(bar, end='')
        sys.stdout.flush()
    print()


def loading(count):
    all_progress = [0] * count
    sys.stdout.write("\n" * count)  # Make sure we have space to draw the bars
    while any(x < 100 for x in all_progress):
        time.sleep(0.01)
        # Randomly increment one of our progress values
        unfinished = [(i, v) for (i, v) in enumerate(all_progress) if v < 100]
        index, _ = random.choice(unfinished)
        all_progress[index] += 1

        # Draw the progress bars
        sys.stdout.write(u"\u001b[1000D")  # Move left
        sys.stdout.write(u"\u001b[" + str(count) + "A")  # Move up
        for progress in all_progress:
            width = progress / 4
            print("[" + "#" * int(width) + " " * int(25 - width) + "]")


def clear():
    print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)


def main():
    clear()
    colors()
    load()
    loading(10)
