while True:

    number = int(input("Which Francois number would you like to see? "))
    if number <= 0:
        print("Please enter a valid number")
    else:
        break

if number == 1:
    francois = 2

elif number == 2:
    francois = 1

else:
    francois_list = [2, 1]
    len_francois = len(francois_list)

    while len_francois != number:
        francois = francois_list[len_francois-1] + francois_list[len_francois-2]
        francois_list.append(francois)
        len_francois = len(francois_list)

print(f"Francois number {number} is {francois}")