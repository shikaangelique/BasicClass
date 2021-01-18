"""Provide an overview of the nutritional values of a recipe"""

__author__ = "Vincent Velthuizen"

import os


Strings = list[str]


def get_recipe_ingredients() -> Strings:
    """
    Asks the user for a list of ingredients that will be included in a recipe
    """
    ingredient_list = []

    return ingredient_list


def get_nutritional_values(ingredient_list: Strings, file_name="nutritional_values.csv") -> dict:
    """
    Tries to get nutritional values for each of the ingredients in the list from a file
    Asks the user for the nutritional values if not yet available in the file and writes them to the file for future use
    """
    nutritional_value_dict = {}

    if not os.path.isfile(file_name):
        with open(file_name, "w") as nutritional_value_file:
            nutritional_value_file.write("name,unit,kcal,fat,carbohydrate,protein\n")

    return nutritional_value_dict


def get_nutritional_value(ingredient: str, nutrient_list: Strings) -> dict:
    """
    Given a list of nutrients and the name of an ingredient,
    asks the user to provide this information.
    """
    values = {}


    return values


def get_amounts(ingredient_list: Strings, nutritional_value_dict: dict) -> dict:
    """
    Given a list of ingredients and a dictionary of nutritional values
    ask the user to provide how much of each ingredient should be used in the recipe
    """
    amounts = {}

    return amounts


def generate_table(amounts: dict, nutritional_value_dict: dict):
    """
    ask the user for a quantity per ingredient
    generate a table with nutrient information per ingredient and a total for the recipe
    also generate a line of the total per portion (ask the user for the number of portions)
    """
    table_string = ""

    print(table_string)


if __name__ == '__main__':

    # 1.  Ask for a list of ingredients.
    ingredients = get_recipe_ingredients()

    # 2. Get nutrient information for each of these ingredients.
    nutritional_values = get_nutritional_values(ingredients)

    # 3. Ask for a list of amounts for each of the ingredients.
    amounts_list = get_amounts(ingredients, nutritional_values)

    # 4. Based on the information retrieved generate a meaningful output.
    generate_table(amounts_list, nutritional_values)
