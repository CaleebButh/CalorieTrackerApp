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
        protein = int(input("Protein: "))
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

        #Generates Macro pie chart
        total_protein = sum(food.protein for food in today)
        total_calories = sum(food.calories for food in today)
        total_carbs = sum(food.carbs for food in today)
        total_fat = sum(food.fat for food in today)

        #Generates pie chart
        macros = [total_calories, total_carbs, total_fat, total_protein]
        pieChartLabels = ["Calories", "Carbs", "Fats", "Protein"]

        fig, ax = plt.subplots()
        ax.pie(macros, labels=pieChartLabels, autopct="%1.1f%%")

        #adds calories from foods to list.
        foodsToday = [food.name for food in today]
        calsToday = []
        for food in today:
            calsToday.append(food.calories)

        #Generates caloric bar graph
        plt.bar(foodsToday, calsToday, width=0.3)
        plt.title("Calories from food today.")
        plt.xlabel("Foods")
        plt.ylabel("Calories")

        #show plots
        plt.show()

    elif choice.lower() == "q":
        done = True
    else:
        continue
print("Goodbye")
