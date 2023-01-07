print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload


direction = input(
    "You stumble across a stop with two pathways. Do you go left or right?: ")

new_direction = direction.lower()

if new_direction == "left".lower():
    print("You chose to go left.")
else:
    print("You take a right and are blinded by a tall beam in the sky. You lose balance and fall into a hole. GAME OVER, TRY AGAIN.")
    exit()

lake = input("You walk a quick and lovely path and are stopped by a mysterious lake. The waters are shaking, something feels off. Swim or Wait?: ")

lake_choice = lake.lower()

if lake_choice == "wait".lower():
    print("A hungry trout erupts from the lake but swims away when it sees there is no food. You continue forward.")
else:
    print("You embark on a swim and feel a tug on your leg sink you down. You take one last look and see a trout attack you and drag you into the abyss. GAME OVER")
    exit()

doors = input("You march on forward and stop by a castle with three doors. There is a red door, a blue door, and a yellow door. Which do you choose to enter?: ")

door_choice = doors.lower()

if door_choice == "yellow".lower():
    print("Congratulations! You've won!")
elif door_choice == "blue".lower():
    print("Eaten by beasts. GAME OVER.")
elif door_choice == "red".lower():
    print("Burned by fire. GAME OVER")
else:
    print("GAME OVER.")
