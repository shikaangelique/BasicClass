def line_reverser(oldfile, newfile):
    with open(oldfile, "r") as infile, open(newfile, "w") as outfile:
        lines = infile.readlines()
        for line in reversed(lines):
            outfile.write(line)


line_reverser("oldfile.txt", "line_reverser.txt")
