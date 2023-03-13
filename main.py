# Global Variables & Imports
row = 2
col = 2

# Functions
HauntedMansion = [
  ["Grand Ball Room", "Master Bedroom", "Bathroom", "Master Bedroom"]
  ["Closet", "Master Bedroom", "Rooftop", "Closet"]
  ["Grand Ball Room", "Bathroom", "Entrance", "Bathroom"]
  ["Master Bedroom", "Closet", "Rooftop", "Bathroom"]
  ["Rooftop", "Master Bedroom", "Grand Ball Room", "Exit"]
]

directions = ["South", "North", "East", "West"]

welcomeMessage = ("Welcome To The Haunted House! You are currently at the Entrance. ")
askDirection = ("Do you want to go South, North, East, or West? ")
answer = ("Sounds good!")
action = ("What movement would you like yo do? The only option in this room is walk. ")
walk = ("Walking!")
ballroomMessage = ("You are currently in the Grand Ball Room. ")
closetMessage = ("You are currently in the Closet. ")
endingMessage = ("Sorry, you cannot move in that direction. Please choose another direction. ")

def movements():
  global row, col
  print(input(askDirection))
  print(answer)
  if askDirection == "South":
    row -= 1
  elif askDirection == "North":
    row += 1
  elif askDirection == "East":
    col += 1
  elif askDirection == "West":
    col -= 1
  else:
    print(endingMessage)
  
# Main
current_location = HauntedMansion[row][col]

if current_location == "Entrance":
  print(welcomeMessage)
  print(input(action))
  print(walk)
  movements()
elif current_location == "Grand Ball Room":
  print(ballroomMessage)
  print(input(action))
  print(walk)
  movements()
elif current_location == "Closet":
  print(closetMessage)
  print(input(action))
  print(walk)
  movements()