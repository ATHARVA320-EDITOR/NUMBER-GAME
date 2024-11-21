import random
playing = True
number = str(random.randint(1,50))
print("I will generate a number, you need to guess it:")
print("The game ends when you get correct number.")
while playing:
    guess = input("Give me your best guess.\n")
    if number == guess:
        print("You win the game")
        print("The number was ",number)
        break
    else:
        print("Try again mate.\n")
