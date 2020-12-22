def find_letters(string, search_letter):
    result = string.find(search_letter)
    return result


print(find_letters("angelique", "p"))


def find_letters_1(string, search_letter, start=0):
    for index, letter in enumerate(string[start:]):
        if letter == search_letter:
            return index + start
    return "not here"


print(find_letters_1("angelique", "e"))


def find(haystack, needle, start=0, end=-1):
    for index, letter in enumerate(haystack[start:end]):
        if letter == needle:
            return index + start
    return -1


print(find("angelique", "e"))
