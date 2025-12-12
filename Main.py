#Russian roulette

import random

cylinders = [0, 0, 0, 0, 0, 1]

def play(choice):
    while playing == True:

      choice = Input("Choose your fate." )
      
    if choice == "Pull It":
       #Play the game. Take a risk to earn money- what could go wrong?
       chamber = random.choice(cylinders)
            if chamer = 1:
                #if cylinder = 1 means IF chamber is loaded. The player loses if they land on a value of 1 | "LOADED"
                print("Bang. It all fades to black")
                playing == False
            else:
                #if cylinder = 0 means IF chamber is emopty. The player passes the round and gets to keep playing
                print("Click. You survive another round").
                playing == True
                round = round + 1
              
    if choice == "Spin It":
        # Reshuffle your rounds. Randomize the order of the bullets. With a risk.
        cylinders = random.shuffle(cylinders)
    if choice == "Stop It" or "End" or "Stop":
        #Stops the game. The player stays alive and keeps all of their money earned.
        playing == False




play(choice)
        
        
