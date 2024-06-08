### Strings ###

letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be made using a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)
print('########################################################################')

multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)
print('########################################################################')

# Escape Sequences in Strings

# \n: new line
# \t: tab means(8 spaces)
# \\: back slash
# \': single quote(')
# \": double quote(")

print('I hope wveryone is enjoying the Python Challenge.\nAre you?') # line break
print('Days\tTopics\tExercises') # adding tab spaces or 4 spaces
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash symbol (\\)') # To write a backslash
print('In every programming languaje it starts with \"Hello, World!"') # to write a double quote inside a single quote
print('-------------------------------------------------------------------')

# String formatting

# Old Style String Formatting (% Operator)

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# "%.number of digitsf" - Floating point numbers with fixed precision

# Strings only
first_name = 'Francisco'
last_name = 'Miranda'
languaje = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, languaje)
print(formated_string)

# Strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 sifnigicant digits after the point
print(formated_string)

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib', 'Pandas']
formated_string = 'The following are python libraries: %s' %(python_libraries)
print(formated_string)

# New Style String Formatting (str.format)

first_name = 'Asabeneh'
last_name = 'Yetayeh'
languaje = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, languaje)
print(formated_string)

a = 4
b = 3

print('{} + {} = {}'.format(a, b, a+b))
print('{} - {} = {}'.format(a, b, a-b))
print('{} * {} = {}'.format(a, b, a*b))
print('{} / {} = {:.2f}'.format(a, b, a/b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# Strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits a after decimal
print(formated_string)

# String Interpolation /f-Strings(Python 3.6+)

a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
print('---------------------------------------------------------')

# Python Strings as Sequences of Characters
# Unpacking Characters

language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # p
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

# Accesssing Characters in Strings by index

