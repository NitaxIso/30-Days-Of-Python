first_name = 'Le Cong'
last_name = 'Luyen'
country = 'Viet Nam'
age = 20
is_Married = False


# 1. Kiểm tra kiểu dữ liệu của tất cả các biến
print("--- 1. Data Types ---")
print('Type of first_name:', type(first_name))
print('Type of last_name:', type(last_name))
print('Type of country:', type(country))
print('Type of age:', type(age))
print('Type of is_Married:', type(is_Married))


# 2 & 3. Tìm độ dài tên và so sánh với họ
print("--- 2 & 3. Name Length Comparison ---")
len_first_name = len(first_name)
len_last_name = len(last_name)

print('Length of first_name', len_first_name)
print('Length of last_name', len_last_name)
print('Is first_name longer than last_name:', len_first_name > len_last_name)

# 4 -> 11. Các phép toán số học với num_one (5) và num_two (4)
print("--- 4 to 11. Arithmetic Operations ---")
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponentiation:", exp)
print("Floor Division:", floor_division)

# 12. Tính toán hình tròn (Bán kính r = 30m)
print("--- 12. Circle Calculations ---")
import math
math.pi = 3.14
radius = 30

area_of_circle = math.pi * (radius ** 2)
circum_of_circle = 2 * math.pi * radius
print('Area of circle:', area_of_circle)
print('Circum of circle:', circum_of_circle)

user_radius = input('Enter radius of the circle:')
user_radius = float(user_radius)
user_area_of_circle =math.pi * (user_radius ** 2) 
print('User area of circle:',user_area_of_circle)

# 13. Sử dụng hàm input() để lấy thông tin người dùng
print("--- 13. User Information Input ---")
u_firstname = input('Enter your first name:')
u_lastname = input('Enter your last name:')
u_country = input('Enter your country:')
u_age = input('Enter your age:')

print('User Information:', u_firstname, u_lastname, u_country, u_age)

print('User Information:')
print('First name:', u_firstname)
print('Last name:', u_lastname)
print('Country:', u_country)
print('Age:', u_age)