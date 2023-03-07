from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Ingredient, RecipeIngredient, Recipe

if __name__ == '__main__':
    engine = create_engine('sqlite:///db/platepal.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Ingredient).delete()
    session.query(Recipe).delete()
    session.query(RecipeIngredient).delete()

    recipe_list = ["Spaghetti Carbonara", "Spaghetti with Tomato Sauce and Meatballs", "Penne with Tomato Sauce and Mozzarella", "Garlic Shrimp Linguine", "Creamy Mushroom Pasta"]

    for rec in recipe_list:
        all_recs = Recipe(name=f"{rec}")
        session.add(all_recs)
        session.commit()

    ingredients_list = ['Spaghetti','Penne','Fettuccine','Macaroni','Linguine','Tomatoes','Garlic','Olive oil','Parmesan cheese','Basil','Mozzarella cheese','Onions','Oregano','Salt','Black pepper','Red pepper flakes','Ground beef','Chicken','Shrimp','Lemon','Spinach','Ricotta cheese','Mushrooms','Bell peppers','Zucchini','Eggplant','Butter','Cream','Anchovies']

    for ing in ingredients_list:
        all_ings = Ingredient(name=f"{ing}")
        session.add(all_ings)
        session.commit()

recipeingredient1 = RecipeIngredient(
    quantity=8,
    unit="oz",
    recipe_id=1,
    ingredient_id=1
)

recipeingredient2 = RecipeIngredient(
    quantity=2,
    unit="cloves",
    recipe_id=1,
    ingredient_id=7
)

recipeingredient3 = RecipeIngredient(
    quantity=3,
    unit="tbsp",
    recipe_id=1,
    ingredient_id=8
)

recipeingredient4 = RecipeIngredient(
    quantity=1,
    unit="cup",
    recipe_id=1,
    ingredient_id=9
)

recipeingredient5 = RecipeIngredient(
    quantity=2,
    unit="tbsp",
    recipe_id=1,
    ingredient_id=10
)

recipeingredient6 = RecipeIngredient(
    quantity=1,
    unit="pinch",
    recipe_id=1,
    ingredient_id=14
)

recipeingredient7 = RecipeIngredient(
    quantity=2,
    unit="oz",
    recipe_id=1,
    ingredient_id=28
)

recipeingredient8 = RecipeIngredient(
    quantity=4,
    unit="oz",
    recipe_id=1,
    ingredient_id=31
)

recipeingredient9 = RecipeIngredient(
    quantity=2,
    unit="tbsp",
    recipe_id=1,
    ingredient_id=32
)

#######################################################
#######################################################
#######################################################
#######################################################

recipeingredient10 = RecipeIngredient(
    quantity=1,
    unit="pound",
    recipe_id=2,
    ingredient_id=1
)

recipeingredient11 = RecipeIngredient(
    quantity=1,
    unit="can",
    recipe_id=2,
    ingredient_id=6
)

recipeingredient12 = RecipeIngredient(
    quantity=2,
    unit="clove",
    recipe_id=2,
    ingredient_id=7
)

recipeingredient13 = RecipeIngredient(
    quantity=2,
    unit="tablespoon",
    recipe_id=2,
    ingredient_id=8
)

recipeingredient14 = RecipeIngredient(
    quantity=1,
    unit="cup",
    recipe_id=2,
    ingredient_id=9
)

recipeingredient15 = RecipeIngredient(
    quantity=2,
    unit="teaspoon",
    recipe_id=2,
    ingredient_id=10
)

recipeingredient16 = RecipeIngredient(
    quantity=1,
    unit="cup",
    recipe_id=2,
    ingredient_id=11
)

recipeingredient17 = RecipeIngredient(
    quantity=1,
    unit="teaspoon",
    recipe_id=2,
    ingredient_id=12
)

recipeingredient18 = RecipeIngredient(
    quantity=1/2,
    unit="teaspoon",
    recipe_id=2,
    ingredient_id=13
)

recipeingredient19 = RecipeIngredient(
    quantity=1/4,
    unit="teaspoon",
    recipe_id=2,
    ingredient_id=14
)

recipeingredient20 = RecipeIngredient(
    quantity=1/4,
    unit="teaspoon",
    recipe_id=2,
    ingredient_id=15
)

recipeingredient21 = RecipeIngredient(
    quantity=1/2,
    unit="pound",
    recipe_id=2,
    ingredient_id=16
)

recipeingredient22 = RecipeIngredient(
    quantity=1,
    unit="cup",
    recipe_id=2,
    ingredient_id=5
)

recipeingredient23 = RecipeIngredient(
    quantity=1/4,
    unit="cup",
    recipe_id=2,
    ingredient_id=18
)

recipeingredient24 = RecipeIngredient(
    quantity=1/2,
    unit="pound",
    recipe_id=2,
    ingredient_id=26
)
##################################################
##################################################
##################################################
##################################################

recipeingredient3 = RecipeIngredient(
    quantity=1,
    unit="pound",
    recipe_id=3,
    ingredient_id=2
)

recipeingredient25 = RecipeIngredient(
    quantity=1,
    unit="can",
    recipe_id=3,
    ingredient_id=6
)

recipeingredient26 = RecipeIngredient(
    quantity=1,
    unit="cup",
    recipe_id=3,
    ingredient_id=8
)

recipeingredient27 = RecipeIngredient(
    quantity=1,
    unit="cup",
    recipe_id=3,
    ingredient_id=9
)

recipeingredient28 = RecipeIngredient(
    quantity=1/2,
    unit="teaspoon",
    recipe_id=3,
    ingredient_id=13
)

recipeingredient29 = RecipeIngredient(
    quantity=1/2,
    unit="teaspoon",
    recipe_id=3,
    ingredient_id=14
)

recipeingredient30 = RecipeIngredient(
    quantity=1/4,
    unit="teaspoon",
    recipe_id=3,
    ingredient_id=16
)

recipeingredient31 = RecipeIngredient(
    quantity=1/2,
    unit="pound",
    recipe_id=3,
    ingredient_id=10
)

recipeingredient32 = RecipeIngredient(
    quantity=1/2,
    unit="cup",
    recipe_id=3,
    ingredient_id=4
)

recipeingredient33 = RecipeIngredient(
    quantity=1,
    unit="cup",
    recipe_id=3,
    ingredient_id=11
)
#######################################
#######################################
#######################################
#######################################

recipeingredient34 = RecipeIngredient(
        quantity=8,
        unit="ounces",
        recipe_id=4,
        ingredient_id=1
    )

recipeingredient35 = RecipeIngredient(
        quantity=2,
        unit="cloves",
        recipe_id=4,
        ingredient_id=7
    )

recipeingredient36 = RecipeIngredient(
        quantity=2,
        unit="tablespoons",
        recipe_id=4,
        ingredient_id=8
    )

recipeingredient37 = RecipeIngredient(
        quantity=1,
        unit="cup",
        recipe_id=4,
        ingredient_id=5
    )

recipeingredient38 = RecipeIngredient(
        quantity=1/2,
        unit="cup",
        recipe_id=4,
        ingredient_id=10
    )

recipeingredient39 = RecipeIngredient(
        quantity=1/4,
        unit="cup",
        recipe_id=4,
        ingredient_id=16
    )

recipeingredient40 = RecipeIngredient(
        quantity=1/4,
        unit="teaspoon",
        recipe_id=4,
        ingredient_id=14
    )

recipeingredient41 = RecipeIngredient(
        quantity=1/4,
        unit="teaspoon",
        recipe_id=4,
        ingredient_id=15
    )

recipeingredient42 = RecipeIngredient(
        quantity=1/2,
        unit="pound",
        recipe_id=4,
        ingredient_id=19
    )

recipeingredient43 = RecipeIngredient(
        quantity=1,
        unit="lemon",
        recipe_id=4,
        ingredient_id=20
    )
#######################################
#######################################
#######################################
#######################################

recipeingredient44 = RecipeIngredient(
    quantity=8,
    unit="oz",
    recipe_id=5,
    ingredient_id=4
)

recipeingredient45 = RecipeIngredient(
    quantity=1,
    unit="tbsp",
    recipe_id=5,
    ingredient_id=7
)

recipeingredient46 = RecipeIngredient(
    quantity=2,
    unit="tbsp",
    recipe_id=5,
    ingredient_id=8
)

recipeingredient47 = RecipeIngredient(
    quantity=1,
    unit="cup",
    recipe_id=5,
    ingredient_id=22
)

recipeingredient48 = RecipeIngredient(
    quantity=1,
    unit="tsp",
    recipe_id=5,
    ingredient_id=13
)

recipeingredient49 = RecipeIngredient(
    quantity=1/2,
    unit="tsp",
    recipe_id=5,
    ingredient_id=14
)

recipeingredient50 = RecipeIngredient(
    quantity=1/4,
    unit="tsp",
    recipe_id=5,
    ingredient_id=16
)

recipeingredient51 = RecipeIngredient(
    quantity=1/2,
    unit="cup",
    recipe_id=5,
    ingredient_id=28
)

recipeingredient52 = RecipeIngredient(
    quantity=1/4,
    unit="cup",
    recipe_id=5,
    ingredient_id=9
)

session.add(recipeingredient1)
session.add(recipeingredient2)
session.add(recipeingredient3)
session.add(recipeingredient4)
session.add(recipeingredient5)
session.add(recipeingredient6)
session.add(recipeingredient7)
session.add(recipeingredient8)
session.add(recipeingredient9)
session.add(recipeingredient10)
session.add(recipeingredient11)
session.add(recipeingredient12)
session.add(recipeingredient13)
session.add(recipeingredient14)
session.add(recipeingredient15)
session.add(recipeingredient16)
session.add(recipeingredient17)
session.add(recipeingredient18)
session.add(recipeingredient19)
session.add(recipeingredient20)
session.add(recipeingredient21)
session.add(recipeingredient22)
session.add(recipeingredient23)
session.add(recipeingredient24)
session.add(recipeingredient25)
session.add(recipeingredient26)
session.add(recipeingredient27)
session.add(recipeingredient28)
session.add(recipeingredient29)
session.add(recipeingredient30)
session.add(recipeingredient31)
session.add(recipeingredient32)
session.add(recipeingredient33)
session.add(recipeingredient34)
session.add(recipeingredient35)
session.add(recipeingredient36)
session.add(recipeingredient37)
session.add(recipeingredient38)
session.add(recipeingredient39)
session.add(recipeingredient40)
session.add(recipeingredient41)
session.add(recipeingredient42)
session.add(recipeingredient43)
session.add(recipeingredient44)
session.add(recipeingredient45)
session.add(recipeingredient46)
session.add(recipeingredient47)
session.add(recipeingredient48)
session.add(recipeingredient49)
session.add(recipeingredient50)
session.add(recipeingredient51)
session.add(recipeingredient52)
session.commit()