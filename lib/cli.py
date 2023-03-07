from db.models import Ingredient
from db.models import RecipeIngredient
from db.models import Recipe
from helpers import (create_ingredients_table, create_recipe_table)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



engine = create_engine('sqlite:///db/platepal.db')
Session = sessionmaker(bind=engine)
session = Session()



if __name__ == '__main__':
    
    

    ingredient_prompt = input('Would you like to select an ingredient? (Y/N): ')

    if ingredient_prompt == 'N':
        recipes = session.query(Recipe)
        create_recipe_table(recipes)
    elif ingredient_prompt == 'Y':
        ingredients = session.query(Ingredient)
        create_ingredients_table(ingredients)
    else:
        print("Please type Y or N")



    # ing = session.query(RecipeIngredient).filter(RecipeIngredient.id == selected_ingredients)
    # print(ing)
    # create_ingredient_list(ingredients_list)
