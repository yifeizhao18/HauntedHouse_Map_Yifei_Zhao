###############################################################################
# Title: Data Structures: RPG - Map

# Class: Computer Science 30 P1 S2                                                                                                                   
# Date: March 13, 2023

# Coder's Name: Yifei Zhao                                                                                                            
# Version: 001                                                                                        
###############################################################################
"""
This program creates a map. 
The user should not be able to walk off the map.
When the user is in a room, there will be a message printed to the console. 
The user will be able to choose which direction to go. 
"""
# Global Variables & Imports
import sys
row = 2
col = 2


# Functions
HauntedMansion = [
  ["Grand Ball Room", "Master Bedroom", "Bathroom", "Master Bedroom"],
  ["Closet", "Master Bedroom", "Rooftop", "Closet"],
  ["Grand Ball Room", "Bathroom", "Entrance", "Bathroom"],
  ["Master Bedroom", "Closet", "Rooftop", "Bathroom"],
  ["Rooftop", "Master Bedroom", "Grand Ball Room", "Exit"]
]

actionChoice = ["walk"]

directions = ["South", "North", "East", "West"]

welcomeMessage = ("Welcome To The Haunted House! You are currently at the Entrance. ")
askDirection = ("Do you want to go South, North, East, or West now? ")
answer = ("Sounds good! ")
action = ("What movement would you like to do? The only option in this room is walk. ")
walk = ("Walking! ")
ballroomMessage = ("You are currently in the Grand Ball Room. ")
closetMessage = ("You are currently in the Closet. ")
bedroomMessage = ("You are currently in the Master Bedroom. ")
rooftopMessage = ("You are currently at the Rooftop of this mansion. ")
bathroomMessage = ("You are currently in the Bathroom. The room of slaughter. ")
wrongMessage = ("Sorry, you cannot move in that direction. Please choose another direction. ")
wrongSpelling = ("Please only answer yes or no. No capital letters. ")
endingMessage = ("Thank you for playing. Bye! ")

def movements():
  global row, col
  movementChoice = (input(askDirection))
  print('\n')
  print(answer)
  print('\n')
  if movementChoice == "North":
    if row == 0:
      print("You have ran into a wall. ")
      print('\n')
      print("Please type in another direction. ")
    else:
      row -= 1
  elif movementChoice == "South":
    if row == 3:
      print("You have ran into a wall. ")
      print('\n')
      print("Please type in another direction. ")
    else:
      row += 1
  elif movementChoice == "West":
    if col == 0:
      print("You have ran into a wall. ")
      print('\n')
      print("Please type in another direction. ")
    else:
      col -= 1
  elif movementChoice == "East": 
    if col == 3:
      print("You have ran into a wall. ")
      print('\n')
      print("Please type in another direction. ")
    else: 
      col += 1
  else:
    print(wrongMessage)

def mainChoice():
  actionChoice = (input(action))
  print('\n')
  if actionChoice == "walk":
    print(walk)
  else:
    print("walk is the only option right now! No capital letters!")
    print('\n')
    input(action)
  print('\n')
  quitOption = input("Do you still want to play? ")
  print('\n')
  if quitOption == "yes":
    movements()
    print('\n')
  elif quitOption == "no":
    print(endingMessage)
    sys.exit() 
  else:
    print(wrongSpelling)

    
  
# Main
while True: 
  current_location = HauntedMansion[row][col]
  if current_location == "Entrance":
    print(welcomeMessage)
    print('\n')
  elif current_location == "Grand Ball Room":
    print(ballroomMessage)
    print('\n')
  elif current_location == "Closet":
    print(closetMessage)
    print('\n')
  elif current_location == "Master Bedroom":
    print(bedroomMessage)
    print('\n')
  elif current_location == "Rooftop":
    print(rooftopMessage)
    print('\n')
  elif current_location == "Bathroom":
    print(bathroomMessage)
    print('\n')
  elif current_location == "Exit":
    print(endingMessage)
    break
  else:
    print(wrongMessage)
    print('\n')
  # Main Menu
  mainChoice()