from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, Float, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    instructions = Column(String())

    recipe_ingredients = relationship('RecipeIngredient', backref=backref('recipe'))
    # ingredients = relationship('Ingredient')

    # recipe_ingredients = Column(Integer(), ForeignKey('recipes.id'))

    def __repr__(self):
        return f'id: {self.id}, ' + \
            f'name: {self.name}, ' + \
            f'ingredients: {self.recipe_ingredients}, ' + \
            f'instructions: {self.instructions}, '


class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    recipe_ingredients = relationship('RecipeIngredient', backref=backref('ingredient'))

    def __repr__(self):
        return f'id: {self.id}, ' + \
            f'name: {self.name}'
    

class RecipeIngredient(Base):
    __tablename__ = 'recipe_ingredients'
    
    id = Column(Integer(), primary_key=True)
    quantity = Column(Float())
    unit = Column(String())
    recipe_id = Column(Integer(), ForeignKey('recipes.id'))
    ingredient_id = Column(Integer(), ForeignKey('ingredients.id'))

    def __repr__(self):
        return f'id: {self.id}, ' + \
            f'quantity: {self.quantity}, ' + \
            f'unit: {self.unit}, ' + \
            f'recipe_id: {self.recipe_id}, ' + \
            f'ingredient_id: {self.ingredient_id}'
