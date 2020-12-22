prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter == "O":
        print(letter +"u"+ suffix)
    if letter == "Q":
        print(letter +"u"+ suffix)
    else:
        print(letter + suffix)