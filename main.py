#Damage list for my Paladin DnD
import csv
import sys
import random

def main():
  menu()


def menu():
  print("************Damage Rolls**************")
  print()

  print(" A: Melee \n B: Spells\n Q: Quit\n")
  choice = input("Enter: ")
  print()

  if choice == "A" or choice =="a":
      melee()
  elif choice == "B" or choice =="b":
      spells()
  elif choice=="Q" or choice=="q":
      sys.exit
  else:
    print("You must only select either A or B")
    print("Please try again")
    menu()

def melee():

  print(" A: Battle Axe \n B: Sickle\n C: Punch\n Q: Quit\n Z: Back\n")
  choice = input("Enter: ")
  print()

  if choice == "A" or choice =="a":
      roll = random.randint(1, 8)
      bonus = 2
      rolla = roll + bonus
      print("You dealt {} slashing damage!".format(rolla))
      print()
      menu()
  elif choice == "B" or choice =="b":
      roll = random.randint(1, 4)
      bonus = 2
      rolla = roll + bonus
      print("You dealt {} slashing damage!".format(rolla))
      print()
      menu()
  elif choice == "C" or choice =="c":
      roll = random.randint(1, 10)
      print("You dealt {} blunt damage!".format(roll))
      print()
      menu()
  elif choice == "Z" or choice =="z":
    print()
    menu()
  elif choice=="Q" or choice=="q":
      sys.exit
  else:
      print("You must select a valid option")
      print("Please try again")
      print()
      melee()
    
def spells():
  print(" A: Almighty Push\n B: Smite\n Q: Quit\n Z: Back\n")
  choice = input("Enter: ")
  print()

  if choice == "A" or choice =="a":
      #add math for roll
      print(roll)
  elif choice == "B" or choice =="b":
        #add math for roll
      print(roll)
  elif choice == "Z" or choice =="z":
      menu()
  elif choice=="Q" or choice=="q":
      sys.exit
  else:
      print("You must select a valid option")
      print("Please try again")
      spells()
    
main()