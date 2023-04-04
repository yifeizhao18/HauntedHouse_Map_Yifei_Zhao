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
###############################################################################
# Global Variables & Imports
import sys
import random
row = 2
col = 2

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

# # dictionary for characters 
# possibleCharacter = {
#   "ghost1" : {
#     "description" : "This is the most common ghost in the mansion. You flashlight will be enough to shine them away from you. ",
#     "locationMap" : "[(1,3), (0,1), (3,1), (2,0), (1,2), (3,2), (3,3)]",
#   },
#   "ghost2" : {
#     "description" : "These are a little bit better than the basic ghosts. however, these have lived in the mansion for the longest time. You need to kill them with the knife. GOOD LUCK! ",
#     "locationMap" : "[(0,0), (2,1), (0,2), (0,3), (2,3), (0,4), (2,4)]",
#   },
#   "theGhost" : {
#     "description" : "OH NO!! These are the ghosts you DO NOT want to come across. They can kill you within seconds, and you will not even notice it. Unfortunately, you can only kill them with the sword. ",
#     "locationMap" : "[(1,0), (3,0), (1,1), (0,3), (1,4)]"
#   }
# }

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
# list for the possible items in the treasure box
treasureBox = ["knife", "sword", "flashlight", "food", "medicine"]

# dictionary for the map-tile
roomsHauntedMansion = {
  "Entrance" : {
    "description" : "Welcome To The Haunted House! You are currently at the Entrance. Your goal is to collect as many items as possible. ",
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

# empty list for inventory, foods, medicines, and weapons
Inventory = []
Food = []
Medicine = []

# messages to be printed on the console 
askDirection = ("Do you want to go South, North, East, or West now? ")
answer = ("Sounds good! ")
action = ("What movement would you like to do? ")
wrongMessage = ("Sorry, you cannot move in that direction. Please choose another direction. ")
wrongSpelling = ("Please only answer yes or no. No capital letters. ")
endingMessage = ("Thank you for playing. Bye! ")
leaveMessage = ("Do you want to leave now? ")
congratsMessage = ("Congratulations! ")
collectMessage = ("Do you want to collect it? ")


def randomResult():
  result = random.randint(0,9)
  if result == 0:
    print(possibleResults["result1"])
  elif result == 1:
    print(possibleResults["result6"])
    print(congratsMessage)
    while True:
      collect = input(collectMessage)
      if collect == "yes":
        Inventory.append("knife")
        print(Inventory)
        break
      elif collect == "no":
        print(answer)
        break
      else:
        print(wrongSpelling)
  elif result == 2: 
    print(possibleResults["result7"])
    print(congratsMessage)
    while True:
      collect = input(collectMessage)
      if collect == "yes":
        Inventory.append("sword")
        print(Inventory)
        break
      elif collect == "no":
        print(answer)
        break
      else:
        print(wrongSpelling)
  elif result == 3: 
    print(possibleResults["result4"])
    print(congratsMessage)
    while True:
      collect = input(collectMessage)
      if collect == "yes":
        Food.append("apples")
        print(Food)
        break
      elif collect == "no":
        print(answer)
        break
      else:
        print(wrongSpelling)
  elif result == 4:
    print(possibleResults["result5"])
    print(congratsMessage)
    while True: 
      collect = input(collectMessage)
      if collect == "yes":
        Inventory.append("flashlight")
        print(Inventory)
        break
      elif collect == "no":
        print(answer)
        break
      else:
        print(wrongSpelling)
  elif result == 5:
    print(possibleResults["result2"])
    print(congratsMessage)
    while True:
      collect = input(collectMessage)
      if collect == "yes":
        Food.append("energy drink")
        print(Food)
        break
      elif collect == "no":
        print(answer)
        break
      else:
        print(wrongSpelling)  
  elif result == 6:
    print(possibleResults["result3"])
    print(congratsMessage)
    while True: 
      collect = input(collectMessage)
      if collect == "yes":
        Medicine.append("bandages", "pills")
        print(Medicine)
        break
      elif collect == "no":
        print(answer)
        break
      else:
        print(wrongSpelling)
  elif result == 7:
    print(possibleResults["result1"])
  elif result == 8:
    print(possibleResults["result5"])
    print(congratsMessage)
    while True: 
      collect = input(collectMessage)
      if collect == "yes":
        Inventory.append("flashlight")
        print(Inventory)
        break
      elif collect == "no":
        print(answer)
        break
      else:
        print(wrongSpelling)
  elif result == 9:
    print(possibleResults["result5"])
    print(congratsMessage)
    while True:
      collect = input(collectMessage)
      if collect == "yes":
        Inventory.append("flashlight")
        print(Inventory)
        break
      elif collect == "no":
        print(answer)
        print('\n')
        break
      else:
        print(wrongSpelling)
      

possibleResults = {
  "result1" : "Sorry! There is nothing here. ",
  "result2" : "You found some energy drink. ",
  "result3" : "You found a treasure chest with bandages and pills. ",
  "result4" : "You found some food. ",
  "result5" : "You found a treasure chest with a flashlight in it. ",
  "result6" : "You found a treasure chest with a knife in it. ",
  "result7" : "You found a treasure chest with a sword in it. "
  }


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


# def treasureChoice():
#   """
#   function for the treasure choices.
#   this will be randomized. 
#   """


def mainChoice():
  """
  function for mainChoice
  this function will asks for the user's action 
  """
  # prints the options for action
  print("Possible actions: ")
  for key in actionChoice:
    print(f"- {key}")
  actionChoice2 = (input(action))
  print('\n')
  # if the user chose walk as their action, do the following
  if actionChoice2 == "walk":
    print(actionChoice["walk"]["message"])
  # if the user chose search as their action, do the following
  elif actionChoice2 == "search":
    print(actionChoice["search"]["message"])
    print('\n')
    randomResult()
    print('\n')
  # if the user chose quit as their action, do the following
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