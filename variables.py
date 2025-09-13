


newInt = 1

#String Examples
newString = "Hello! This is my String for this Camp :)"

#Float Examples
newFloat = 1.2534312323

#Boolean Examples
newBool = False

#Slicing Example
brand = "McDonald's"
print (brand)
print (brand[2:-2])
newfString = f"The value of newInt is {newInt}"
print(newfString)

#TYPECASTING Example

typeCastExample = "10"
typeCastInt = int(typeCastExample)
print(typeCastExample)
print(1 + float(typeCastInt))
fakeBoolean = "True"
realBoolean = bool(fakeBoolean)
fakeInt = 1.9999999
realInt = int(fakeInt)
print(int(fakeInt))
  
def add10(a):
    return + 10

#BOOLEAN Example 
x = 4
if x > 5:
    print("x is greater than 5")
    x = x-1
    print("x is equal to 5")
else:
    print("x is less than 5")


#WHILE Examples
#count = 0
#    while count < 3:
    

#FOR Examples
for i in range(3):
    if i == 1:
        continue
    print("Iteration", i)
    #count *= 1

#Lists Examples 
newList = [[1, 2, 3, 4, 5], ["one", "two", "three", "four", "five"]]
newList.append(2)
extraList = list([1, 2, 3])

newTuple = (1, 2, 3, 4, 5)

newSet = {1, 2, 3, 4, 5}
newSet.add(6)
print(newSet)

#Dictionary Example
newDictionary = { 1: "Water Bottle", 2: "Bicycle", 3: ("Goat", "Cheese") }
print(newDictionary[2])



def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")
greet("Bob", "Hi")


#MORE Examples 'Range'
list = [1, 2, 3]
list2 = [4, 5, 6]
#print(len(list))

print(list)
print(list(map(add10, list, list2)))

#for i in range(5):
 #   print(i)    

for idx, val in enumerate(list):
    if(val == 3):
        print("You found 3!")
    else:
        print("no 3 here :(")

#Zip Examples
Player = ['Landon', 'Ted', 'Freddy']
Point = [30, 67, 92]
print(list(zip(Player, Point)))

print(list(filter(lambda x: x > 1, list)))


x = "global"
print(x)

#Scopes Example
 
def outer():
    x = "outer"
    print(x) 

def inner():
    nonlocal x
    x = "inner"
    print(x)


    
    
def change_global():
    global x 
    x = "changed global"

    print(x)
    outer()
    print(x)
    change_global()
    print(x)

