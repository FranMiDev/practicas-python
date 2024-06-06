### Operators ###

# Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
# 2.0  Division in Python gives floating number
print('Division: ', 4 / 2)
print('Division: ', 6 / 2)        # 3.0
print('Division: ', 7 / 2)        # 3.5
# 3,  gives without the floating number or without the remaining
print('Division without the remainder: ', 7 // 2)
print('Division without the remainder: ', 7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3)  # 9 it means 2 * 2 * 2
print('#######################################################')

# Example: Floats

# Floating numbers
print('Floating Point Number, PI ', 3.14)
print('Floating Point Number, gravity ', 9.81)
print('#######################################################')

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ', (1 + 1j) * (1 - 1j))
print('#######################################################')

# Example Comparison Operatos

print(3 > 2)            # True, because 3 is greater than 2
print(3 >= 2)           # True, because 3 is greater than 2
print(3 < 2)            # False, because 3 is greater than 2
print(2 < 3)            # True, because 2 is less than 3
print(2 <= 3)           # True, because 2 is less than 3
print(3 == 2)           # False, because 3 is not equals to 2
print(3 != 2)           # True, because 3 is not equals to 2
print(len('mango') == len('avocado'))       # False
print(len('mango') != len('avocado'))       # True
print(len('mango') < len('avocado'))        # True
print(len('milk') != len('meat'))           # False
print(len('milk') == len('meat'))           # True
print(len('tomato') == len('potato'))       # True
print(len('python') > len('dragon'))        # False
print('#######################################################')

# Comparing something gives either a True or False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False: ', False == False)
print('#######################################################')

# In addition to the above comparison operator Python uses:

# * is: Returns true if both variables are the same object(x is y)
# * is not: Returns true if both variables are not the same object(x is not y)
# * in: Returns True if the queried list contains a certain item(x in y)
# * not in: Returns True if the queried list doesnt have certain item(x in y)

# True - because the data value are the same
print('1 is 1 ', 1 is 1)
print('1 is not 2 ', 1 is not 2)    # True - because 1 is not 2
print('A in Asabeneh ', 'A' in 'Asabeneh')  # True - A found in the string
print('B in Asebeneh ', 'B' in 'Asebeneh')  # False - there is no uppercase B
# True - because coding for all has the word coding
print('coding' in 'coding for all')
print('a in an: ', 'a' in 'an')     # True
print('4 is 2 ** 2: ', 4 is 2 ** 2)  # True
print('#######################################################')

# Logical Operators

# and --> Returns True if both statements are true                --> x < 5 and x < 10
# or  --> Returns True if one of the statements is true           --> x < 5 or x < 4
# not --> Reverse the result, returns False if the result is true --> not(x < 5 and x < 10)

print(3 > 2 and 4 > 3)  # True - because both statements are true
print(3 > 2 and 4 < 3)  # False - because the second statement is false
print(3 < 2 and 4 < 3)  # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False)  # False
