with open("input.txt","r") as f:
    data = f.read().splitlines()

food = {}
safe_ing = set()
all_ing = []

for i in data:
    ingredients, allergens = i.split(" (contains ")
    allergens = allergens[:-1]
    ingredients = ingredients.split(" ")
    all_ing.extend(ingredients)
    unique_in = set(ingredients)
    safe_ing=safe_ing.union(unique_in)
    allergens = allergens.split(", ")
    for allergen in allergens:
        if food.get(allergen) is None:
            food[allergen] = unique_in
        else:
            food[allergen] = food[allergen].intersection(unique_in)

safe_ing = safe_ing.difference(set(k for value in food.values() for k in value))
safe_count = sum([ingredient in safe_ing for ingredient in all_ing])

print(f"Part 1: {safe_count}")

while any([len(i) > 1 for i in food.values()]):    
    for a, i in food.items():                      
        if len(i) == 1:                                 
            alg = list(i)[0]                            
            for a2, i2 in food.items():            
                if a2 == a:                             
                    continue                            
                if len(i2) > 1:                         
                    if alg in i2:                       
                        food[a2].remove(alg)       



names = list(food.keys())                          
names.sort()                                            
print("Part 2: ", ",".join([",".join(food[i]) for i in names]))


