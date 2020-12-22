import string


def reverse(word):
    reversed_word = ""
    for i in range(len(word) - 1, -1, -1):  # confused about this line of code
        reversed_word += word[i]
    return reversed_word

def mirror(word):
    return word + reverse(word)


def letter_remover(word, letter):
    removed = ""
    for i in word:
        if i != letter:
            removed += i
    return removed


def palindrome_scanner(word):
    if word == reverse(word):
        return True


def is_palindrome(word):
    return word == reverse(word)


def counter(word,searchee):
    count = 0
    for letter in word:
        if letter == searchee:
            count += 1
    return count

def sub_counter(word,searchee):
    count = 0
    if searchee in word:
        count += 1
    return count


def substring_remover(word, substring):
    new_word = word.replace(substring, "", 2)  # 1 removes (only one) the first occurrence
    return new_word


print(reverse("shika"))
print(mirror("shika"))
print(letter_remover("shika", "s"))
print(palindrome_scanner("racecar"))
print(not is_palindrome("shika"))

print(sub_counter("badabaddabadybumswing", "bad"))
print(substring_remover("badabaddabadybumswing", "bad"))



