import random

print("Welcome to the Guessing Game App")

#create name profile
name = input("\nWhat is your name: ").title()
print("Well " + name + ", I am thinking of a number between 1 and 20")


number = random.randint(1, 20)

#create a limit of 5 possible guesses in the game
for guess_num in range(0,5):
   guess = int(input("\nGuess the number: "))

   if guess > number:
       print("Guess too high")
   elif guess < number:
       print("Guess too low")
   else:
       break

#create exit for game
if guess == number:
    print("\nGood job, you guessed", number, "correctly!")
else:
    print("\nThat's too bad, the number I was thinking of was", number)
