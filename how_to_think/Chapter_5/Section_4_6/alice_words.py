import os
import urllib.request

file_name = "alice.txt"
if not os.path.isfile(file_name):
    # if the file does not exist yet, retrieve it
    url = "http://www.gutenberg.org/files/11/11-0.txt"
    urllib.request.urlretrieve(url, file_name)

with open(file_name) as alice_book:
    alice_text = alice_book.read()

words = alice_text.lower().split()

word_bank = {}
for word in words:
    word = word.strip("!\"#$%&'()*+,./:;<=>?@[\]^_`{|}~!”")
    if len(word) > 0 and word[0].isalpha():  # if the word length is more than 1 and the first letter is an alphabet
        word_bank[word] = word_bank.get(word, 0) + 1

longest_word = ""
for word in word_bank.keys():
    if len(word) > len(longest_word):
        longest_word = word

table_format = "{:<" + str(len(longest_word)) + "} {:>5}"
print(table_format.format("Word", "Count"))
print("=" * (len(longest_word) + 5))

for word, quantity in word_bank.items():
    print(table_format.format(word, quantity))

# as a separate output file 
with open("alice_words.txt", "w") as alice_output:
    string_format = "{:<" + str(len(longest_word)) + "} {:>5}\n"

    alice_output.write(string_format.format("Word", "Count"))
    alice_output.write("=" * (len(longest_word) + 6) + "\n")

    for word in sorted(word_bank.keys()):
        alice_output.write(string_format.format(word, word_bank[word]))


