import menuy  # abstracted files in local directory
import loopy
import classy
from mody import advy  # abstracted files in a folder (aka module)
from mody import questy
from wipy import termy
from wipy import biny
from wipy import funcy

# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function refereces will be executed directly file.function()
main_menu = [
    ["Stringy", "stringy.py"],
    ["Numby", "numby.py"],
    ["Listy", "listy.py"],
    ["Loopy", loopy.main],
    ["Classy", classy.main]
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Random", "wipy/randomy.py"],
    ["Termy", termy.main],
    ["Biny", biny.main],
    ["Pre-Funcy", "wipy/prefuncy.py"],
    ["Funcy", funcy.ship],
    ["Advy", advy.main]
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Submenu", submenu])
    menuy.menu(title, menu_list)


# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu():
    title = "Function Submenu" + banner
    menuy.menu(title, sub_menu)


# def menuc
# using main_menu list:
# 1. custom title is created for menu
# 2  main menu and submenu references are created [Prompts, Actions]
# 3. menu_list is sent as parameter to questy.Menus class that creates an object that will be used to support menu control
# 4  object (m.) has method (menu()) that support menu control
def menuc():
    title = "Class Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Submenu", submenuc])
    m = questy.Menu(title, menu_list)
    m.menu()  # method and data reside in object


# def submenuc
# using main_menu list:
# submenuc works similarly to menuc
def submenuc():
    title = "Class Submenu" + banner
    m = questy.Menu(title, sub_menu)
    m.menu()


# def shell
# using main_menu list and sub_menu list
# using class questy.Prompts, a parent to questy.Menus creates an object that will be used to support shell style Prompts
# object (p.) illustrates usage of setter, shell, and getter methods
def shell():
    menu_list = main_menu + sub_menu
    p = questy.Prompts(menu_list)
    p.set_recurse(True)  # change data after object is created
    p.shell()
    print("Last Choice: ", p.get_choice())  # obtaining data after shell has exited


# this code is activated when file is executed directly
if __name__ == "__main__":
    menu()
    # menuc()
    # shell()
