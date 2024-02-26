import random

guesses = 0     #Score

top_of_range = input("Type top of range: ")     #Taking Highest Limit from user.
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)     #Generating Random number.

while True:     #User guessing number.
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    elif user_guess == 'quit':
        print(f'The number was {random_number}')
        print(f'You quit after {guesses} wrong guesses.')
        quit()
    else:
        print("Please type a number next time.")
        continue

    guesses += 1

    if user_guess == random_number:
        print("You got it!")
        break
    else:
        print("Wrong guess!     (Quit to Exit)")
        if user_guess > random_number:
            print("Guess a lower number.")
        else:
            print("Guess a higher number.")

print(f'You got the answer in {guesses} guesses.')
