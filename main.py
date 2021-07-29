#Damage list for my Paladin DnD
#todo:
# add smite option to weapon attack
# add attack roll
# add "is undead/fiend" to smite option
#complete rewrite options as follow:
#        type r to roll
#        choose main second cantrip other 

import csv
import sys
import random

def main():
  menu()


def menu():
  print("************Damage Rolls**************")
  print()

  print(" A: Attack \n Q: Quit\n")
  choice = input("Enter: ")
  print()

  if choice == "A" or choice =="a":
      melee()

  elif choice=="Q" or choice=="q":
      sys.exit
  else:
    print("You must only select either A or B")
    print("Please try again")
    menu()

def melee():

  print(" A: Battle Axe \n B: Sickle\n C: Punch\n D: Cantrip\n Q: Quit\n Z: Back\n")
  choice = input("Enter: ")
  print()

  if choice == "A" or choice =="a":
    print("Would you like to use smite?: Y/N")
    smite = input("Enter: ")
    print()
    if smite == "Y" or smite =="y":
      roll = random.randint(1, 8)
      bonus = 2
      rolla = roll + bonus
      rollsa = random.randint(1, 8)
      rollsb = random.randint(1, 8)
      print(" Lvl 2 spell slot: Y/N")
      slot = input("Enter: ")
      if slot == "Y" or slot =="y":
        rollsc = random.randint(1, 8)
        rolls = rollsa + rollsb + rollsc
        print("You dealt {} slashing damage and {} radiant damage!".format(rolla, rolls))
        print()
        menu()
      elif slot == "N" or slot =="n":
        rolls = rollsa + rollsb
        print("You dealt {} slashing damage and {} radiant damage!".format(rolla, rolls))
        print()
        menu()
      else:
        print("You must select a valid option")
        print("Please try again")
        print()
        menu()
    elif smite == "N" or smite =="n":
      roll = random.randint(1, 8)
      bonus = 2
      rolla = roll + bonus 
      print("You dealt {} slashing damage!".format(rolla))
      print()
      menu()
    else:
      print("You must select a valid option")
      print("Please try again")
      print()
      melee()


  elif choice == "B" or choice =="b":
    print("Would you like to use smite?: Y/N")
    smite = input("Enter: ")
    print()
    if smite == "Y" or smite =="y":
      roll = random.randint(1, 4)
      bonus = 2
      rolla = roll + bonus
      rollsa = random.randint(1, 8)
      rollsb = random.randint(1, 8)
      print(" Lvl 2 spell slot: Y/N")
      slot = input("Enter: ")
      if slot == "Y" or slot =="y":
        rollsc = random.randint(1, 8)
        rolls = rollsa + rollsb + rollsc
        print("You dealt {} slashing damage and {} radiant damage!".format(rolla, rolls))
        print()
        menu()
      elif slot == "N" or slot =="n":
        rolls = rollsa + rollsb
        print("You dealt {} slashing damage and {} radiant damage!".format(rolla, rolls))
        print()
        menu()
      else:
        print("You must select a valid option")
        print("Please try again")
        print()
        menu()
    elif smite == "N" or smite =="n":
      roll = random.randint(1, 4)
      bonus = 2
      rolla = roll + bonus 
      print("You dealt {} slashing damage!".format(rolla))
      print()
      menu()
    else:
      print("You must select a valid option")
      print("Please try again")
      print()
      melee()

  elif choice == "C" or choice =="c":
      roll = random.randint(1, 10)
      print("You dealt {} blunt damage!".format(roll))
      print()
      menu()

  elif choice == "D" or choice =="d":
      roll = random.randint(1, 4)
      print(" Dex Save Success: Y/N")
      save = input("Enter: ")
      if save == "Y" or save =="y":
        print("You dealt {} force damage!".format(roll))
        print()
        menu()
      elif save == "N" or save =="n":
        rolla = roll / 2
        print("You dealt {} force damage!".format(rolla))
        print()
        menu()
      else:
        print("You must select a valid option")
        print("Please try again")
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

main()