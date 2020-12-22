import string

nicki_quote = """
You could never make eye contact, 
everything you got was based on my contacts, 
You a fraud but imma remain icon stat,
Balenciagas on my boots with the python strap,
You was caught up in the rush?
Caught up in the thrill of it,
You was with me way before I hit a quarter mill in it,
Put you in a crib and you ain\'t never paid a bill in it,
I was killing it! 
Man you had me popping pills in it.
"""


def sign_strip(verse):
    stripped_verse = ""
    count = 0
    for word in verse:
        if word not in string.punctuation:
            stripped_verse += word
            count += 1
    return stripped_verse

def words_containing(word, letter):
    ecount = 0
    for word in sign_strip(word).split():
        if letter in word:
            ecount += 1
    return ecount

stripped_nicki = sign_strip(nicki_quote).split()
word_count = len(stripped_nicki)
words_with_e = words_containing(nicki_quote,"e")
percentage = round((words_with_e/word_count)*100)


print("Your text contains", word_count, "words of which", words_with_e,  "(",percentage,"%) contain an \"e\".")
