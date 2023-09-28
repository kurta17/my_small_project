print("Welcome to My quiz!")

playing = input("Do you want to play? ")

if playing != "Yes":
    print("Okey, Goodbye ")
    quit()

print("Okey, let's play! ")

score = 0

answer = input("1. What are two things you can never eat for breakfast?")
if answer == "Lunch and Dinner":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")


answer = input("2. What is always coming but never arrives?")
if answer == "Tomorrow":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")


answer = input(
    "3. What is it that lives if it is fed, and dies if you give it a drink?"
)
if answer == "Fire":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")


answer = input("4. What goes up but never ever comes down?")
if answer == "Human's Age":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")

answer = input(
    "5. If you have one, you want to share it. But once you share it, you do not have it. What is it?"
)
if answer == "A secret":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")


answer = input("6. What has a face and two hands, but no arms or legs?")
if answer == "A clock":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")

answer = input(
    "7. Some months have 31 days, others have 30 days, but how many have 28 days?"
)
if answer == "All 12 months":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")

print("You got" + str(score) + "questions correct! ")
