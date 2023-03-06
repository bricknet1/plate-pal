from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, Float, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    recipe_ingredients = Column(Integer())


class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    

class RecipeIngredient(Base):
    __tablename__ = 'recipe_ingredients'

    id = Column(Integer(), primary_key=True)
    recipe_id = Column(Integer())
    ingredient_id = Column(Integer())
    quantity = Column(Float())
    unit = Column(String())