'''
A guessing game where the computer will randomly choose any one of the 10 digits and the user gets 3 chances to guess the correct number.
'''
import random
from clint.textui import puts, colored

computer_number = random.choice(list(range(0,10)))
previous_guesses = set()
puts(colored.blue("The computer has choosen its number. Now it is your turn to guess..."))
user_lives = 3
while user_lives > 0:
    puts(colored.yellow("\nYou have {} lives remaining.".format(user_lives)))
    guess = int(input("Enter your guess: "))
    if guess in previous_guesses:
        puts(colored.yellow("You have already tried this number. Try again."))
        continue
    previous_guesses.add(guess)
    if guess == computer_number:
        puts(colored.green("CONGRATULATIONS!! YOU HAVE GUESSED THE NUMBER CORRECTLY."))
        break
    else:
        user_lives = user_lives - 1
        puts(colored.red("Sorry wrong guess. Try again."))
        if guess > computer_number:
            print("HINT: The number is smaller than the number you entered")
        else:
            print("HINT: The number is larger than the number you entered")
        
if user_lives == 0:
    puts(colored.red("GAME OVER!"))
    puts(colored.blue("The computer's number was {}".format(computer_number)))
