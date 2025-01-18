# Arithmetic Operations in Python
# Integers
print('Addition:', 1 + 2)
print('Subtraction or diff:', 2 - 1)
print('Multiplication:', 2 * 3)
# Division in python gives floating number
print ('Division:', 4 / 2)
print('Division:', 6 / 2)
print('Division:', 7 / 2)
# Floor Division is shown by // the double slash
print('Floor Division:', 4 // 2)
print('Floor Division:', 6 // 2)
print('Floor Division:', 7 // 2)
# Gives the remainder
print('Modulus or Remainder:', 3 % 2)
print('Exponential:', 3 ** 2)
# Floating numbers
print(f'Floating Number: PI is', 3.14)
print(f'Floating Number: Gravity is', 9.81)
# Complex numbers
print('Complex number:', 1 + 1j)
print('Multiplying complex number:',(1 + 1j) * (1-1j) * (2+3j))
# Declaring the variable at the top first
a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type
# Declaring values and organizing them together
num_one = 3
num_two = 4
# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_two
remainder = num_two % num_one
# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)
# Calculating area of a circle, we know that area of circle pi*r^2
radius = 10
area_of_circle = 3.14 * radius ** 2
print('Area of a circle:', area_of_circle)
# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)
# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print("Weight:",weight, 'N')
#Boolean
print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
#Length with boolean
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False
# Boolean comparison
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)
# Another way comparison
print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('a in Jahid', 'a' in 'Jahid')       # True - a found in the string
print('E in Meher', 'E' in 'Meher')       # False -there is no uppercase E
print('e in Meher', 'e' in 'Meher')       # True -there is e lowercase
print('coding' in 'coding for all')       # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')            # True
print('4 is 2 ** 2:', 4 is 2 ** 2)        # True
#More boolean
print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statement is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)       # False - because 3 > 2 is true, then not True gives False
print(not 1)           # False - Negation, the not operator turns true to false
print(not False)       # True
print(not not True)    # True
print(not not False)   # False
print(not not 1)       # True
"""not not 1
In Python, truthy and falsy values determine the Boolean value of an object:
1 is a truthy value (non-zero numbers are truthy).
not 1 → False
not False → True
Result: True
"""
print(not not 0)       # False
"""not not 0
In Python, truthy and falsy values determine the Boolean value of an object:
0 is a falsy value (zero is falsy).
not 0 → True
not True → False
Result: False
"""

#Operators and Their Bindings
print(9 % 6 % 2)
#from left to right: first 9 % 6 gives 3, and then 3 % 2 gives 1
print(2 ** 2 ** 3)
#2 ** 3 → 8; 2 ** 8 → 256, The result clearly shows that the exponentiation operator uses right-sided binding.

print(2 * 3 % 5)
'''Both operators (* and %) have the same priority, so the result can be guessed only when you know the binding direction.
result is 1
'''

#subexpressions in parentheses are always calculated first.
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
#output 10

#Keynotes
''' 
1. A unary operator is an operator with only one operand, e.g., -1, or +3.
2. A binary operator is an operator with two operands, e.g., 4 + 5, or 12 % 5.
3. Some operators act before others - the hierarchy of priorities:
the ** operator (exponentiation) has the highest priority;
then the unary + and - (note: a unary operator to the right of the exponentiation operator binds more strongly, for example 4 ** -1 equals 0.25)
then: *, /, and %,
and finally, the lowest priority: binary + and -.
4. Subexpressions in parentheses are always calculated first, e.g., 15 - 1 * (5 * (1 + 2)) = 0.
5. The exponentiation operator uses right-sided binding, e.g., 2 ** 2 ** 3 = 256.
'''
