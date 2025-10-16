#Tamer's LAMBDA Examples (Practice)

# <1> Example of how a function works (in Python)
# [A function for Exponents]
def square(x):
    return x * x
print("Squared (normal):", square(5))

# RESULT --> Squared (normal): 25

# ---------------------------------------------------------------

# <2> Example of how a LAMBDA style works(in Python)
# [A LAMBDA Style for Exponents]
square_lambda = lambda x: x * x
print("Square (lambda):", square_lambda(5))

# RESULT --> Squared (lambda): 25

# ---------------------------------------------------------------
# (Syntax): lambda arguments: expression
# (Note): Lambdas can only contain one expression (no loops or statements inside).
# Useful when you just need a quick function once.
#    |
#    |
#    |
#    V
# ---------------------------------------------------------------

# <3> Example of 'Tamer's' LAMBDA Exponent function for the doubled number
thsquared_lambda = lambda folders: folders * folders
print("Squared (lambda) Folders:", thsquared_lambda(10))

# RESULT --> Squared (lambda) Folders: 100
 
# ---------------------------------------------------------------
# =======================================
# Higher-Order Functions
# =======================================
# A higher-order function is a function that either:
#   1. Takes another function as input
#   2. Returns a function as output
#
# Python has several built-in higher-order functions.
# The most common ones are map(), filter(), and reduce().
#    |
#    |
#    |
#    V
# ---------------------------------------------------------------------

# <4> Higher-Order Functions Practice !!!
# 
# =======================================
# 1. Use map() with a lambda to triple each number in nums.

nums = [1, 2, 4, 8] # <----- The 'nums' Array

tripler = list(map(lambda x: x * 3, nums))# <----- Our 'tripler' function

print(tripler)

# RESULT --> [6, 12, 24]


# 2. Use filter() with a lambda to get numbers greater than 2.

above_two = list(filter(lambda x: x % 2 == 0, nums)) # <---- Our 'above_two' function

print(above_two)

# RESULT --> [2, 4, 8]

# 3. Use reduce() with a lambda to multiply all numbers in nums.

from functools import reduce # <----- We must import the 'reduce'
# function because it is a PYTHON "Module"

multiplier = reduce(lambda x, y: x * y, nums) # <---- Our 'multiplier' function
print(multiplier)

# RESULT --> 64

