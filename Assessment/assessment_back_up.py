__author__ = "Shika Akpaloo"

import os

file_name = "nutritional_values.csv"

if not os.path.isfile(file_name):
    with open(file_name, "w") as nutritional_value_file:
        nutritional_value_file.write("ingredient,unit,kcal,fat,carbohydrate,protein \n")

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
print(ingredient_list)
#print(nutritional_value_dict)

for ingredient in ingredient_list:
    if ingredient not in nutritional_value_dict:
        print("Please provide the following information:")
        unit = input("How many weight does " + ingredient + " contain? ")
        kcal = input("How many kilo calories does " + ingredient+ " contain? ")
        fat = input("How many grams of fat does " + ingredient + " contain? ")
        carbohydrate = input("How many grams of carbohydrate does " + ingredient + " contain? ")
        protein = input("How many grams of protein does " + ingredient + " contain? ")
        nutritional_value_dict[ingredient] = (unit, kcal, fat, carbohydrate, protein)

with open(file_name, "w") as nutritional_value_file:
    nutritional_value_file.write("ingredient,unit,kcal,fat,carbohydrate,protein \n")
    for ingredient in nutritional_value_dict:
        unit, kcal, fat, carbohydrate, protein = nutritional_value_dict[ingredient]
        nutritional_value_file.write(ingredient + "," + str(unit) + "," + str(kcal) + "," + str(fat) + "," + str(carbohydrate) + "," + str(protein) + "\n")

user_amounts = {}
for ingredient in ingredient_list:
    user_amount = input("What is the weight (in grams) of " + ingredient + " in your recipe?")
    user_amounts[ingredient] = user_amount

total_val = {}
for ingredient in ingredient_list:
    total_cal = float(user_amounts[ingredient]) * float(nutritional_value_dict[ingredient][1])
    total_faat = float(user_amounts[ingredient]) * float(nutritional_value_dict[ingredient][2])
    total_car = float(user_amounts[ingredient]) * float(nutritional_value_dict[ingredient][3])
    total_pro = float(user_amounts[ingredient]) * float(nutritional_value_dict[ingredient][4])
    total_val[ingredient] = (total_cal, total_faat, total_car, total_pro)
print(total_val)

total_calories = 0
total_fat = 0
total_carbs = 0
total_protein = 0
for ingredient in ingredient_list:
    print(ingredient, total_val[ingredient][0])
    total_calories += round(total_val[ingredient][0], 2)
    total_fat += round(total_val[ingredient][1], 2)
    total_carbs += round(total_val[ingredient][2], 2)
    total_protein += round(total_val[ingredient][3], 2)

longest_ingredient = max([len(ingredient) for ingredient in ingredient_list])
while longest_ingredient < len("ingredient"):
    longest_ingredient = len("ingredient")

table_format = "{:<" + str(longest_ingredient+2) + "} {:>7} {:>7} {:>7} {:>7} {:>11} {:>7}\n"

with open("output.txt", "w") as output_file:
    output_file.write(table_format.format("ingredient","unit","unit2","kcal","fat","carbohydrate","protein"))
    for ingredient in ingredient_list:
        output_file.write(table_format.format(ingredient, user_amounts[ingredient], *nutritional_value_dict[ingredient]))
    output_file.write(table_format.format("","","", total_calories, total_fat, total_carbs, total_protein))

for ingredient in ingredient_list:
    print(table_format.format(ingredient, user_amounts[ingredient], *nutritional_value_dict[ingredient]))
    print(table_format.format("total","","", total_calories, total_fat, total_carbs, total_protein))

