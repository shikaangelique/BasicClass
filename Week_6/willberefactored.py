
with open("test.txt", "w") as handle_1:
    handle_1.write("-Cast of Friends-\n")
    handle_1.write("Joey Tribbiani\n")
    handle_1.write("Monica Geller-Bing\n")
    handle_1.write("Ben Geller\n")
    handle_1.write("Ross Geller\n")
    handle_1.write("Rachel Geller-Green\n")
    handle_1.write("Chandler Bing\n")
    handle_1.write("Emma Geller-Green\n")


with open("test.txt", "r") as handle_2:
    all_lines = handle_2.readlines()
    all_lines.sort()

for line in all_lines:
    print(line, end="")


def filter(oldfile, newfile):
    with open(oldfile, "r") as infile, open(newfile, "w") as outfile:
        for line in infile:
            if not line.__contains__('R'):
                outfile.write(line)

filter("test.txt", "exam.txt")

trial_3 = open("/Users/angeliqueshika/PycharmProjects/BasicClass/how_to_think/Chapter_5/Section_4_6/alice_words.txt", "r")
word_list = trial_3.readlines()
print(word_list[3:5])