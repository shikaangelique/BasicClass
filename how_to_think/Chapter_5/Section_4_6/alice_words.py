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


print(words)