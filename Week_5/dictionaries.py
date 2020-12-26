# key value pairs
fruit_bowl = {}

fruit_bowl["apple"] = 4
fruit_bowl["banana"] = 2

print(fruit_bowl)

# get()
print(fruit_bowl["banana"])
print(fruit_bowl.get("orange", 0))

letter_counts = {}
for letter in "Shika Akpaloo":
    letter_counts[letter] = letter_counts.get(letter, 0)+1
print(list(letter_counts.items()))

user_input = input("What kind of fruit will you add?")
fruit_bowl[user_input] = fruit_bowl.get(user_input, 0)+1  #  +=for things only in dictionary

print(fruit_bowl)


# iterate over all keys
# for fruit in fruit_bowl:
#   print(fruit, fruit_bowl[fruit])

for fruit, quantity in fruit_bowl.items():
    print(fruit, quantity)

# in tests keys (not values)
if "pineapple" in fruit_bowl:
    print("exotic!")
else:
    print("mundane!")

if 4 in fruit_bowl.values():
    print("there are 4")


# to and including 13 exer 5.4.6 --- 5.1, read 5.4, exx 5.2, 5.1



