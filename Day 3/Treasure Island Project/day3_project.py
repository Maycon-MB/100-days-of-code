import time

print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("🏝️ Welcome to the Fabulous Treasure Island Adventure! 🏝️")
print("Your mission is to find the legendary treasure... if you dare!")
time.sleep(1)

# Primeira escolha: cruzamento
choice1 = input('You\'re at a mysterious crossroad. 🌲🌲 '
                'Will you go "left" into the dark forest or "right" towards the mountain trail? \n').lower()

if choice1 == "left":
    print("You bravely venture left and arrive at a misty lake. 🌫️")
    time.sleep(1)
    
    # Segunda escolha: lago
    choice2 = input('There\'s an eerie island in the middle of the lake. '
                    'Do you "wait" for a boat 🛶 or "swim" across like a fearless hero? \n').lower()
    
    if choice2 == "wait":
        print("You patiently wait, and a boat mysteriously appears out of nowhere! 🛥️ It takes you to the island.")
        time.sleep(1)
        
        # Terceira escolha: portas
        choice3 = input("On the island, you find a strange house with 3 doors: "
                        "one red 🔴, one yellow 🟡, and one blue 🔵. "
                        "Which color do you choose?\n").lower()
        
        if choice3 == "red":
            print("🔥 Oops! It's a room full of fire! You're now a toasted marshmallow. Game Over!")
        elif choice3 == "yellow":
            print("🎉 Congratulations! You open the door and find the treasure chest overflowing with gold! You Win! 🏆💰")
        elif choice3 == "blue":
            print("😱 You enter a dark room filled with snarling beasts! They seem to be very hungry. Game Over!")
        else:
            print("🚪 Hmm, that door doesn’t exist in this world. Maybe in a parallel universe? Game Over.")
    
    else:
        print("🌊 You start swimming, but a very angry trout decides you look like dinner. Game Over!")
    
else:
    print("😵 You confidently walk right... only to step into a deep, dark hole! Ouch. Game Over!")
