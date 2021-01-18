import random
import time

with open("terms.txt", "r") as terms_file:
    bingo_terms = terms_file.read().splitlines()

random.shuffle(bingo_terms)

for term in bingo_terms:
    print(term)
    # time.sleep(int(input("enter 1 when ready for the next card")))
    if input("next?") not in ["", "y", "yes"]:
        break

