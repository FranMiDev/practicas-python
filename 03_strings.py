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
print('------------------------------------------------------------')
# Accesssing Characters in Strings by index

language = 'Python'
first_letter = language[0]
print(first_letter)             # P
second_letter = language[1]
print(second_letter)            # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)              # n
print('------------------------------------------------------------')

# if we want to start from right end we can use negative indexing. -1 is the last index.

language = 'Python'
last_letter = language[-1]
print(last_letter)              # n
second_last = language[-2]
print(second_last)              # o
print('------------------------------------------------------------')


# Slicing Python Strings

language = 'Python'
first_three = language[0:3]     # starts at zero index and up to 3 but not include 3
print(first_three)  # Pyt
last_three = language[3:6]
print(last_three)   # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon
print('------------------------------------------------------------')

# Reversing a String

greeting = 'Hello, World!'
print(greeting[::-1])       # !dlroW , olleH
print('------------------------------------------------------------')


# Skipping Characters While Slicing

language = 'Python'
pto = language[0:6:2]
print(pto)  # Pto
print('------------------------------------------------------------')


# String Methods

# capitalize(): Converts the first character of the string to capital letter

challenge = 'thirty days of python'
print(challenge.capitalize())   # Thirty days of python
print('------------------------------------------------------------')


# count(): returns ocurrences of substring in string, count(substring, start=..., end=...The
# start is a starting indexing for counting and end is the last index to count

challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14))  # 1
print(challenge.count('th'))        # 2
print('------------------------------------------------------------')

# endswith(): checks if a string end with a especified ending

challenge = 'thirty days fo python'
print(challenge.endswith('on'))     # True
print(challenge.endswith('tion'))   # False
print('------------------------------------------------------------')

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())       # 'thirty  days    of      python'
print(challenge.expandtabs(10))     # 'thirty    days      of        python'
print('------------------------------------------------------------')

# find(): Returns the index of the first occurrence of a substring, if not found returns -1
challenge = 'thirty days of python'
print(challenge.find('y'))      # 5
print(challenge.find('th'))     # 0
print('------------------------------------------------------------')

# rfind(): Returns the index of the last ocurrence of a substring, if not found returns -1
challenge = 'thirty days of python'
print(challenge.rfind('y'))     # 16
print(challenge.rfind('th'))    # 17
print('------------------------------------------------------------')

# format(): formats string into a nicer output
first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, age, job, country)
print(sentence)     # I am Asabeneh Yetayeh. I am 250 years old. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result)    # The area of a circle with radius 10 is 314
print('------------------------------------------------------------')

# index(): Returns the lowest index of a substring, additional arguments indicate starting and
# ending index (default 0 and string length -1). If the substring is not found it raises a valueError.
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))      # 7
#print(challenge.index(sub_string, 9))   # error
print('------------------------------------------------------------')

# rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 8
# print(challenge.rindex(sub_string, 9)) # error
print('------------------------------------------------------------')

# isalnum(): Checks alphanumeric character

challenge = 'ThirtyDaysPython'
print(challenge.isalnum())      # True

challenge = '30DaysPython'
print(challenge.isalnum())      # True

challenge = 'thirty days of python'
print(challenge.isalnum())      # False, space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum())  #false
print('------------------------------------------------------------')

# isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)

challenge = 'thirty days of python'
print(challenge.isalpha())  # False, space is once again excluded
challenge = 'ThirtyDaysOfPython'
print(challenge.isalpha())  # True
num = '123'
print(num.isalpha())  # False
print('------------------------------------------------------------')

# isdecimal(): Checks if all characters in a string are decimal (0-9)

challenge = 'thirty days of python'
print(challenge.isdecimal())        # False
challenge = '123'
print(challenge.isdecimal())        # True
challenge = '\u00B2'
print(challenge.isdecimal())   # False
challenge = '12 3'
print(challenge.isdecimal())  # False, space not allowed
print('------------------------------------------------------------')


# isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)

challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True
print('------------------------------------------------------------')

# isnumeric(): Checks if all characters in a string are numbers o number related (just like
# isdigit(), just accepts more symbols, like ½)

num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False
print('------------------------------------------------------------')


# isidentifier(): checks for a valid identifier - it checks if a string is a valid variable name

challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True
print('------------------------------------------------------------')

# slower(): Checks if all alphabet characters in the string are lowercase
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False
print('------------------------------------------------------------')

# isupper(): Checks if all alphabet characters in the string are uppercase
challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True
print('------------------------------------------------------------')

# join(): Returns a concatenated string
web_tech = ['HTML', 'CSS', 'JavaScripts', 'React']
result = ' '.join(web_tech)
print(result)

result = '# '.join(web_tech)
print(result)
print('------------------------------------------------------------')


# strip(): Removes all given characters starting from the beginning and end of the string
challenge = 'thirty days of python'
print(challenge.strip('noth'))      # irty days of py
print('------------------------------------------------------------')

# replace(): Replaces substring with a given string
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'))    # 'thirty days of coding'
print('------------------------------------------------------------')

# split(): Splits the string, using given string or space as a separator
challenge = 'thirty days of python'
print(challenge.split())  # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']
print('------------------------------------------------------------')

# title(): returns a title cased string