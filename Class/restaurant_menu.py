# Activity:  Design a personalized menu using nested dictionaries in Python. Your menu should feature different categories, such as appetizers (apps), main courses, desserts, and beverages. For each item in your menu, include details like price, ingredients, and any other relevant information you think would be helpful.

# Appetizer
    # Samosas - Shafee
        # Price: $3
    # Fries - Jeremy
        # Price: $5
    # Calamari - Ayanna
        # Price: $10
    # Dumpling - Kenneth
# Main Course
# Desserts
# Bev

# food_menu = {
#     "appetizer": {
#         "samosa": {
#             "price": 3.00
#         },
#         "fries": {
#             "price": 5.00
#         },
#         "calamari": {
#             "price": 10.00
#         },
#         "dumplings": {
#             "price": 7.50
#         }
#     },
#     "main course": {
#         "lasagna": {
#             "description": "Type of layered pasta dish"
#         },
#         "pizza": {
#             "description": "A cheesy pie"
#         },
#         "burger": {
#             "description": "It's a burger"
#         },
#         "paella": {
#             "description": "Medley of rice, seafood, sausage, vegetables"
#         }
#     },
#     "desserts": {
#         "milkshake": {
#             "calories": 400
#         },
#         "sundae": {
#             "calories": 600
#         },
#         "lava_cake": {
#             "calories": 800
#         },
#         "sorbet": {
#             "calories": 200
#         }
#     },
#     "beverages": {
#         "mango lassi": {
#             "is_vegan": False,
#             "ingredients": ['mango', 'yogurt', 'water']
#         },
#         "thai iced tea": {
#             "is_vegan": False,
#             "ingredients": ['milk', 'black tea', 'sugar']
#         },
#         "sugarcane juice": {
#             "is_vegan": True,
#             "ingredients": ['sugarcane', 'ice']
#         },
#         "water": {
#             "is_vegan": True,
#             "ingredients": ['hydrogen^2', 'oxygen']
#         }
#     }
# }

# print(food_menu["appetizer"]["dumplings"]["price"])
food_menu = {
    "appetizer": {
        "samosa": {
            "price": 3.00,
            "description": "Crispy pastry filled with spiced potatoes and peas",
            "calories": 130,
            "is_vegan": True,
            "ingredients": ['potatoes', 'peas', 'flour', 'spices', 'oil']
        },
        "fries": {
            "price": 5.00,
            "description": "Golden crispy potato fries",
            "calories": 365,
            "is_vegan": True,
            "ingredients": ['potatoes', 'oil', 'salt']
        },
        "calamari": {
            "price": 10.00,
            "description": "Fried squid rings served with dipping sauce",
            "calories": 450,
            "is_vegan": False,
            "ingredients": ['squid', 'flour', 'oil', 'spices']
        },
        "dumplings": {
            "price": 7.50,
            "description": "Steamed or fried dough filled with meat or vegetables",
            "calories": 200,
            "is_vegan": False,  
            "ingredients": ['flour', 'meat or vegetables', 'soy sauce', 'spices']
        }
    },
    "main course": {
        "lasagna": {
            "price": 12.00,
            "description": "Layered pasta with rich meat sauce, cheese, and béchamel",
            "calories": 600,
            "is_vegan": False,
            "ingredients": ['pasta', 'ground beef', 'tomato sauce', 'cheese', 'béchamel sauce']
        },
        "pizza": {
            "price": 15.00,
            "description": "Cheesy tomato sauce base with various toppings",
            "calories": 300,
            "is_vegan": False,  
            "ingredients": ['pizza dough', 'tomato sauce', 'cheese', 'toppings']
        },
        "burger": {
            "price": 10.00,
            "description": "Juicy beef patty with lettuce, tomato, and cheese",
            "calories": 500,
            "is_vegan": False,  
            "ingredients": ['beef patty', 'bun', 'lettuce', 'tomato', 'cheese']
        },
        "paella": {
            "price": 18.00,
            "description": "Spanish rice dish with seafood, sausage, and vegetables",
            "calories": 700,
            "is_vegan": False,
            "ingredients": ['rice', 'seafood', 'sausage', 'vegetables', 'saffron']
        }
    },
    "desserts": {
        "milkshake": {
            "price": 5.00,
            "description": "Creamy blended ice cream drink",
            "calories": 400,
            "is_vegan": False,  
            "ingredients": ['ice cream', 'milk', 'sugar', 'flavoring']
        },
        "sundae": {
            "price": 6.00,
            "description": "Ice cream topped with syrup, nuts, and whipped cream",
            "calories": 600,
            "is_vegan": False,  
            "ingredients": ['ice cream', 'syrup', 'whipped cream', 'nuts']
        },
        "lava_cake": {
            "price": 7.00,
            "description": "Warm chocolate cake with a molten center",
            "calories": 800,
            "is_vegan": False,
            "ingredients": ['chocolate', 'flour', 'sugar', 'eggs', 'butter']
        },
        "sorbet": {
            "price": 4.00,
            "description": "Frozen dessert made with sweetened fruit juice",
            "calories": 200,
            "is_vegan": True,
            "ingredients": ['fruit juice', 'sugar', 'water']
        }
    },
    "beverages": {
        "mango lassi": {
            "price": 3.50,
            "description": "Smoothie made with mango and yogurt",
            "calories": 150,
            "is_vegan": False,  
            "ingredients": ['mango', 'yogurt', 'water']
        },
        "thai iced tea": {
            "price": 4.00,
            "description": "Sweetened black tea with milk",
            "calories": 180,
            "is_vegan": False,  
            "ingredients": ['milk', 'black tea', 'sugar']
        },
        "sugarcane juice": {
            "price": 3.00,
            "description": "Freshly pressed sugarcane juice served over ice",
            "calories": 120,
            "is_vegan": True,
            "ingredients": ['sugarcane', 'ice']
        },
        "water": {
            "price": 1.00,
            "description": "Pure, refreshing water",
            "calories": 0,
            "is_vegan": True,
            "ingredients": ['hydrogen^2', 'oxygen']
        }
    }
}