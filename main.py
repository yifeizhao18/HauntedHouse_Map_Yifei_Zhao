###############################################################################
# Title: Data Structures: RPG - Inventory

# Class: Computer Science 30 P1 S2                                                                                                                   
# Date: March 13, 2023

# Coder's Name: Yifei Zhao                                                                                                            
# Version: 002                                                                                        
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

# map for the HauntedMansion 
HauntedMansion = [
  ["Grand Ball Room", "Master Bedroom", "Bathroom", "Master Bedroom"],
  ["Closet", "Master Bedroom", "Rooftop", "Closet"],
  ["Grand Ball Room", "Bathroom", "Entrance", "Bathroom"],
  ["Master Bedroom", "Closet", "Rooftop", "Bathroom"],
  ["Rooftop", "Master Bedroom", "Grand Ball Room", "Exit"]
]

# dictionary for actions 
actionChoice = {
  "walk" : {
    "message" : "Currently Walking Around!"
  },
  "search" : {
    "message" : "Searching For Possible Keys!"
  },
  "quit" : {
    "message" : "Thank you for playing. Bye!"
  }
}

# dictionary for characters
possibleCharacter = {
  "ghost1" : {
    "description" : "This is the most common ghost in the mansion. You flashlight will be enough to shine them away from you. ",
    "locationMap" : "[(1,3), (0,1), (3,1), (2,0), (1,2), (3,2), (3,3)]",
  },
  "ghost2" : {
    "description" : "These are a little bit better than the basic ghosts. These have lived in the mansion for the longest time. You need to kill them with the knife. GOOD LUCK! ",
    "locationMap" : "[(0,0), (2,1), (0,2), (0,3), (2,3), (0,4), (2,4)]",
  },
  "theGhost" : {
    "description" : "OH NO!! These are the ghosts you DO NOT want to come across. They can kill you within seconds, and you will not even notice it. Unfortunately, you can only kill them with the sword. ",
    "locationMap" : "[(1,0), (3,0), (1,1), (0,3), (1,4)]"
  }
}

# dictionary for the objects
# treasureBox: {
#   "Medicine" : {
#     "description" : "The user will be able to find medicine to heal themselves from the possible attacks from the ghosts. ",
#     "possibleItems" : "["bandages", "pills"]",
#     "bandages" : "This can help with the minimum attack. ",
#     "pills" : "This can help with stronger attacks. ",
#   },
#   "Food" : {
#     "description" : "The user will be able to find food to gain energy. ",
#     "possibleItems" : ["water", "foods", "snacks"],
#     "water" : "This can help with dehydration, but you cannot gain a lot of energy. ",
#     "foods" : "This can help you gain a lot of energy to keep exploring the house. ",
#     "snacks" : "This can help you gain some energy. ",
#   },
#   "KeyItems" : {
#     "description" : "The user will be able to find items that are very important in survivng. ",
#     "possibleItems" : ["knife", "sword", "flashlight"],
#     "knife" : "This can help you fight ghost2. ",
#     "sword" : "This can help you fight ghost3. ",
#     "flashlight" : "This can help you fight ghost1. "
#   }
# }
treasureBox = ["knife", "sword", "flashlight", "food", "medicine"]

# dictionary for the map-tile
roomsHauntedMansion = {
  "Entrance" : {
    "description" : "Welcome To The Haunted House! You are currently at the Entrance. Your goal is to escape this mansion before you die. ",
    "num_treasure" : "0", 
  }, 
  "Grand Ball Room" : {
    "description" : "You are currently in the Grand Ball Room. This is the largest room in this house, maybe you want to explore it. BE CAREFUL!! ",
    "num_treasure" : "1",
  },
  "Closet" : {
    "description" : "You are currently in the Closet. This is the smallest room in this house. All of the clothes in the closet... What can I find here? ",
    "num_treasure" : "1",
  },
  "Master Bedroom" : {
    "description" : "You are currently in the Master Bedroom. This is where the previous couples stayed before they were never seen ever again... ",
    "num_treasure" : "2",
  },
  "Rooftop" : {
    "description" : "You are currently at the Rooftop of this mansion. This is the highest place of this mansion. Be careful NOT to fall down... ",
    "num_treasure" : "1",
  },
  "Bathroom" : {
    "description" : "You are currently in the Bathroom. The room of slaughter. Be careful NOT to be the next one... ",
    "num_treasure" : "3",
  },
  "Exit" : {
    "description" : "Thank you for playing. Bye! ",
    "num_treasure" : "1",
  }
}

# empty list for inventory
actionPossible = ["walk", "search", "quit"]
Inventory = []
Food = []
Heal = []
Weapon = []

# messages to be printed on the console when the user is in that specific room
askDirection = ("Do you want to go South, North, East, or West now? ")
answer = ("Sounds good! ")
action = ("What movement would you like to do? ")
walk = ("Walking! ")
wrongMessage = ("Sorry, you cannot move in that direction. Please choose another direction. ")
wrongSpelling = ("Please only answer yes or no. No capital letters. ")
endingMessage = ("Thank you for playing. Bye! ")


def movements():
  """
  movement function that asks for the user input on directions.
  makes sure the user does not walk off of the map.
  """
  global row, col
  # asks for user input 
  movementChoice = (input(askDirection))
  print('\n')
  print(answer)
  print('\n')
  # if the user put in North, do the following 
  if movementChoice == "North":
    # makes sure the user stays in the map
    if row == 0:
      print("You have ran into a wall. ")
      print('\n')
      print("Please type in another direction. ")
    else:
      row -= 1
  # if the user put in South, do the following
  elif movementChoice == "South":
    # makes sure the user stays in the map
    if row == 4:
      print("You have ran into a wall. ")
      print('\n')
      print("Please type in another direction. ")
    else:
      row += 1
  # if the user put in West, do the following
  elif movementChoice == "West":
    # makes sure the user stays in the map
    if col == 0:
      print("You have ran into a wall. ")
      print('\n')
      print("Please type in another direction. ")
    else:
      col -= 1
  # if the user put in East, do the following
  elif movementChoice == "East": 
    # makes sure the user stays in the map
    if col == 3:
      print("You have ran into a wall. ")
      print('\n')
      print("Please type in another direction. ")
    else: 
      col += 1
  # if the user chose none of the above, do the following
  else:
    print(wrongMessage)


def mainChoice():
  """
  function for mainChoice
  this function will asks for the user's action 
  """
  print("Possible actions: ")
  for option in actionPossible:
    print(f"- {option}")
  actionChoice2 = (input(action))
  print('\n')
  # if the user chose walk as their action, do the following
  if actionChoice2 == "walk":
    print(actionChoice["walk"]["message"])
  # if the user chose search as their action, do the following
  elif actionChoice2 == "search":
    print(actionChoice["search"]["message"])
  elif actionChoice2 == "quit":
    print(actionChoice["quit"]["message"])
    sys.exit()
  # if the user chose none of the above, do the following
  else:
    print("walk is the only option right now! No capital letters!")
    print('\n')
    input(action)
  print('\n')


# Main
while True: 
  current_location = HauntedMansion[row][col]
  # if the user is at the Entrance, do the following
  if current_location == "Entrance":
    print(roomsHauntedMansion["Entrance"]["description"])
    print('\n')
  # if the user is at the grand ball room, do the following
  elif current_location == "Grand Ball Room":
    print(roomsHauntedMansion["Grand Ball Room"]["description"])
    print('\n')
  # if the user is at the closet, do the following
  elif current_location == "Closet":
    print(roomsHauntedMansion["Closet"]["description"])
    print('\n')
  # if the user is at the master bedroom, do the following
  elif current_location == "Master Bedroom":
    print(roomsHauntedMansion["Master Bedroom"]["description"])
    print('\n')
  # if the user is at the rooftop, do the following
  elif current_location == "Rooftop":
    print(roomsHauntedMansion["Rooftop"]["description"])
    print('\n')
  # if the user is at the bathroom, do the following
  elif current_location == "Bathroom":
    print(roomsHauntedMansion["Bathroom"]["description"])
    print('\n')
  # if the user is at the exit, do the following
  elif current_location == "Exit":
    print(roomsHauntedMansion["Exit"]["description"])
    break
  # if the user is not at any of the locations above, do the following
  else:
    print(wrongMessage)
    print('\n')
  # Main Menu
  mainChoice()
  movements()