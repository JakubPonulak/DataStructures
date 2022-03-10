# advy.py - adventure starter
from mody import questy
    
def beach():
  print("beach function")

def mountain():
  print("mountain function")

def lake():
  print("lake function")

def main():
  banner = "You are on a treasure adventure... \nWhere do you want to start your journey?"

  options = [
    ["At the Beach?", beach],
    ["On top of the Mountains?", mountain],
    ["Navigating a lake?", lake]
  ]
  q = questy.Question(banner, options)
  q.question()
  print("Last Choice: ", q.get_choice())