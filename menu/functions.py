ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[2;0H\u001B[2"
SMILE_COLOR = u"\u001B[31m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"
from tt1 import lists
import time

def smile_print(position):
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    sp = " " * position
    print(SMILE_COLOR, end="")
    print(sp + "  ___  ")
    print(sp + " /   \ ")
    print(sp + "| ^ ^ |")
    print(sp + " \ U / ")
    print(sp + "  ‾‾‾  ")
    print(sp + "       ")
    print(RESET_COLOR)

def smile():
  start = 0
  distance = 30 
  step = 1

  for position in range(start, distance, step):
      smile_print(position)  
      time.sleep(.1)

def diamond():
  sp1 = " " * 4
  sp2 = " " * 2
  print(sp1 + "↑" + sp1)
  print(sp2 + "↑   ↑" + sp2)
  print("←       →")
  print(sp2 + "↓   ↓" + sp2)
  print(sp1 + "↓" + sp1)


def numberSwapper():
  age1 = input('Enter 1st Number: ')
  age2 = input('Enter 2nd Number: ')
  temp = age1
  age1 = age2
  age2 = temp
  print(age1, age2)

def lessNumSwap():
  age1 = input('Enter 1st Number: ')
  age2 = input('Enter 2nd Number: ')
  if age2 > age1:
    print(age1, age2)
  else:
    print(age2, age1)

# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders

# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [
    ["Animation", smile],
    ["Diamond", diamond],
    ["List Printer", lists.tester],
    ["Fibonacci", lists.fibonacci]
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Swapping", numberSwapper],
    ["Smaller # 1st", lessNumSwap],
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"



# def patterns_submenuc
# using patterns_sub_menu list:
# patterns_submenuc works similarly to menuc

# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Swap Menu", submenu])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu():
    title = "Swap Submenu" + banner
    buildMenu(title, sub_menu)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()