# variables in Python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['html', 'css', 'js', 'react', 'python']
person_info = {
    'firstname': 'Asabeneh',
    'lastname': 'Yetayeh',
    'country': 'Finland',
    'city': 'Helsinki'
}

# Printing the values stored in the variables

print('First name: ', first_name)
print('First name length: ', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('skills: ', skills)
print('Person information: ', person_info)
print('#################################################################')

# Multiple variables can also be declared in one line:

nombre, apellido, ciudad, anho, estas_casado = 'Francisco', 'Miranda', 'Encarnacion', '37', 'casado'

print(nombre, apellido, ciudad, anho, estas_casado)

print('#################################################################')

# primer_nombre = input('What is your name: ')
# anho = input('How old are you?: ')

# print(primer_nombre)
# print(anho)

print('#################################################################')

# Checking Data Types and Casting

# Printing out types

print(type('Francisco'))      # str
print(type(first_name))       # str
print(type(10))               # int
print(type(3.14))             # float
print(type(1 + 1j))           # complex
print(type(True))             # bool
print(type([1, 2, 3, 4]))        # list
print(type({'name: ': 'Francisco', 'age: ': 37}))  # dict
print(type((1, 2)))                                # tuple
print(type(zip([1, 2], [3, 4])))                     # set

print('#################################################################')

# Casting

# int to float
num_int = 10
print('num_int ', num_int)  # 10
num_float = float(num_int)
print('num_float: ', num_float)  # 10.0

# float to int
gravity = 9.81
print(int(gravity))  # 9

# int to str
num_int = 10
print(num_int)              # 10
num_str = str(num_int)
print(num_str)              # '10'

# str to int or float
num_str = '10.6'
# print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Asabeneh'
print(first_name)                           # Asabeneh
first_name_to_list = list(first_name)
# ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']
print(first_name_to_list)
