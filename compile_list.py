"""
This programme enables me to compile a shopping list of all the ingridients neded to 
cook any combination of the various batch cook meals I regularly cook.
It then takes this list and sorts the ingridients into a shopping list 
the list is orded by the section of the supermarket that the items can be found in.

"""

import json


BATCH_COOKS_FILE = "batch_cooks.json"
INGREDIENTS_CAT_FILE = "ingredients_cat.json"


def main():
    batch_cooks = read_file(BATCH_COOKS_FILE)
    meal_list = get_meal_list(batch_cooks)
    ingredients_totals = get_ingredients_totals(meal_list, batch_cooks)
    shopping_list = get_shopping_list(ingredients_totals, INGREDIENTS_CAT_FILE)
    print_nested_dict(shopping_list, 0)


def print_nested_dict(dict_obj, indent = 0):
    ''' 
    Prints nested dictionary with a given indent level
    And excludeds and ingredients that have a total of less than 1.
    in: a nested dictionary
        an indent
    out: printed dictionary
    
    '''
    #   Iterate over all key-value pairs of dictionary.
    for key, value in dict_obj.items():
        #   If value is a dict, then print nested dict. 
        if isinstance(value, dict):
            print(" " * indent + str(key) + ": ")
            print_nested_dict(value, indent + 4)
            print(" ")
        #   If the value isn't a dictionary.
        else:
            # And if the value is greater than 0, print the key:value pair.
            if value > 0:
                print(" " * indent + str(key) + " : " + str(value))


def read_file(filename):

    #   Reads json file and returns it.
    with open(filename) as f:
        new_dictionary = json.load(f)

    return new_dictionary


def get_meal_list(batch_cooks):
    """
        Gets a list of what meals the user wants to cook from batch_cooks dictionary:
        in: batch_cooks dictonary
        out: returns a list of meals the user wants to cook
    """

    print("Below is a list of the available batch cookes:")
    #   Prints the meals available in batch_cooks.
    for key in batch_cooks.keys():
        print(str(key))

    #   Creates list of meals available in batch_cook for use in is_valid_choice.
    batch_cooks_list = list(batch_cooks.keys())
    #print(batch_cooks_list)

    #   Asks user to select the meals that they want to cook and compiles a list.
    meal_list = []
    while True:
        choice = str(input("Enter a meal from the list above or 'f' to finish. "))
        # if choice is available in the batch_cook_dict
        if is_valid_choice(choice, batch_cooks_list):
            meal_list.append(choice)
        # if the choice is "f"
        elif choice == "f":
            print("You have selected " + str(meal_list))
            #   checks if the user is happy with their selections and enables them to rewrite the list if not.
            happy = are_you_happy(meal_list)
            if happy == True:
                print()
                return meal_list
            else:
                meal_list = []
                print("Let's start again.")
        # if the choice is none of the above.
        else:
            print("That selection is not available.")
            print("Please note that the selection is case sensitive.")


def are_you_happy(meal_list):
    while True:
        happy = str(input("Are you happy with your selection? y/n: "))
        if happy == "y":
            return True
        elif happy == "n":
            return False
        else:
            print("Please type 'y' for yes or 'n' for no.")


def is_valid_choice(choice, batch_cooks_list):
    """
        Checks to see if the given meal choice can be found in the given batch_cook_list.
        in: batch_cook_list
        out:returns true or false
    
    NB
    I could code so that the choice is not cap sensitive but it would cause consiquenses further on in the code.
    I decided not to resolve this issue this way for now.
    # if choice.casefold() in map(str.casefold, batch_cooks_list):
   """ 
    
    if choice in batch_cooks_list:
       return True
    else:
        return False


def get_ingredients_totals(meal_list, d):
    """
        use the list of selected batch cooks to compile a dictionary contating 
        the required ingridients and the total amount of each ingredients in key:value pairs.
        in: batch_cook.json
            list of intended batch cooks
        out:dictionary of needed ingredients and total amount needed
    """

    ingredients_totals = {}

    #   for each meal in meal_list
    for meal in meal_list:
        #print(meal)
        #print(d[meal])
        #   For each key in the selected meal's ingredients sub dictionary.
        for k in d[meal]['ingredients']:
            #print(str(k) + ': ' + str(d[meal]['ingredients'][k]))
            #   if ingredients is already in ingredients_totals update the total.
            if k in ingredients_totals:
                #do i need to set up a true fale to avoid errorr?
                ingredients_totals[k] += d[meal]['ingredients'][k]
            #   if ingridient isn't already in ingredients_totals append the new key:value pair.
            else:
                ingredients_totals[k] = d[meal]['ingredients'][k]

    return ingredients_totals


def get_shopping_list(ingredients_totals, INGREDIENTS_CAT_FILE):
    """
        uses ingredients_cat.json to creat a structured shopping list.
        use the dictionary of ingredients_totals to update the structured shopping list
        in: ingredients_cat.json
            dict of shopping list:volume
        out:dict structred shopping list
    """

    #   reads the ingredients_cat_file and creats a dictionary
    ingredients_cat_dict = read_file(INGREDIENTS_CAT_FILE)
    #   reverses the ingredients_cat_dict into a more convienient dictionary of catagories, that contain lists of ingredients.
    shopping_list_skeleton = reverse_and_nest(ingredients_cat_dict)
    #   goes through every category in shopping_list_skeleton
    for category in shopping_list_skeleton:
        #   goes through every item in the selected category of shopping_list_skeleton.
        for item in shopping_list_skeleton[category]:
        #   if the item is also in ingredients_totals
            if item in ingredients_totals:
                #   allocate the value from the item in ingredients_totals to the item in shopping_list_skeleton
                shopping_list_skeleton[category][item] = ingredients_totals[item]
    
    return shopping_list_skeleton


def reverse_and_nest(original):
    """
    Reverses the key:value pairs of a dictioanry
    stores the old keys in a nested dictionary as keys to a new value 0.
    where there are duplicates old values it will add the associated old key to the new nested dictionary with the value 0 .
    in: a dictionary
    out: returns a dictionary.
    """
    reversed_dict = {}

    #   for every key in the original dictionary.
    for old_key in original:
        old_value = original[old_key]
        #   if the old value is not already in reversed_dict.
        if old_value not in reversed_dict:
            #   {old value becomes new key:{old key becomes part of a new nested dictionary: and is assigned the value 0}} 
            reversed_dict[old_value] = {old_key:0}
        #   if the old value is already a new key in the reversed_dict.
        else:
            #   old key is added to the associated nested dictionary and is assigned the value 0 
            reversed_dict[old_value][old_key] = 0#.append(old_key:0)
    #for key in reversed_dict:
        #print(key, '->', reversed_dict[key])

    return reversed_dict


if __name__ == "__main__":
    main()
