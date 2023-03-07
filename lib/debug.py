#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Recipe, Ingredient, RecipeIngredient

if __name__ == '__main__':
    engine = create_engine('sqlite:///db/platepal.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb; ipdb.set_trace()