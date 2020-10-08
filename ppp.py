with open('recept.txt', encoding='utf-8') as new_cookbook:
    recipes = new_cookbook.read()
    recipes = recipes.split("\n\n")

    class Dishes:
      def __init__(self, dish_name, ingredient_number, ing_list):
        self.name = dish_name
        self.ing_number = ingredient_number
        self.ing_list = ing_list

    class Ingredients:
      def __init__(self, name, quantity, measure):
        self.name = name
        self.quantity = quantity
        self.measure = measure

    cook_book = {}
    for dish in recipes:
      dish = dish.split('\n')
      dish = Dishes(dish[0], dish[1], dish[2:])
      for new_ingredient in dish.ing_list:
        ingredients = new_ingredient.split('|')
        ingredients = Ingredients(ingredients[0], int(ingredients[1]), ingredients[2])
        ing_dict = {'ingredient_name': ingredients.name.strip(), 'quantity': ingredients.quantity, 'measure': ingredients.measure.strip()} 
        ingedient_dict = []
        ingedient_dict.append(ing_dict)
        cook_book.setdefault(dish.name, ingedient_dict)

    print(cook_book)




