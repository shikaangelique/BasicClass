def four_digiter(oldfile, newfile):
    with open(oldfile, "r") as infile, open(newfile, "w") as outfile:
        string_format = "{:<4} {}"
        four_digit = 0
        for line in infile:
            four_digit += 1
            outfile.write(string_format.format(four_digit, line))


four_digiter("oldfile.txt", "four_digiter.txt")

#  alternatively:
#  with open("numbered_snakes.txt", "w") as numbered_snake_poem:
#  for line_number, line in enumerate(lines):
#  numbered_snake_poem.write(str(line_number + 1) + ": " + line)