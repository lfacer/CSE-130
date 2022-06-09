print("")
street = "27617 238th PL SE"
city = "Maple Valley"
state = "WA"
zip = "98038"

print (street)
print (city + ", " + state + " " + str(zip))

print("")
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

gender_string = ""

while gender_string != "y" and gender_string != "n":
    gender_string = input("Are you male? (y/n) ")
 
    if gender_string == "y":
        gender = True

    elif gender_string == "n":
        gender = False
    
    else:
        print("Please enter 'y' or 'n'.")


print (f"Your name is {name}.")
print ("You were born in the year ", 2022-age)
print ("You are a male? ", gender)

print("")

start_value = int(input("What number do you want to start with? "))
end_value = int(input("What number would you like to end with? "))
step_value = int(input("How much do you want to count by? "))

for number in range(start_value, end_value+1, step_value):
    print(number)

print("")

phone_book = {"Police": 911, "Jenny": 8675309, "Operator": 0}

print(phone_book["Jenny"])
