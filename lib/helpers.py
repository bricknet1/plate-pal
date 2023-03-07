def create_ingredients_table(ingredients):
    print('-' * 50)
    print(f'|ID  |NAME{" " * 39}|')
    print('-' * 50)
    for ingredient in ingredients:
        id_spaces = 4 - len(str(ingredient.id))
        name_spaces = 43 - len(ingredient.name)
        print(f'|{ingredient.id}{" " * id_spaces}|{ingredient.name}{" " * name_spaces}|')
    print('-' * 50)

def create_recipe_table(recipes):
    print('-' * 50)
    print(f'|ID  |RECIPE{" " * 39}|')
    print('-' * 50)
    for recipe in recipes:
        id_spaces = 4 - len(str(recipe.id))
        name_spaces = 43 - len(recipe.name)
        print(f'|{recipe.id}{" " * id_spaces}|{recipe.name}{" " * name_spaces}|')
    print('-' * 50)