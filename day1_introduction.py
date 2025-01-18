# Day1_Introduction
print(3 + 2)   # addition(+)
print(3 - 2)   # subtraction(-)
print(3 * 2)   # multiplication(*)
print(3 / 2)   # division(/)
print(3 ** 2)  # exponential(**)
print(10 % 4)   # modulus(%) That means remainder of division
print(3 // 2)  # Floor division operator(//)

# Checking data types

print(type(10))                  # Integer
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type('Jahid'))             # String
print(type([1, 2, 3]))           # List
print(type({'name':'Jahid'}))    # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple
print(type(3 == 3))              # Bool
print(type(3 >= 3))              # Bool

#For new line
print("The itsy bitsy spider\nclimbed up the waterspout.")
'''Output
The itsy bitsy spider
climbed up the waterspout.
'''
#multiple arguments
print("The itsy bitsy spider" , "climbed up" , "the waterspout.")
# Out put
#The itsy bitsy spider climbed up the waterspout.

#Positional arguments
print("My name is", "Python.")
print("Monty Python.")
'''Out put
My name is Python.
Monty Python.
'''
#Keyword arguments
print("My name is", "Python.", end=" ")
print("Monty Python.")
'''Out put
My name is Python. Monty Python.
'''
#keyword argument that can do this is named sep (as in separator).
print("My", "name", "is", "Monty", "Python.", sep="-")
'''Out put
My-name-is-Monty-Python.
'''
#Both keyword arguments may be mixed in one invocation
print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
#Output: My_name_is*Monty*Python.*

#print() function and its arguments
print("Programming","Essentials","in", sep="***", end="...")
print("Python")
#Output: Programming***Essentials***in...Python

#Formatting the output
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
#minimize the number of print() function invocations by inserting the \n sequence into the strings; altr way
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")

#Python literals - strings
print('"I\'m"\n"\"learning\""\n"\"\"Python\"\"\"')
'''Output
"I'm"
""learning""
"""Python"""
'''
