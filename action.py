import main 
import randomResult
import sys

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
    actionChoice2 = (input(main.actionMessage))
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
      for item in main.Inventory:
        print(f"- {item}")
        print('\n')
      print('\n')
      print("Medicines: ")
      for meds in main.Medicine:
        print(f"- {meds}")
        print('\n')
      print('\n')
      print("Foods: ")
      for food in main.Food:
        print(f"- {food}")
        print('\n')
      print('\n')
      break
    # if the user chose none of the above, do the following
    else:
      print("No capital letters!")
      print('\n')