spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    name_list = list()
    for i in spicy_foods:
        name_list.append(i["name"])
    return name_list

def get_spiciest_foods(spicy_foods):
    spiciest_foods = list()
    for i in spicy_foods:
        if i["heat_level"] > 5:
            spiciest_foods.append(i)
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for i in spicy_foods:
        print(f'{i["name"]} ({i["cuisine"]}) | Heat Level: {"🌶" * i["heat_level"]}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')

def get_average_heat_level(spicy_foods):
    total_spice = 0
    for food in spicy_foods:
        total_spice += food["heat_level"]
    average_spice = total_spice / len(spicy_foods)
    return int(average_spice)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
