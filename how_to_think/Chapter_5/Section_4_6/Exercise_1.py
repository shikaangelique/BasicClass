text = "ThiS is String with Upper and lower case Letters"

def extracting(text):
    letter_counts = {}
    text = text.lower()
    for letter in text:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    return letter_counts


print(extracting("shika"))


def sorting(text):
    dictionary = extracting(text)
    for letter in sorted(dictionary):
        print(letter, dictionary[letter])


print(sorting(text))

def add_fruit(inventory, fruit, quantity=0):
    if fruit not in inventory:
        inventory[fruit] = quantity
    else:
        inventory[fruit] += quantity
