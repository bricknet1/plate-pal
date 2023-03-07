from db.models import Ingredient
from db.models import Recipe
from db.models import RecipeIngredient

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


def add_ingredient(session):
    ingredient_item_id = input('Please enter in an ingredient ID: ')
    while ingredient_item_id:
        selected_ingredients_list.append(ingredient_item_id)
        print(selected_ingredients_list)
        yes_no = None
        while yes_no not in YES + NO:
            yes_no = input('Would you like to add another ingredient? (Y/N) ')
            if yes_no.lower() in YES:
                ingredient_item_id = input('Please enter the ID of your next ingredient: ')
            elif yes_no.lower() in NO:
                ingredient_item_id = None
                print('We are friggin done')
                # recipes = session.query(Recipe)
                # create_recipe_table(recipes)




