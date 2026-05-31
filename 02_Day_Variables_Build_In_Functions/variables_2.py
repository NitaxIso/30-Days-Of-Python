# Functions Input() : getting user input.
first_Name = input('What is your name:')
age = input('How old are you?')

print(first_Name)
print(age)



# Casting : Ép kiểu dữ liệu.
# int -> float
num_Int = 10
print('num_Int',num_Int)            # 10
num_Float= 10
print('num_Float',num_Float)        # 10.0

#float -> int 
gravity = 9.81
print(int(gravity))                 # 9

#int -> str
num1_Int = 10
print(num_Int)                      # 10
num_Str = str(num1_Int)
print(num1_Int)                     # '10'

#str -> int or float
num_Str1 = '10.6'

num_Float = float(num_Str1)         # Convert the string to a float first
num_Int2 = int(num_Float)           # Convert the float to an integer
print('num_Int',num_Int2)      # 10
print('num_Float',num_Float)  # 10.6

num_Int3 = int(num_Float)           
print('num_Int',int(num_Int3))      # 10    

#str -> list
first_Name = 'Le Cong Luyen'
print(first_Name)
first_Name_to_List = list(first_Name)
print(first_Name_to_List)