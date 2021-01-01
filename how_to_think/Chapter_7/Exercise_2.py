def snake_catcher(oldfile, newfile):
    with open(oldfile, "r") as infile, open(newfile, "w") as outfile:
        for line in infile:
            if line.__contains__('snake'):
                outfile.write(line)


snake_catcher("oldfile.txt", "snake_catcher.txt")

#  alternatively:
#  for line in lines:
#  if line.find("snake") >= 0:
#  print(line)
