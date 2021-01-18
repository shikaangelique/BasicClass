def show_card(card, size):
    longest_term = max([len(term) for term in bingo_terms])

    term_format = "{:^" + str(longest_term) + "}"
    line_format = term_format * size + "\n"
    card_format = line_format * size

    print(card_format.format(*card))

show_card(bingo_terms, 5)