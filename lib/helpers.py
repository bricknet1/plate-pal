from db.models import Ingredient
from db.models import Recipe
from db.models import RecipeIngredient
from playsound import playsound

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


def create_recipe_table(session, recipes):
    print('-' * 50)
    print(f'|ID  |RECIPE{" " * 39}|')
    print('-' * 50)


    recipe_objects = session.query(RecipeIngredient).filter(RecipeIngredient.ingredient_id.in_(selected_ingredients_list)).all()
    recipe_ids = []
    for obj in recipe_objects:
        recipe_ids.append(obj.recipe_id)
    if len(recipe_ids) == 0:
        print("Sorry, there are no recipes at this thyme. Please try adding other ingredients.")
        print('~' * 50)
        add_ingredient(session)

    for recipe in recipes:
        id_spaces = 4 - len(str(recipe.id))
        name_spaces = 43 - len(recipe.name)
        if recipe.id in recipe_ids:
            print(f'|{recipe.id}{" " * id_spaces}|{recipe.name}{" " * name_spaces}|')
    playsound('recipes.mp3')
    print('-' * 50)

    choose_recipe(session)


def add_ingredient(session):
    ingredient_item_id = input('Please enter in an ingredient ID: ')
    playsound('add.mp3')
    while ingredient_item_id:
        selected_ingredients_list.append(ingredient_item_id)
        ingredients = session.query(Ingredient)
        print('-' * 50)
        print("Ingredients you've selected")
        print('-' * 50)
        playsound('recipes.mp3')

        for ingredient in ingredients:
            if str(ingredient.id) in selected_ingredients_list:
                print(f'•{ingredient.name}')
        print('-' * 50)
        yes_no = None
        while yes_no not in YES + NO:
            yes_no = input('Would you like to add another ingredient? (Y/N) ')
            playsound('add.mp3')
            if yes_no.lower() in YES:
                ingredient_item_id = input('Please enter the ID of your next ingredient: ')
                playsound('recipes.mp3')
                
            elif yes_no.lower() in NO:
                playsound('recipes.mp3')
                ingredient_item_id = None
                recipes = session.query(Recipe)
                create_recipe_table(session, recipes)


def choose_recipe(session):
    recipe_item_id = input('Please enter in a recipe ID: ')
    playsound('add.mp3')
    recipes = session.query(Recipe)
    for recipe in recipes:
        if recipe.id == int(recipe_item_id):

            print('~' * 50)
            print(f"How to prepare {recipe.name}")
            print(recipe.instructions)
            print('~' * 50)
            playsound('recipes.mp3')
        
    recipe_list_loop = input('Would you like to see the recipe list again? (Y/N) ')
    if recipe_list_loop.lower() in NO:
        playsound('add.mp3')
        print('''   
  ____                                    ?~~bL
  z@~ b     Goodbite, have a nice dish!    |  `U,
 ]@[  |                                   ]'  z@'
 d@~' `|, .__     _----L___----, __, .  _t'   `@j
`@L_,   "-~ `--"~-a,           `C.  ~""O_    ._`@
 q@~'   ]P       ]@[            `Y=,   `H+z_  `a@
 `@L  _z@        d@               Ya     `-@b,_a'
  `-@d@a'       )@[               `VL      `a@@'
    aa~'   ],  .a@'                qqL  ), ./~
    @@_  _z~  _d@[                 .V@  .L_d'
     "~@@@'  ]@@@'        __      )@n@bza@-"
       `-@zzz@@@L        )@@z     ]@@=%-"
         "~~@@@@@bz_    _a@@@@z___a@K
             "~-@@@@@@@@@@@@@@@@@@~" 
                `~~~-@~~-@@~~~~~' 

        Presented by the The Plate Mates™
        
        ''')
        playsound('goodbite.mp3')
    else:
        create_recipe_table(session, recipes)