# Dictionary to store food items and their macronutrient values (per 100g or per serving)
food_database = {
    "apple": {"calories": 52, "protein": 0.3, "carbs": 14, "fat": 0.2},
    "chicken breast": {"calories": 165, "protein": 31, "carbs": 0, "fat": 3.6},
    "rice": {"calories": 130, "protein": 2.4, "carbs": 28, "fat": 0.3}
}

# Dictionary to track daily intake
daily_log = {
    "calories": 0,
    "protein": 0,
    "carbs": 0,
    "fat": 0
}

def add_food(name, calories, protein, carbs, fat):
    """
    Add a new food item to the food database.
    """
    food_database[name] = {
        "calories": calories,
        "protein": protein,
        "carbs": carbs,
        "fat": fat
    }
    print(f"Added {name} to the food database.")

def log_meal(food_name, serving_size):
    """
    Log a meal by adding its macronutrients to the daily log.
    
    Parameters:
    food_name (str): Name of the food item
    serving_size (float): Serving size in grams or as a multiplier of the base serving
    """
    if food_name in food_database:
        food = food_database[food_name]
        daily_log["calories"] += food["calories"] + serving_size
        daily_log["protein"] += food["protein"] * serving_size
        daily_log["carbs"] += food["carbs"] * serving_size
        daily_log["fat"] += food["fat"] * serving_size
        print(f"Logged {serving_size} serving(s) of {food_name}.")
    else:
        print(f"{food_name} not found in the database.")

def view_daily_summary():
    """
    View a summary of the daily intake.
    """
    print("\nDaily Intake Summary:")
    print(f"Calories: {round(daily_log['calories'], 2)} kcal")
    print(f"Protein: {round(daily_log['protein'], 2)} g")
    print(f"Carbohydrates: {round(daily_log['carbs'], 2)} g")
    print(f"Fat: {round(daily_log['fat'], 2)} g")

# Example usage
while True:
    print("\nOptions:")
    print("1. Add a new food item")
    print("2. Log a meal")
    print("3. View daily summary")
    print("4. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        name = input("Enter food name: ").lower()
        calories = float(input("Enter calories per serving: "))
        protein = float(input("Enter protein per serving (g): "))
        carbs = float(input("Enter carbs per serving (g): "))
        fat = float(input("Enter fat per serving (g): "))
        add_food(name, calories, protein, carbs, fat)
    
    elif choice == "2":
        food_name = input("Enter food name to log: ").lower()
        serving_size = float(input("Enter serving size (e.g., 1 for standard serving, 0.5 for half serving): "))
        log_meal(food_name, serving_size)
    
    elif choice == "3":
        view_daily_summary()
    
    elif choice == "4":
        print("Exiting...")
        break
    
    else:
        print("Invalid option. Please try again.")
