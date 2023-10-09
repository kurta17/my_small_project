import random
import string

characters = list(string.ascii_letters + string.digits + "!@#$%^&")

def gen_password():
    len_password = int(input("Enter your password length "))

    random.shuffle(characters)

    password = []

    for i in range(len_password):
        password.append(random.choice(characters))
    
    random.shuffle(password)
    new_password = "".join(password)
    print(new_password)

ask = input("Do you want to create password? (Yes/No)").lower()

if ask == "yes":
    gen_password()
elif ask == 'no':
    print('Okay, bye')
    quit()
else:
    print ("Invalid Input!")

