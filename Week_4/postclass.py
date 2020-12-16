def get_five_numbers():
    total = 0
    for i in range(5):
        number = input("Give a number ")
        number = int(number)
        total = total + number
    return total

def get_user_input():
    # intial values to get us started total = 0
    total = 0
    print("0 to stop")
    number = int(input("Give a number "))
    while number != 0:
        # process the number
        total = total + number
        # get the next number
        number = int(input("Give a number "))
    return total

total = get_five_numbers()
print(total)

total = get_user_input()
print(total)