import random
from typing import List

with open("terms.txt", "r") as terms_file:
    bingo_terms = terms_file.read().splitlines()

random.shuffle(bingo_terms)

# the card
card_size = 5
longest_term = max([len(term) for term in bingo_terms])
term_format = "{:^" + str(longest_term) + "}"
line_format = term_format * card_size + "\n"
card_format = line_format * card_size

print(card_format.format(*bingo_terms[:(card_size ** 2)]))


#user_input = input("What term would you like to mark?")

#if user_input in magic_set:
    #magic_set[magic_set.index(user_input)] = "X"
    #print(magic_set)
#else:
    #print("that term is not on your card")
    #print(magic_set)


