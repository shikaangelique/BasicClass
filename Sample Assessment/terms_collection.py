## downton abbey themed bingo

with open("terms.txt", "r") as terms_file:
    bingo_terms = terms_file.read().splitlines()

with open("terms.txt", "a+") as terms_file:
    add_term = input("Add a Downton Abbey Character to the list or hit enter to exit: ")

    while add_term != "":
        if add_term in bingo_terms:
            print("This character is already included")
        else:
            bingo_terms.append(add_term)
            terms_file.write(add_term + "\n")
        add_term = input("Add a Downton Abbey Character to the list or hit enter to exit: ")


