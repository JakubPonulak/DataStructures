{% include navigation.html %}

# Data Structures Project Documentation

## Tech Requirement Documentation:

In order to meet the requirements set for N@TM, along with creating something that would be helpful for our website, so we created a calendar that makes use of our database. The idea is that administrators can create and update events, and students will be able to see those events and why day they are by clicking on the calendar. Something I had trouble with was looping through the database in JS. Eventually, after troubleshooting and testing, I realized that it was easiest for my to put the data in python lists and then looping through them via a Jinja for loop. We also created an authentication page that stops unauthorized users from user certain pages, such as our calendar. Overall our team was quite succesful with these additions, though there are some small features that we haven't implement. I think that our team could have been more focused in class, so I give us 4.5/5. I would give myself a 5/5, because I worked on the calendar in class, and spent a significant amount of time outside of class on it.

## Runtime Demo
<iframe frameborder="0" width="100%" height="800px" src="https://replit.com/@JakubPonulak/DataStructures?embed=true#index.html"></iframe>

<!-- ## Code Snippets
  
### Tech Talk 0 - Code

```   
# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
from menu import functions
import time

# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [
    ["Animation", functions.smile],
    ["Xmas Tree", functions.xmas_tree],
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Swapping", functions.numberSwapper],
    ["Smaller # 1st", functions.lessNumSwap],
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

```

### Tech Talk 1

```
    
# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "FirstName": "Jakub",  
               "LastName": "Ponulak",  
               "DOB": "March 25",  
               "Residence": "San Diego",  
               "Email": "jakub.ponulak@gmail.com",  
               "Owns_Cars":["1997 BMW M3","2005 Subaru Impreza","1999 Nissan GTR Skyline","1997 Toyota Supra", "1990 Lamborghini Countach"]  
              })

InfoDb.append({  
               "FirstName": "John",  
               "LastName": "Cena",  
               "DOB": "April 23",  
               "Residence": "Hollywood",  
               "Email": "johncena@gmail.com",  
               "Owns_Cars":["2022 Invisi-Mobile"]  
              }) 

InfoDb.append({  
               "FirstName": "Akhil",  
               "LastName": "Nandhukamar",  
               "DOB": "April 1",  
               "Residence": "San Diego",  
               "Email": "akhiln@gmail.com",  
               "Owns_Cars":["2005 Ferarri FXX", "2005 Honda CRV"]  
              })  

InfoDb.append({  
               "FirstName": "Elon",  
               "LastName": "Musk",  
               "DOB": "June 28",  
               "Residence": "Los Angeles",  
               "Email": "elonmusk@gmail.com",  
               "Owns_Cars":["2022 Tesla Model X", "Tesla Cybertruck"]  
              })  


# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Cars: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Owns_Cars"]))  # join allows printing a string list with separator
    print()

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
## hack 2b: def while_loop(0)
## hack 2c : def recursive_loop(0)

def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion

def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)

def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

# Factorial of a number using recursion
def recur_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n-1)

# this is test driver or code that plays when executed directly, versus import which will not run these statements
def tester1():
    num = int(input("Enter a number for factorial: "))
    # check if the number is negative
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    else:
        print("The factorial of", num, "is", recur_factorial(num))

# Hack 3: Fibonacci.  Write a recursive program to create a fibonacci sequence including error handling for invalid input
def fibonacci():
  num = int(input("Enter the length of your Fibonacci sequence: "))
  if num < 0:
    print("You cannot use a negative number")
  else:
    for i in range(num):
      print(recur_fibonacci(i))

def recur_fibonacci(n):
  if n <= 1:  
     return n  
  else:  
     return(recur_fibonacci(n-2) + recur_fibonacci(n-1)) 
  
``` -->

<br>

                   
## Key Learnings:

One of the most important things I learned while working on python data structures in perseverence. I often came across problems I didn't know how to solve, but instead of giving up or looking for an easy solution online, I kept trying and persevering until I was able to complete my task, while also learning and understanding what my code does / is supposed to do.

Another challange I faced was organizing all my files. I started this project without a clear goal/idea of how I would organize it, so I often found myself moving or rearanging files in between new assignments. Towards the end of these weeks I have been able to better organize my work/code, but in the future I will make sure to plan ahead and figure this out before I start a new project/assignment.

## Code / Runtime Links

[GitHub Repository](https://github.com/AkhilNandhakumar/Guython)

[Replit](https://replit.com/@JakubPonulak/DataStructures#main.py)
