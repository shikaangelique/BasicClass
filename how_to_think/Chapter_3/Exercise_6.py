numbers = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
                     49.9, 45, 44.9, 40, 39.9, 2, 0]

for number in numbers:
    if number >= 75:
        print(number, "Grade: First")

    elif 70 <= number < 75:
        print(number, "Grade: Upper Second")

    elif 60 <= number < 70:
        print(number, "Grade: Second")

    elif 50 <= number < 60:
        print(number, "Grade: Third")

    elif 45 <= number < 50:
        print(number, "Grade: F1 Supp")

    elif 40 <= number < 45:
        print(number, "Grade: F2")

    else:
        print(number, "Grade: F3")


