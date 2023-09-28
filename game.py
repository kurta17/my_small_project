name = input("What is your name? ")
print("Welcome ", name, "to this advanture!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. which way would you like to go? "
).lower()

if answer == "left":
    answer = input(
        "You come to a river, you can walk around it or swim accross?  type walk to walk around or swim to swim accross: "
    )

    if answer == "swim":
        print("You swim accross and were eaten by alligator.")

    elif answer == "walk":
        print("You walked for many miles, run out of water and you lost the game.")

    else:
        print("Not a valid option. You lose!")

elif answer == "right":
    answer = input(
        "You come to a bride, it looks wobbly, do you want to accross it or head back (cross/back)?"
    )

    if answer == "back":
        print("You go back to the main road and you lose!")

    elif answer == "cross":
        answer = input(
            "You cross the bridge and meet a strangers. Do you talk to them  (Yes/No)?"
        )

        if answer == "yes":
            print("You talk to the strangers and they give you gold. YOU WIN!")

        elif answer == "no":
            print("You ignored the strangers and they are offended and you lose.")

        else:
            print("Not a valid option. You lose!")

    else:
        print("Not a valid option. You lose!")


else:
    print("Not a valid option. You lose!")

print("Thank you for trying ", name + ".")
