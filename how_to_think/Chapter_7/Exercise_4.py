def digit_undoer(oldfile, newfile):
    with open(oldfile, "r") as infile, open(newfile, "w") as outfile:
        string_format = "{:>" + " " + "} {:>5}\n"
        four_digit = 1000
        for line in infile:
            split = line.split()
            newline = " ".join(split[1:])
            outfile.write(newline + "\n")


digit_undoer("four_digiter.txt", "digit_undoer.txt")

# alternatively:
# for line_number, line in enumerate(lines):
# unnumbered_snake_poem.write(line.replace(str(line_number + 1) + ": ", ""))
