def game():
    import random
    computer = random.randint(1, 100)

    guess = 5
    while True:
        guess = guess - 1
        usr = int(input("You get five tries to guess the number between 1 and 100: "))
        if guess == 0:
            print("Out of tries!")
            break
        elif usr == computer:
            print("You guessed right!")
            break
        elif usr < 1:
            print("Don't go under one!")
            continue
        elif usr > 100:
            print("Don't exceed 100!")
            continue
        elif usr != computer:
            print("Wrong!")
            if usr < computer:
                print("You guessed too low")
                continue
            elif usr > computer:
                print("You guessed too high.")
                continue
        else:
            print("Not a number!")
            continue
import game
while True:
    usr1 = input("Would you like to play again? Y|n\n").lower()
    if usr1 == "y" or usr1 == "":
        import game

