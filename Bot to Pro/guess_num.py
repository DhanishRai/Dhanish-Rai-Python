import random
secret_number= random.randint(1,10)
print("welcome to the guessing game")
print("I have choosen a number between 1 and 10")
for attempt in range(3):
    guess=int(input(f"Attempting {attempt+1}:enter your guess"))
    if guess==secret_number:
        print(" congratulations , you have guessed the correct number")
        break
    elif guess> secret_number:
        print("high!!!, try lower one")
       
    else:
        print("low!!, try a highet number")
     
    
else: 
       print(f"sorry, you ran out of tries, the guesed number was {secret_number}") 
