text_raw = "ThiS is String with Upper and lower case Letters"
text = text_raw.lower()

print(text)
letter_counts = {}

for letter in text:
    letter_counts[letter] = letter_counts.get(letter, 0) + 1

dick = list(letter_counts.items())
dick.sort()

for (letter, number) in dick:
    print(letter, number, sep="     ")


