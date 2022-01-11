print("welcome to my computer quiz!")

playing = input("do you want to play quiz game? ")

if playing.lower() != "yes":
    quit()
print("Okay! Let's start the game:) ")
score = 0

answer = input("What does CPU stand for? ")
if answer == "CENTRAL processing unit".lower():
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer == "random access memory".lower():
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does www stand for? ")
if answer == "world wide web".lower():
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does GPU stand for? ")
if answer == "graphics processing unit".lower():
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got" + str(score) + "questions correct")
print("You got " + str((score/4)*100) + ".%")


