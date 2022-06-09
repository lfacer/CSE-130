# 1. Name: 
#    Lyndsey Facer
# 2. Assignment Name: 
#    Lab 02: Authentication
# 3. Assignment Description: 
#    The assignment was to create a login program. We were given
#    a list of usernames and passwords in a json file. So I needed
#    to open the file, run through it, and then make sure that the 
#    right username is lined up with the right password.
# 4. What was the hardest part? Be as specific as possible. 
#    I think the hardest part is the index part for me. I have some trouble
#    remebering the correct syntax, espically sense I am learning several 
#    programming languages at the same time. But logically, the program wasn't 
#    too difficult for me, just remebering the right syntax.
# 5. How long did it take for you to complete the assignment? 
#    This assignment took me about an 1.5 to 2 hours to complete.

# This imports and opens the file with all the usernames and passwords.
# It also loads everything into this program
import json
with open("Lab02.json", "r") as file:
    text = file.read()
    data = json.loads(text)

# This takes the lists of usernames and passwords and sets them as a variable,
# while still being a list.
usernames = data["username"]
passwords = data["password"]

# Here is where the user will enter the username and password.
enter_username = input("Username: ")
enter_password = input("Password: ")
    
# This if loop checks for the entered username, against the list of usernames.
# It also stores the index number of the entered username, so it can later check
# across the passwords.
if enter_username in usernames:
    index = usernames.index(enter_username)

    # Here it makes sure that the password you entered matches with the same index
    # as the username you entered.
    if enter_password == passwords[index]:
        print("You are authenticated!")

    # If the indexs don't add up (you entered the wrong password), then it will 
    # make it so you don't have access to the system.
    else:
        print("You are not authorized to use the system.")

else:
    print("You are not authorized to use the system.")



