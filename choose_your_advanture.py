name = input("Enter your name: ")
print("Welcom",name,"to this advanture!")

answer = input("you are on a dirt road, it has  to come at end and you can go left or right, which way would you like to go?  ").lower()

if answer == "left":
    answer = input("you came to a river, you can walk around it or swim across? enter walk to walk around and swim to swim across; ")

    if answer == "swim":
        print("you swam across and were eaten by fish.since , you lost!")

    elif answer  == "walk":
        print("you walked many miles, ran out of water and you lost the game.")

    else:
        print("not a valid option. you lost!")


elif answer == "right":
    answer = input("you came to a bridge, it looks wobbly, do you want cross it head  back(cross/back)? ").lower()

    if answer == "back":
        print("you came back and lost!")

    elif answer  == "cross":
        answer = input("you crossed the bridge and met the stranger, do you want to talk to stranger? ").lower()


        if answer == "yes":
            print("you talked to a stranger, they gave you gold,  you won!")
        
        elif answer == " no":

            print("you ignored the stranger, they got offended at you, you lose!")

        else:
            print("not a valid option , you lost!")

    else:
        print("not a valid option. you lost!")



else:
    print("not a valid option. you lost!")