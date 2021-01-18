__author__ = "Shika Akpaloo"

import os

Strings = list[str]  ## delete this after dear

def get_recipe_ingredients() -> Strings:
    ingredient_list = []
    new_ingredient = input("Add an ingredient to the list or hit enter to exit")
    while new_ingredient != "":
        if new_ingredient in ingredient_list:
            print("This ingredient is already included")
        else:
            ingredient_list.append(new_ingredient)
    return ingredient_list


def get_nutritional_values(ingredient_list: Strings, file_name="nutritional_values.csv") -> dict:
    if not os.path.isfile(file_name):
        with open(file_name, "w") as nutritional_value_file:
            nutritional_value_file.write("name,unit,kcal,fat,carbohydrate,protein\n")

    nutritional_value_dict = {}
    with open(file_name) as nutritional_value_file:
        for line in file_name:
            name, unit, kcal, fat, carbohydrate, protein = line.split(",")
            nutritional_value_dict[name] = (float(unit), float(kcal), float(fat), float(carbohydrate), float(protein))

    for value in nutritional_value_dict:
        if value not in nutritional_value_dict:
            kcal = input("How many kilo calories does", value, "contain?")
            fat = input("How many grams of fat does", value, "contain")
            carbohydrate = input("How many grams of carbohydrate does", value, "contain")
            protein = input("How many grams of protein does", value, "contain")

    return nutritional_value_dict

def get_nutritional_value(ingredient: str, nutrient_list: Strings) -> dict:
    """
    Given a list of nutrients and the name of an ingredient,
    asks the user to provide this information.
    """
    values = {}
    ingredient = input("Add an ingredient from the recipe of press enter to exit")



