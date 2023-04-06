# map for the HauntedMansion 
HauntedMansion = [
  ["Grand Ball Room", "Master Bedroom", "Bathroom", "Master Bedroom"],
  ["Closet", "Master Bedroom", "Rooftop", "Closet"],
  ["Grand Ball Room", "Bathroom", "Entrance", "Bathroom"],
  ["Master Bedroom", "Closet", "Rooftop", "Bathroom"],
  ["Rooftop", "Master Bedroom", "Grand Ball Room", "Exit"]
]

# dictionary for the map-tile
roomsHauntedMansion = {
  "Entrance" : {
    "description" : "Welcome To The Haunted House! You are currently at the Entrance. Your goal is to collect as many items as possible. ",
    "num_treasure" : "randomized", 
  }, 
  "Grand Ball Room" : {
    "description" : "You are currently in the Grand Ball Room. This is the largest room in this house, maybe you want to explore it. BE CAREFUL!! ",
    "num_treasure" : "randomized",
  },
  "Closet" : {
    "description" : "You are currently in the Closet. This is the smallest room in this house. All of the clothes in the closet... What can I find here? ",
    "num_treasure" : "randomized",
  },
  "Master Bedroom" : {
    "description" : "You are currently in the Master Bedroom. This is where the previous couples stayed before they were never seen ever again... ",
    "num_treasure" : "randomized",
  },
  "Rooftop" : {
    "description" : "You are currently at the Rooftop of this mansion. This is the highest place of this mansion. Be careful NOT to fall down... ",
    "num_treasure" : "randomized",
  },
  "Bathroom" : {
    "description" : "You are currently in the Bathroom. The room of slaughter. Be careful NOT to be the next one... ",
    "num_treasure" : "randomized",
  },
  "Exit" : {
    "description" : "Thank you for playing. Bye! ",
    "num_treasure" : "randomized",
  }
}


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