import random

secret_number = random.randint(1,10)
guess_number = int(input("choose a number between 1 and 10: "))

if guess_number not in range(1,11):
    print("The number must be between 1 and 10")
else:
    if guess_number == secret_number:
        print("Congrats! You guessed the number!")
    else:
        print("Wrong number. Try again.")

print("guessed number was " + str(guess_number))
print("secret number was " + str(secret_number))
