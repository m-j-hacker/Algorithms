#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    # variable for the limiting reagent of the recipe
    smallest = None
    # loop to search for key
    for key in recipe:
        # check if key is in ingredients
        if key not in ingredients:
            return 0
        # divide the ingredient by its requirement
        result = ingredients[key] // recipe[key]
        # check if result == 0
        if result == 0:
            # no batches possible, so return 0
            return 0
        # check if smallest is None or result < smallest
        elif smallest is None or result < smallest:
            smallest = result
    return smallest  


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))