# Variables in Python
first_Name = 'Le Cong'
last_Name = 'Luyen'
country = 'Viet Nam'
city = 'Ho Chi Minh City'
age = 20
is_Married = False
skills = ['Java ','C','SQL','Python']
person_Info = {
    'firstName' : 'Le Cong' ,
    'lastName' : 'Luyen' ,
    'country' : 'Viet Nam' ,
    'city' : 'Ho Chi Minh City'
}
# Printing the values stored in the variables
print('First name :',first_Name)
print('First name length:',len(last_Name))
print('Last name:',last_Name)
print('Last name length:',len(last_Name))
print('Country:',country)
print('City:',city)
print('Age:',age)
print('Married:',is_Married)
print('Skill:',skills)
print('Personal Infomation:',person_Info)
# Declaring multiple variables in one line
first_name, last_name, country, age, is_married = 'Le Cong', 'Luyen', 'Viet Name', 20, False
print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)