#variables in python
first_name = "Md Jahid"
last_name = "Islam"
country = "Finland"
citizenship = "Bangladeshi"
city = "Vantaa"
age = "26 years old"
skills = "HTML, PYTHON, DATA SCIENCE, AI, ML" #not using list
is_married = True
# Printing the values stored in the variables
print("First Name:", first_name)
print("First Name Length:", len(first_name))
print("Last Name:", last_name)
print("Last Name Length:", len(last_name))
print("Country:", country)
print("Citizenship:", citizenship)
print("City:", city)
print("Age:", age)
print("Skills:", skills)
print("Married:", is_married)
#or using the dictionary
my_info = {
    'first_name' : "Md Jahid",
    'last_name' : "Islam",
    'country' : "Finland",
    'citizenship' : "Bangladeshi",
    'city' : "Vantaa",
    'age' : "26 years old",
    'skills' : ["HTML", "PYTHON", "DATA SCIENCE", "AI", "ML"], #using list
    "is_married" : True
}
print(my_info)

# Declaring multiple variables in one line
first_name, last_name, country, citizenship, city, age, skills, is_married = "Md Jahid", "Islam", "Finland", "Bangladeshi", "Vantaa", "26 years old", ["HTML", "PYTHON", "DATA SCIENCE", "AI", "ML"], True
#we can print in one line
print(f"{first_name} {last_name} {country} {citizenship} {city} {age} {skills} {is_married}")
#or we can print individual
print("First Name:", first_name)
print("Last Name:", last_name)
print("Country:", country)
print("Citizenship:", citizenship)
print("City:", city)
print("Age:", age)
print("Skills:", skills)
print("Married:", is_married)

#Out put
"""First Name: Md Jahid
First Name Length: 8
Last Name: Islam
Last Name Length: 5
Country: Finland
Citizenship: Bangladeshi
City: Vantaa
Age: 26 years old
Skills: HTML, PYTHON, DATA SCIENCE, AI, ML
Married: True
{'first_name': 'Md Jahid', 'last_name': 'Islam', 'country': 'Finland', 'citizenship': 'Bangladeshi', 'city': 'Vantaa', 'age': '26 years old', 'skills': ['HTML', 'PYTHON', 'DATA SCIENCE', 'AI', 'ML'], 'is_married': True}
Md Jahid Islam Finland Bangladeshi Vantaa 26 years old ['HTML', 'PYTHON', 'DATA SCIENCE', 'AI', 'ML'] True
First Name: Md Jahid
Last Name: Islam
Country: Finland
Citizenship: Bangladeshi
City: Vantaa
Age: 26 years old
Skills: ['HTML', 'PYTHON', 'DATA SCIENCE', 'AI', 'ML']
Married: True
"""
'''
Here is a short story:

Once upon a time in Appleland, John had three apples, Mary had five apples, and Adam had six apples. They were all very happy and lived for a long time. End of story.

Your task is to:

create the variables: john, mary, and adam;
assign values to the variables. The values must be equal to the numbers of fruit possessed by John, Mary, and Adam respectively;
having stored the numbers in the variables, print the variables on one line, and separate each of them with a comma;
now create a new variable named total_apples equal to the addition of the three previous variables.
print the value stored in total_apples to the console;
experiment with your code: create new variables, assign different values to them, and perform various arithmetic operations on them (e.g., +, -, *, /, //, etc.). Try to print a string and an integer together on one line, e.g., "Total number of apples:" and total_apples.
'''
john=3
mary=5
adam=6
print(f"john={john},mary={mary},adam={adam}")
total_apples=john+mary+adam
print(total_apples)

'''output
john=3,mary=5,adam=6
14
'''

#Shorthand Operators in Python
'''
Operator	Equivalent Expression	    Description
+=	variable = variable + expression	Adds and assigns
-=	variable = variable - expression	Subtracts and assigns
*=	variable = variable * expression	Multiplies and assigns
/=	variable = variable / expression	Divides and assigns
//=	variable = variable // expression	Floor divides and assigns
%=	variable = variable % expression	Modulo and assigns
**=	variable = variable ** expression	Exponentiation and assigns
&=	variable = variable & expression	Bitwise AND and assigns
`	=`	`variable = variable
^=	variable = variable ^ expression	Bitwise XOR and assigns
>>=	variable = variable >> expression	Bitwise right shift and assigns
<<=	variable = variable << expression	Bitwise left shift and assigns
'''
#Addition Shorthand:
x = 5
x += 3  # Same as x = x + 3
print(x)  # Output: 8
#Multiplication Shorthand:
x = 4
x *= 2  # Same as x = x * 2
print(x)  # Output: 8
#Bitwise Operations:
x = 8  # Binary: 1000
x >>= 2  # Same as x = x >> 2
print(x)  # Output: 2 (Binary: 0010)

#Miles and kilometers are units of length or distance.

#Bearing in mind that 1 mile is equal to approximately 1.61 kilometers, complete the program in the editor so that it converts:

#miles to kilometers;
#kilometers to miles.

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles*1.61
kilometers_to_miles = kilometers/1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
'''Output
7.38 miles is 11.88 kilometers
12.25 kilometers is 7.61 miles
'''
x =  0
y = float(x-1)
print("y =", y) #y = -1.0
x=1
y=float(x+2)
print("y =", y) #y = 3.0
x=-1
y=float(x*9)
print("y =", y) #y = -9.0
