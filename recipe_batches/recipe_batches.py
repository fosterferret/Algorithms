#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    if set(recipe.keys()).issubset(set(ingredients.keys())):
        batches, max_batches = 0, math.inf
        for required_ingredient in recipe:
            batches = ingredients[required_ingredient] // recipe[required_ingredient]
            max_batches = batches if batches < max_batches else max_batches
        return max_batches
    else:
      return 0


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
