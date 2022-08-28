def main():
    users_fruit = input("Item: ").title().strip()

    fruit_calories = {
        "Apple": "130",
        "Avocado": "50",
        "Banana": "110",
        "Cantaloupe": "50",
        "Grapefruit": "60",
        "Grapes": "90",
        "Honeydew Melon": "50",
        "Sweet Cherries": "100",
        "Strawberries": "50",
        "Kiwifruit": "90",
        "Pear": "100"


    }

    if users_fruit in fruit_calories:
        print("calories:",fruit_calories[users_fruit])



main()