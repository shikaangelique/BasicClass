def sum_to(upper_limit):
    sum_to = 0
    for i in range(upper_limit + 1):
        sum_to += i
    return sum_to


print(sum_to(10))


def area_of_circle(radius):
    area = 22 / 7 * (radius ** 2)
    return area


print(round(area_of_circle(2), 2))
