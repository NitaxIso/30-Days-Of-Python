print("--- 1.Concatenate the string. ---")
string = ['Thirty','Days','Of','Python']
print(' '.join(string))

print("\n--- 2.Concatenate the string 'Coding', 'For', 'All'. ---")
string1 = ['Coding','For','All']
print(' '.join(string1))

print("\n--- 3.Declare a variable named company. ---")
company = 'Coding For All'

print("\n--- 4.Print the variable company. ---")
print(company)

print("\n--- 5.Print the length of the company string. ---")
print(len(company))

print("\n--- 6.Change all characters to uppercase. ---")
print(company.upper())

print("\n--- 7.Change all characters to lowercase. ---")
print(company.lower())

print("\n--- 8.Use capitalize, title, swapcase methods. ---")
print(company.capitalize())
print(company.title())
print(company.swapcase())

print("\n--- 9.Slice out the first word. ---")
print(company.strip('Coding '))

print("\n--- 10.Check if string contains a word Coding. ---")
print(company.find('Coding') != -1)
print('Coding' in company)

print("\n--- 11.Replace the word Coding with Python. ---")
print(company.replace('Coding','Python'))

print("\n--- 12.Change Python for Everyone to Python for All. ---")
string12 = 'Python for Everyone'
print(string12.replace('Everyone','All'))

print("\n--- 13.Split the string using space as separator. ---")
print(company.split())
 
print("\n--- 14.Split the string at the commas. ---")
techs = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(techs.split(' '))

print("\n--- 15.What is the character at index 0. ---")
print(company[0])

print("\n--- 16.What is the last index of the string. ---")
print(company[-1])

print("\n--- 17.What character is at index 9. ---")
print(company[9])

print("\n--- 18.Create an acronym for Python For Everyone. ---")
print(company.index('C'))

print("\n--- 19.Create an acronym for Coding For All. ---")
print(company.index('F'))

print("\n--- 20.Position of the first occurrence of C. ---")
print(company.rfind('l'))

print("\n--- 21.Position of the first occurrence of F. ---")
string22 = 'Coding For All People'
print(string22.rfind('l'))

print("\n--- 22.Position of the last occurrence of l. ---")
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
print(sentence.index('because'))

print("\n--- 23.Position of the first occurrence of because. ---")
print(sentence.rfind('because'))

print("\n--- 24.Position of the last occurrence of because. ---")
start = sentence.find('because')
finish = sentence.rfind('because') + len('because')
print(sentence[start:finish])

print("\n--- 25.Slice out the phrase because because because. ---")
print(company.startswith('Coding'))

print("\n--- 26.Find the position of the first occurrence of because. ---")
print(company.endswith('coding'))

print("\n--- 27.Slice out the phrase because because because. ---")
bad_string = '     Code   For All'
print(' '.join(bad_string.split()))

print("\n--- 28.Does Coding For All start with Coding. ---")
string_true = input('Enter String: ')
print(string_true.isidentifier())

print("\n--- 29.Does Coding For All end with coding. ---")
library = ['Django','Flask','Bottle','Pyramid','Falcon']
print(' '.join(library))

print("\n--- 30.Remove the left and right trailing spaces. ---")
print('I am enjoying this challenge.\nI just wonder what is next.')

print("\n--- 31.Which variable returns True for isidentifier. ---")
row1 = ['Name','Age','Country','City']
row2 = ['Luyen','20','VietName','Ho Chi Minh City']
print('\t'.join(row1))
print('\t'.join(row2))

print("\n--- 32.Join the list with a space string. ---")
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square.'.format(radius,area))

print("\n--- 33.Use new line escape sequence to separate sentences. ---")
a = 8 
b = 6
print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}') 
print(f'{a} / {b} = {a/b :.2f}')
print(f'{a} % {b} = {a%b}')
print(f'{a} // {b} = {a//b}')
print(f'{a} ** {b} = {a**b}')