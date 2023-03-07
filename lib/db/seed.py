from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Ingredient, RecipeIngredient, Recipe

if __name__ == '__main__':
    engine = create_engine('sqlite:///platepal.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Ingredient).delete()
    session.query(Recipe).delete()
    session.query(RecipeIngredient).delete()

    # ingredients = [
    #     "Flour",
    #     "Sugar",
    #     "Eggs",
    #     "Milk",
    #     "Salt",
    #     "Pepper",
    #     "Olive oil",
    #     "Butter",
    #     "Garlic",
    #     "Onion",
    #     "Tomatoes",
    #     "Cheese",
    #     "Chicken",
    #     "Beef",
    #     "Fish",
    #     "Rice",
    #     "Pasta",
    #     "Lemon",
    #     "Basil",
    #     "Oregano",
    #     "Thyme",
    #     "Cumin",
    #     "Paprika",
    #     "Ginger",
    #     "Soy sauce"
    # ]

    # recipe_names = ["The baked Tricia", "Braised Stove", "A big scoop of Nick"]

    # for recipe in recipe_names:
    #     new_recp = Recipie(
    #         name=recipe
    #     )
    #     for _ in range (random.randint(1,3)):
    #         ingredient = Ingredient(
    #             name=random.choice(ingredients)
    #         )

    recipe = Recipe(
        name="Fart Chicken"
    )

    session.add(recipe)
    session.commit()

    ingredient = Ingredient(
        name="Fart"
    )
    ingredient2 = Ingredient(
        name="Chicken"
    )

    session.add(ingredient)
    session.add(ingredient2)
    session.commit()

    recipeingredient = RecipeIngredient(
        quantity=2.0,
        unit="Gallons",
        recipe_id=1,
        ingredient_id=1
    )

    recipeingredient2 = RecipeIngredient(
        quantity=1.0,
        unit="Whole Bird",
        recipe_id=1,
        ingredient_id=2
    )

    session.add(recipeingredient)
    session.add(recipeingredient2)
    session.commit()