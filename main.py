from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

PROTEIN_GOAL = 200
CALORIE_GOAL = 2000

today = []

@dataclass
class Food:
    name: str
    protein: int
    calories: int
    carbs: int
    fat: int

done = False

while not done:
    print("""
    1) Add a food
    2) Visualize progress
    q) Quit
    """)

    choice = input("Choose an option: ")
    if choice == "1":
        print("Adding a new food.")
        name = input("Name: ")
        protein = input("Protein: ")
        calories = int(input("Calories: "))
        carbs = int(input("Carbs: "))
        fat = int(input("Fat: "))
        food = Food(name, protein, calories, carbs, fat)
        today.append(food)
        print(f"{name} added successfully!")

    if choice == "2":

        if not today:
            print("No foods added yet!")
            continue

        #Continue
       # total_protein = sum(food.protein for food in today)
        #total_calories = sum(food.calories for food in today)
        #total_carbs = sum(food.carbs for food in today)
        #total_fat = sum(food.fat for food in today)

        foodsToday = [food.name for food in today]
        calsToday = [food.calories for food in today]

        plt.bar(foodsToday, calsToday, width=0.3)
        plt.title("Calories from food today.")
        plt.xlabel("Foods")
        plt.ylabel("Calories")
        plt.show()



    if choice == "q":
        print("Quitting program")
        break
