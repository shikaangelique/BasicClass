
def replace(word, old, new):
    word_list = word.split()
    for words in word_list:
        new_word = word.replace(old, new)
    return new_word


song = "I love spom! Spom is my favorite food. Spom, spom, spom, yum!"

print(song.split())

print(replace(song, "om", "am"))