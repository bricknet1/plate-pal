YES = ['y', 'ye', 'yes']
NO = ['n', 'no']
selected_ingredients_list = []

def create_ingredients_table(ingredients):
    print('-' * 50)
    print(f'|ID  |NAME{" " * 39}|')
    print('-' * 50)
    for ingredient in ingredients:
        id_spaces = 4 - len(str(ingredient.id))
        name_spaces = 43 - len(ingredient.name)
        print(f'|{ingredient.id}{" " * id_spaces}|{ingredient.name}{" " * name_spaces}|')
    print('-' * 50)

    select_ingredient_prompt = input('Select an ingredient by ID: ')

    selected_ingredients(select_ingredient_prompt)
    print(selected_ingredients_list)

def create_recipe_table(recipes):
    print('-' * 50)
    print(f'|ID  |RECIPE{" " * 39}|')
    print('-' * 50)
    recipes_to_display = []
    for each in selected_ingredients_list:
        if each in RecipeIngredient.ingredient_id:
            recipes_to_display.append(each)

    for recipe in recipes:
        
        id_spaces = 4 - len(str(recipe.id))
        name_spaces = 43 - len(recipe.name)
        if recipe.id in recipes_to_display:
            print(f'|{recipe.id}{" " * id_spaces}|{recipe.name}{" " * name_spaces}|')
    print('-' * 50)


def selected_ingredients(ingredient):
    selected_ingredients_list.append(ingredient)
