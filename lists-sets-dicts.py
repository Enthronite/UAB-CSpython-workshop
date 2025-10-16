# Tamer's LISTS Examples (Practice)

# <1> Tamer's List

vegetables = ["lettuce", "carrots", "mushrooms"]
print("List:", vegetables)

# RESULT --> List: ['lettuce', 'carrots', 'mushrooms']

#---------------------------------------------------------------

# <2> Tamer's Indexed Item
print("Tamer's Favorite Veggie is:", vegetables[2])


# RESULT --> 
# List: ['lettuce', 'carrots', 'mushrooms']
# Tamer's Favorite Veggie is: mushrooms

#---------------------------------------------------------------

# <3> Tamer's Forgotten Favorite
vegetables.append("cucumber")
print("Let me add one more item on there :>", vegetables)

# RESULT --> 
# List: ['lettuce', 'carrots', 'mushrooms']
# Tamer's Favorite Veggie is: mushrooms
# Let me add one more item on there :> ['lettuce', 'carrots', 'mushrooms', 'cucumber']

#---------------------------------------------------------------

# <4> Tamer's Indecisiveness
vegetables.remove("lettuce")
print("Wait! Let me remove 'lettuce' from there :<", vegetables)

# RESULT --> 
# List: ['lettuce', 'carrots', 'mushrooms']
# Tamer's Favorite Veggie is: mushrooms
# Let me add one more item on there :> ['lettuce', 'carrots', 'mushrooms', 'cucumber']
# Wait! Let me remove 'lettuce' from there :< ['carrots', 'mushrooms', 'cucumber']

#---------------------------------------------------------------

# <5> Tamer's Extra Mushroom
vegetables.append("shitake mushrooms")
print("There's another type of mushroom that I forgot to add on here :/", vegetables)

# RESULT --> 
# List: ['lettuce', 'carrots', 'mushrooms']
# Tamer's Favorite Veggie is: mushrooms
# Let me add one more item on there :> ['lettuce', 'carrots', 'mushrooms', 'cucumber']
# Wait! Let me remove 'lettuce' from there :< ['carrots', 'mushrooms', 'cucumber']
# There's another type of mushroom that I forgot to add on here :/ ['carrots', 'mushrooms', 'cucumber', 'shitake mushrooms']

#---------------------------------------------------------------

# <6> Tamer's Single Instance of CUCUMBER 'Removal'
for vegetable in vegetables[:]:
    if vegetable == 'cucumber':
        vegetables.remove(vegetable)
print(vegetables) 

# RESULT --> ['carrots', 'mushrooms', 'shitake mushrooms']

#---------------------------------------------------------------

# <7> Tamer's Lists 'REITERATED /:< (For/While)
print("\nIterating Vegetables (method 1: simple for-loop)")
for v in vegetables:
    print("Vegetable:", v)

print("\nIterating Vegetables (method 2: by index)")
for i in range(len(vegetables)):
    print("Index", i, "->", vegetables[i])

print("\nIterating Vegetables (method 3: enumerate for index + value)")
for i, v in enumerate(vegetables):
    print(f"Index {i} has {v}")

print("\nIterating vegetables (method 4: while-loop)")
i = 0
while i < len(vegetables):
    print("While loop ->", vegetables[i])
    i += 1

print("\nIterating vegetables (method 5: list comprehension)")
uppercased = [v.upper() for v in vegetables]
print("Uppercased:", uppercased)

print("\nIterating vegetables (method 6: unpacking with * operator)")
print(*vegetables) #prints items seperated by spaces

# RESULT --> 
'''
List: ['lettuce', 'carrots', 'mushrooms']
Tamer's Favorite Veggie is: mushrooms
Let me add one more item on there :> ['lettuce', 'carrots', 'mushrooms', 'cucumber']
Wait! Let me remove 'lettuce' from there :< ['carrots', 'mushrooms', 'cucumber']
There's another type of mushroom that I forgot to add on here :/ ['carrots', 'mushrooms', 'cucumber', 'shitake mushrooms']
['carrots', 'mushrooms', 'shitake mushrooms']

Iterating Vegetables (method 1: simple for-loop)
Vegetable: carrots
Vegetable: mushrooms
Vegetable: shitake mushrooms

Iterating Vegetables (method 2: by index)
Index 0 -> carrots
Index 1 -> mushrooms
Index 2 -> shitake mushrooms

Iterating Vegetables (method 3: enumerate for index + value)
Index 0 has carrots
Index 1 has mushrooms
Index 2 has shitake mushrooms

Iterating vegetables (method 4: while-loop)
While loop -> carrots
While loop -> mushrooms
While loop -> shitake mushrooms

Iterating vegetables (method 5: list comprehension)
Uppercased: ['CARROTS', 'MUSHROOMS', 'SHITAKE MUSHROOMS']

Iterating vegetables (method 6: unpacking with * operator)
carrots mushrooms shitake mushrooms
'''


