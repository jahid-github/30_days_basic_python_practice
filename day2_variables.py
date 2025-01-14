# -*- coding: utf-8 -*-
"""Variables.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZT75VDy7YJB2II_C_4C6C4zezCPqOaIe
"""

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
