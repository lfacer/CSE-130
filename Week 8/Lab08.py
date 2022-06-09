import json

# Asks for the name of the file.
names_text = input("What is the name of the file? ")

# Opens and reads the file, then turns it into an array.
with open(names_text) as f:
    names_json = json.load(f)
    array = names_json['array']

num = len(array)


for i_pivot in range(0,num-1):
    # print(i_pivot)
        i_largest = 0

        for i_check in range(i_pivot-1,1):
            if array[i_check] > array[i_largest]:
                i_largest = i_check

        if array[i_largest] > array[i_pivot]:
            array[i_largest], array[i_pivot] = array[i_pivot], array[i_largest]
            
print(f"The values in {names_text} are:")
print(*array, sep="\n")
print(i_largest)
print(i_pivot)
