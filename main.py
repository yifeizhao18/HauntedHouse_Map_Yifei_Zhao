###############################################################################################
# Title: Data Structures: RPG - Map

# Class: Computer Science 30 P1 S2                                                                                                                   
# Date: March 13, 2023

# Coder's Name: Yifei Zhao                                                                                                            
# Version: 001                                                                                        
###############################################################################################
"""
This program creates a map. 
"""
# Global Variables & Imports
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
endingMessage = ("Thank you for playing. Bye! ")

def movements():
  global row, col
  movementChoice = (input(askDirection))
  print('\n')
  print(answer)
  if movementChoice == "South":
    row += 1
  elif movementChoice == "North":
    row -= 1
  elif movementChoice == "East":
    col += 1
  elif movementChoice == "West":
    col -= 1
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
  movements()
  print('\n')
  
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