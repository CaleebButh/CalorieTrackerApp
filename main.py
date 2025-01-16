from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

FAT_GOAL = 90
PROTEIN_GOAL = 200
CALORIE_GOAL = 2000
CARBS_GOAL = 154

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

        #Generate the figure with 4 subplots
        fig, axs = plt.subplots(2,2)

        #Generate the pie chart
        axs[0,0].pie([total_calories, total_carbs, total_fat, total_protein], labels=["Calories","Carbs", "Fats", "Protein"], autopct="%1.1f%%")
        axs[0,0].set_title("Macro Distribution")

        #bar chart
        axs[0,1].bar([0, 1, 2], [total_protein, total_fat, total_carbs], width=0.4)
        axs[0,1].bar([0.5, 1.5, 2.5], [PROTEIN_GOAL, FAT_GOAL, CARBS_GOAL], width=0.4)
        axs[0,1].set_title("Macro Progress")

        #Calories vs daily limit pie chart
        axs[1,0].pie([total_calories, CALORIE_GOAL - total_calories], labels=["calories", "Remaining"], autopct="%1.1f%%")
        axs[1,0].set_title("Calories consumed vs Goal")

        #Line chart
        axs[1,1].plot(list(range(len(today))), np.cumsum([food.calories for food in today]), label="Calories Eaten")
        axs[1,1].plot(list(range(len(today))), [CALORIE_GOAL] * len(today), label = "Calorie goal" )
        axs[1,1].legend()
        axs[1,1].set_title("Calories Goal Over Time")

        #show plots
        fig.tight_layout()
        plt.show()

    elif choice.lower() == "q":
        done = True
    else:
        continue
print("Goodbye")