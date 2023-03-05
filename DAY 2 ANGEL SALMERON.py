# Variables in Python

first_name = 'Angel'
last_name = 'Salmeron'
country = 'El Salvador'
city = "San Miguel"
age = 19
is_married = False
skills = ["Python","Computer repairs"]
person_info = {
    'firstname':'Angel', 
    'lastname':'Salmeron', 
    'country':'El Salvador',
    'city':'San Miguel'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = "Angel", "Salmeron", "El Salvador", 19, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)