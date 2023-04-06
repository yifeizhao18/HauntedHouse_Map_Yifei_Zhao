###############################################################################
# Title: Data Structures: RPG - Modules

# Class: Computer Science 30 P1 S2                                                                                                                   
# Date: March 13, 2023

# Coder's Name: Yifei Zhao                                                                                                            
# Version: 003                                                                                        
###############################################################################
"""
This program creates a map. 
The user should not be able to walk off the map.
When the user is in a room, there will be a message printed to the console. 
The user will be able to choose which direction to go. 
Has empty lists that the user will be able to add items into it. 
"""
###############################################################################
# Global Variables & Imports
import sys
import map
import randomResult
row = 2
col = 2

# dictionary for actions 
actionChoice = {
  "walk" : {
    "message" : "Currently Walking Around!",
    "description" : "You will be able to walk around the room. "
  },
  "search" : {
    "message" : "Searching For Possible Keys!",
    "description" : "You will be able to search the room. "
  },
  "quit" : {
    "message" : "Thank you for playing. Bye!",
    "description" : "The game will stop. "
  },
  "inventory" : {
    "message" : "These are your current inventories. ",
    "description" : "If you do not see anything in it, that is because you have not found or collected anything yet. "
  }
}

# empty list for inventory, foods, medicines, and weapons
Inventory = []
Food = []
Medicine = []

# messages to be printed on the console 
askDirection = ("Do you want to go south, north, east, or west now? ")
answer = ("Sounds good! ")
action = ("What movement would you like to do? ")
wrongMessage = ("Sorry, you cannot move in that direction. Please choose another direction. No capital letters! ")
wrongSpelling = ("Please only answer yes or no. No capital letters. ")
endingMessage = ("Thank you for playing. Bye! ")
leaveMessage = ("Do you want to leave now? ")
congratsMessage = ("Congratulations! ")
collectMessage = ("Do you want to collect it? ")


def movements():
  """
  movement function that asks for the user input on directions.
  makes sure the user does not walk off of the map.
  """
  global row, col
  # asks for user input 
  while True:
    movementChoice = (input(askDirection))
    print('\n')
    print(answer)
    print('\n')
    # if the user put in North, do the following 
    if movementChoice == "north":
      # makes sure the user stays in the map
      if row == 0:
        print("You have ran into a wall. ")
        print('\n')
        print("Please type in another direction. ")
        print('\n')
      else:
        row -= 1
        break
    # if the user put in South, do the following
    elif movementChoice == "south":
      # makes sure the user stays in the map
      if row == 4:
        print("You have ran into a wall. ")
        print('\n')
        print("Please type in another direction. ")
        print('\n')
      else:
        row += 1
        break
    # if the user put in West, do the following
    elif movementChoice == "west":
      # makes sure the user stays in the map
      if col == 0:
        print("You have ran into a wall. ")
        print('\n')
        print("Please type in another direction. ")
        print('\n')
      else:
        col -= 1
        break
    # if the user put in East, do the following
    elif movementChoice == "east": 
      # makes sure the user stays in the map
      if col == 3:
        print("You have ran into a wall. ")
        print('\n')
        print("Please type in another direction. ")
        print('\n')
      else: 
        col += 1
        break
    # if the user chose none of the above, do the following
    else:
      print(wrongMessage)
      print('\n')


def mainChoice():
  """
  function for mainChoice
  this function will asks for the user's action 
  """
  # prints the options for action
  while True:
    print("Possible actions: ")
    for key in actionChoice:
      print(f"- {key}")
    actionChoice2 = (input(action))
    print('\n')
    # if the user chose walk as their action, do the following
    if actionChoice2 == "walk":
      print(actionChoice["walk"]["description"])
      print('\n')
      print(actionChoice["walk"]["message"])
      print('\n')
      break
    # if the user chose search as their action, do the following
    elif actionChoice2 == "search":
      print(actionChoice["search"]["description"])
      print('\n')
      print(actionChoice["search"]["message"])
      print('\n')
      randomResult.randomResult()
      print('\n')
      break
    # if the user chose quit as their action, do the following
    elif actionChoice2 == "quit":
      print(actionChoice["quit"]["description"])
      print('\n')
      print(actionChoice["quit"]["message"])
      sys.exit()
    # if the user chose inventory as their action, do the following
    elif actionChoice2 == "inventory":
      print(actionChoice["inventory"]["description"])
      print('\n')
      print(actionChoice["inventory"]["message"])
      print('\n')
      print("Inventories: ")
      for item in Inventory:
        print(f"- {item}")
        print('\n')
      print('\n')
      print("Medicines: ")
      for meds in Medicine:
        print(f"- {meds}")
        print('\n')
      print('\n')
      print("Foods: ")
      for food in Food:
        print(f"- {food}")
        print('\n')
      print('\n')
      break
    # if the user chose none of the above, do the following
    else:
      print("No capital letters!")
      print('\n')


# Main
while True: 
  current_location = map.HauntedMansion[row][col]
  # if the user is at the Entrance, do the following
  if current_location == "Entrance":
    print(map.roomsHauntedMansion["Entrance"]["description"])
    print('\n')
  # if the user is at the grand ball room, do the following
  elif current_location == "Grand Ball Room":
    print(map.roomsHauntedMansion["Grand Ball Room"]["description"])
    print('\n')
  # if the user is at the closet, do the following
  elif current_location == "Closet":
    print(map.roomsHauntedMansion["Closet"]["description"])
    print('\n')
  # if the user is at the master bedroom, do the following
  elif current_location == "Master Bedroom":
    print(map.roomsHauntedMansion["Master Bedroom"]["description"])
    print('\n')
  # if the user is at the rooftop, do the following
  elif current_location == "Rooftop":
    print(map.roomsHauntedMansion["Rooftop"]["description"])
    print('\n')
  # if the user is at the bathroom, do the following
  elif current_location == "Bathroom":
    print(map.roomsHauntedMansion["Bathroom"]["description"])
    print('\n')
  # if the user is at the exit, do the following
  elif current_location == "Exit":
    print(map.roomsHauntedMansion["Exit"]["description"])
    break
  # if the user is not at any of the locations above, do the following
  else:
    print(wrongMessage)
    print('\n')
  # Main Menu
  mainChoice()
  movements()