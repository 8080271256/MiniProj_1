import random

entered_num =int(input("Enter a num: "))

if entered_num <= 0:
    print("please enter a num larger than 0 next time")
    quit()
guesses = 0
while True:
    user_guess = int(input("make a guess: "))
    guesses += 1

    random_num = random.randint(0,entered_num)
    print(random_num)

    if user_guess == random_num:
        print("congrats! you got it.")
        break
    else:
        print("oops! you got it wrong.")
print("you got it in ",guesses,"guesses")

