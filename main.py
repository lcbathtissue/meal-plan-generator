import random


def get_dishes_from_file():
    f = open("dishes.txt", "r")
    recipes = []
    file_contents = f.read().split("\n")
    for line in file_contents:
        if line != "# enter your dishes here , one on each line, minimum 15":
            recipes.append(line)
    f.close()
    return recipes


def get_previous_meal_plan_from_file():
    f = open("meal_plan.txt", "r")
    meals = []
    file_contents = f.read().split("\n")
    for line in file_contents:
        meals.append(line)
    f.close()
    return meals


def generate_random_meal(recipes):
    return recipes[random.randrange(0, len(recipes)-1)]


def generate_weekly_meals(recipes, prev_meals):
    weekly_meals = []
    prev_week = get_previous_week_meals(prev_meals)
    days = [
        "Monday: ",
        "Tuesday: ",
        "Wednesday: ",
        "Thursday: ",
        "Friday: ",
        "Saturday: ",
        "Sunday: "
    ]
    while len(weekly_meals) != 7:
        meal_to_be_added = generate_random_meal(recipes)
        add_meal = True
        if weekly_meals.count(meal_to_be_added) != 0:  # checks if the meal is already a part of the new week
            add_meal = False
        if prev_week.count(meal_to_be_added) != 0:  # checks if the meal is already a part of the previous week
            add_meal = False
        if add_meal:
            weekly_meals.append(meal_to_be_added)
    for num in range(7):
        print(f"{days[num]}{weekly_meals[num]}")
    overwrite_save_file(prev_week, weekly_meals)


def get_previous_week_meals(prev_meals):
    if len(prev_meals) == 1:
        prev_meals = []
        recipes = get_dishes_from_file()
        for num in range(14):
            prev_meals.append(recipes[num])
    if len(prev_meals) < 10:
        recipes = get_dishes_from_file()
        prev_week = recipes[0:7]
        weekly_meals = recipes[7:14]
        overwrite_save_file(prev_week, weekly_meals)
    prev_week = []
    for num in reversed(range(7)):
        prev_week.append(prev_meals[-num-1])
    return prev_week


def overwrite_save_file(prev_week, weekly_meals):
    meals = ""
    for meal in prev_week:
        meals = meals + meal + "\n"
    for meal in weekly_meals:
        meals = meals + meal + "\n"
    meals = meals[:-1]

    f = open("meal_plan.txt", "w")
    f.write(meals)
    f.close()


recipes = get_dishes_from_file()
prev_meals = get_previous_meal_plan_from_file()
generate_weekly_meals(recipes, prev_meals)
