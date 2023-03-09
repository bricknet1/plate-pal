from playsound import playsound
from db.models import Ingredient
from db.models import RecipeIngredient
from db.models import Recipe
from helpers import (create_ingredients_table, create_recipe_table, add_ingredient)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



engine = create_engine('sqlite:///db/platepal.db')
Session = sessionmaker(bind=engine)
session = Session()



if __name__ == '__main__':
    playsound('backgroundmusic.mp3', False)
    playsound('ambience.mp3', False)

    print('''
 ________    __         ________    ________   ________
|    _   \  |  |       /    _   \  |__    __| |   _____|
|   (_)   | |  |       |   (_)   |    |  |    |  |
|  ______/  |  |       |   ___   |    |  |    |  |__
|  |        |  |       |  |   |  |    |  |    |   __|
|  |        |  |       |  |   |  |    |  |    |  |
|  |        |  |_____  |  |   |  |    |  |    |  |_____
|__|        |________| |__|   |__|    |__|    |________|
             ________    ________    __
            |    _   \  /    _   \  |  |
            |   (_)   | |   (_)   | |  |
            |  ______/  |   ___   | |  |
            |  |        |  |   |  | |  | 
            |  |        |  |   |  | |  |
            |  |        |  |   |  | |  |_____
            |__|        |__|   |__| |________|
            
    ''')
    
    ingredients = session.query(Ingredient)
    create_ingredients_table(ingredients)
    add_ingredient(session)

