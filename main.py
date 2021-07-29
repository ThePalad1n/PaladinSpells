#Damage list for Paladin DnD
import csv
import sys

def main():
   menu()


def menu():
    print("************Damage Rolls**************")
    print()

    choice = input("""
                      A: Melee
                      B: Spells
                      Q: Quit

                      Please enter your choice: """)

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
   choice = input("""
                      A: Battle Axe
                      B: Sickle
                      C: Punch
                      Q: Quit
                      Z: Back

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
      #add math for roll
        print(roll)
    elif choice == "B" or choice =="b":
        #add math for roll
        print(roll)
    elif choice == "C" or choice =="c":
        #add math for roll
        print(roll)
    elif choice == "Z" or choice =="z":
        menu()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must select a valid option")
        print("Please try again")
        melee()
    
def spells():
      choice = input("""
                      A: Almighty Push
                      B: Smite
                      Q: Quit
                      Z: Back

                      Please enter your choice: """)

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