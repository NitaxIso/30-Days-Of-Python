# Creating a string
letter = 'P'
print(letter)
print(len(letter))

greeting = 'Hello , World!'
print(greeting)
print(len(greeting))

sentence = 'I hope you are enjoying 30 days of PYTHON Challenge'
print(sentence)

# Multiline-string  Use ''' or """
multiline_strings = '''My name is Luyen.
I like PYTHON
I learning Information Security
'''
print(multiline_strings)

#String concatenation : Nối chuỗi 
first_name = 'Le Cong'
last_name = 'Luyen'
space = ' '
full_name = last_name + space + last_name
print(full_name)
print(len(full_name))

#Escape Sequences in Strings : Chuoi thoat
# \n: new line
# \t: Tab means(8 spaces)
# \\: Back slash
# \': Single quote (')
# \": Double quote (")
print('I hope everyone is enjoying the PYTHON challenge.\nAre you ?')
print('Days\tTopics\tExercises')
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash symbol (\\)')
print('In every programming language is start with "Hello, World!"')

#String formatting : Định dạng chuỗi 
# %s - Chuỗi 
# %d - Số nguyên
# %f - Số thực dấu phẩy động
# "%.number of digitsf" - Mấy số sau dấu phẩy
#String only
first_name1 = 'Le Cong'
last_name1 = 'Luyen'
language = 'Python'
formated_string = 'I am %s %s. I learning %s' %(first_name,last_name,language)
print(formated_string)
#String and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string2 = ' The area of the circle with radius %d is %.2f' %(radius,area)

python_libraries = ['Django','Flask','NumPy','Matplotlib','Pandas']
formated_string3 = 'The following are python libraries is: %s' %(python_libraries)
print(formated_string3)


#String formatting - New Style
formated_string5 = 'I am {} {}. I learning{}'.format(first_name,last_name,language)
formated_string4 = 'The area of a circle with a radius {} is {:.2f}.'.format(radius,area)

#Sting Interpolation - f-Strings
a = 3
b = 4
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')



#Python Strings as Sequences of Characters
language = 'Python'
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)

#Sử dụng index âm. -1 là index cuối cùng.
last_letter_index_negative = language[-1]
print(last_letter_index_negative)
second_letter_index_negative = language[-2]
print(second_letter_index_negative)

#Slicing Python Strings : cắt chuỗi
first_three = language[0:3]
print(first_three)
last_three = language[3:6]
print(last_three)
last_three_index_negative = language[-3:]
last_three_index_positive = language[3:]
print(last_three_index_negative)
print(last_three_index_positive)

#Reverse String : dịch ngược chuỗi
reverse_string = 'Hello, World!'
print(greeting[::1])

#Skipping Characters While Slicing
pto = language[0:6:2] 
print(pto)

