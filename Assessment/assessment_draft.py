__author__ = "Shika Akpaloo"

import os

file_name = "nutritional_values.csv"

if not os.path.isfile(file_name):
    with open(file_name, "w") as nutritional_value_file:
        nutritional_value_file.write("ingredient,unit,kcal,fat,carbohydrate,protein\n")
        nutritional_value_file.write("cheese,100.0,404.0,33.0,3.1,23.0\n")
        nutritional_value_file.write("sugar,100.0,387.0,0,99.9,0\n")

ingredient_list = []
new_ingredient = input("Add an ingredient to the list or hit enter to exit:")
while new_ingredient != "":
    if new_ingredient in ingredient_list:
        print("This ingredient is already included")
    else:
        ingredient_list.append(new_ingredient)
    new_ingredient = input("Add an ingredient to the list or hit enter to exit:")

nutritional_value_dict = {}
with open(file_name) as nutritional_value_file:
    lines = nutritional_value_file.readlines()[1:]
    for line in lines:
        ingredient, unit, kcal, fat, carbohydrate, protein = line.split(",")
        nutritional_value_dict[ingredient] = (float(unit), float(kcal), float(fat), float(carbohydrate), float(protein))
# print(ingredient_list)
# print(nutritional_value_dict)

for ingredient in ingredient_list:
    if ingredient not in nutritional_value_dict:
        print("Please provide the following information:")
        unit = input("What is the unit for " + ingredient + "? ")
        kcal = input("How many kilo calories does " + ingredient + " contain? ")
        fat = input("How many grams of fat does " + ingredient + " contain? ")
        carbohydrate = input("How many grams of carbohydrate does " + ingredient + " contain? ")
        protein = input("How many grams of protein does " + ingredient + " contain? ")
        nutritional_value_dict[ingredient] = (unit, kcal, fat, carbohydrate, protein)

with open(file_name, "w") as nutritional_value_file:
    nutritional_value_file.write("ingredient,unit,kcal,fat,carbohydrate,protein \n")
    for ingredient in nutritional_value_dict:
        unit, kcal, fat, carbohydrate, protein = nutritional_value_dict[ingredient]
        nutritional_value_file.write(
            ingredient + "," + str(unit) + "," + str(kcal) + "," + str(fat) + "," + str(carbohydrate) + "," + str(
                protein) + "\n")

user_amounts = {}
for ingredient in ingredient_list:
    user_amount = input("What is the weight (per 100 gram) of " + ingredient + " in your recipe?")
    user_amounts[ingredient] = user_amount

total_val = {}
for ingredient in ingredient_list:
    total_cal = float(user_amounts[ingredient]) * float(nutritional_value_dict[ingredient][1])
    total_faat = float(user_amounts[ingredient]) * float(nutritional_value_dict[ingredient][2])
    total_car = float(user_amounts[ingredient]) * float(nutritional_value_dict[ingredient][3])
    total_pro = float(user_amounts[ingredient]) * float(nutritional_value_dict[ingredient][4])
    total_val[ingredient] = (total_cal, total_faat, total_car, total_pro)
# print(total_val)

total_calories = 0
total_fat = 0
total_carbs = 0
total_protein = 0
for ingredient in ingredient_list:
    total_calories += total_val[ingredient][0]
    total_fat += total_val[ingredient][1]
    total_carbs += total_val[ingredient][2]
    total_protein += total_val[ingredient][3]

longest_ingredient = max([len(ingredient) for ingredient in ingredient_list])
while longest_ingredient < len("ingredient"):
    longest_ingredient = len("ingredient")

table_format = "{:<" + str(longest_ingredient + 2) + "} {:>9} {:>9} {:>9} {:>9} {:>11} {:>9}\n"

with open("output.txt", "w") as output_file:
    output_file.write("Overview of Nutritional Information for Recipe:\n")
    output_file.write(table_format.format("ingredient", "amount", "unit(g)", "kcal", "fat(g)", "carbohydrate(g)", "protein(g)"))
    for ingredient in ingredient_list:
        output_file.write(table_format.format(ingredient, user_amounts[ingredient], *nutritional_value_dict[ingredient]))
    output_file.write(table_format.format("total", "", "", round(total_calories, 2), round(total_fat, 2), round(total_carbs, 2), round(total_protein, 2)))

with open("output.txt", "r") as output_file:
    print(output_file.read())
