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

# Syntax: lambda arguments: expression
# Note: Lambdas can only contain one expression (no loops or statements inside).
# Useful when you just need a quick function once.

# ---------------------------------------------------------------

# <3> Example of 'My' LAMBDA Exponent function for the doubled number
thsquared_lambda = lambda folders: folders * folders
print("Squared (lambda) Folders:", thsquared_lambda(10))

# RESULT --> Squared (lambda) Folders: 100
 
# ---------------------------------------------------------------

# <4>

# Higher-Order Functions Practice !!!
# =======================================
# 1. Use map() with a lambda to triple each number in nums.
def from_two(num):
    return num + 2

nums = [2, 4, 8]
list(map(from_two, nums))




# 2. Use filter() with a lambda to get numbers greater than 2.
# 3. Use reduce() with a lambda to multiply all numbers in nums.
# Print your results!



