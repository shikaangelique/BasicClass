from typing import List

vector1 = [2, 1, 4]
vector2 = [2, 1, 4]

print(list(zip(vector1, vector2)))

def add_vectors(vector1, vector2):
    new_vector = []
    for i,j in zip(vector1, vector2):
        sum_vector = i+j
        new_vector.append(sum_vector)
    return new_vector


def scalar_mult(scalar, vector):
    new_vector = []
    for i in vector:
        scalar_multiple = i*scalar
        new_vector.append(scalar_multiple)
    return new_vector


def dot_product(vector1, vector2):
    new_vector = []
    for i,j in zip(vector1,vector2):
        ind_product = i*j
        new_vector.append(ind_product)
    dot_product = sum(new_vector)
    return dot_product


def cross_product(vector1, vector2):
    new_vector = []

print(add_vectors([2, 1, 4], [1, 1, 3]))

print(scalar_mult(5, [1, 2]))

print(dot_product([1, 2, 1], [1, 4, 3]))


