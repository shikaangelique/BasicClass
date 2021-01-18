import os

existing_file = "travel_modes.txt"
if not os.path.isfile(existing_file):
    with open("travel_modes.txt", "w") as user_file:
        user_file.write("Bike " + input("What is your travel time by bike?") + "\n")
        user_file.write("Bus " + input("What is your travel time by bus?") + "\n")
        user_file.write("Train " + input("What is your travel time by train?") + "\n")
        user_file.write("Car " + input("What is your travel time by car?") + "\n")

dictionary = {}
with open("travel_modes.txt", "r") as travel_data:
    for line in travel_data:
        words = line.split()
        dictionary[words[0]] = dictionary.get(words[1], 0)+1

print(dictionary)








