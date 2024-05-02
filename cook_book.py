
import pprint

def add_new_rec(): # add new recipe to recipes file
    with open("recipes.txt", "a") as f:    
        rec_name = input("Введите название рецепта: ")
        iingredients_amount = int(input("Введите количество ингридиентов: "))
        f.write(f"{rec_name}\n{iingredients_amount}\n")
        i = 1
        while i <= iingredients_amount:
            ingrdient_name = input(f"Введите название ингридиента {i}: ")
            ingredient_amount = int(input(f"Введие количество ингридиента {i}: "))
            ingredient_pcs = input(f"Введие единицы измерения количества ингридиента {i}: ")
            f.write(f"{ingrdient_name} | {ingredient_amount} | {ingredient_pcs}\n")
            f.write("\n")
            i += 1

def create_cook_book(recipe_file): # create cook book from recipes file
    
    cook_book = {}
    
    # pack recipes from file to list
    with open(recipe_file, "r", encoding='utf-8') as f: 
        lst = [] # tmp list to store ingredient information (name, quantity, measure)
        rec_lst = [] # list of lists with recipes
        for l in f: # iterate file line by line
            if l == "": # if reached empty line, stop iteration, reached end of file
                break
            elif l == "\n": # if reached line break, add recipe to list, go to next line
                rec_lst.append(lst)
                lst = []
            else:
                lst.append(l.strip())
        rec_lst.append(lst)        
    
    # unpack list of recipes to dict
    for rec in rec_lst: 
        key, n, *values = rec # varible n (number of ingredients) is not used
        lst = [] # tmp list to store information of all ingredients (as dicts) for one recipe
        for value in values:
            str_value = value.split(" | ") # delete string separator and returns list of information of ingredient
            v_ingredient_name, v_quantity, v_measure = str_value
            ing_dict = {"ingredient_name" : v_ingredient_name, "quantity" : v_quantity, "measure" : v_measure}
            lst.append(ing_dict)
        cook_book[key] = lst
    # pprint.pp(cook_book, width=150) # use this to check if function correctly works
    return cook_book
    
def get_shop_list_by_dishes(dishes, person_count):
    pass


# add_new_rec() # use this tupdate recipe.txt file with new recipe  
# add_new_rec() # use this tupdate recipe.txt file with new recipe   
# add_new_rec() # use this tupdate recipe.txt file with new recipe  
# add_new_rec() # use this tupdate recipe.txt file with new recipe 
            
# create_cook_book("recipes.txt")
        

    