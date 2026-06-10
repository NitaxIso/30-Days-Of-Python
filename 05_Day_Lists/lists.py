#How to create a LIST
#Sử dụng hàm tích hợp sẵn
# Systax : lst = list()
empty_list = list()  # List rỗng , không có item trong list()
print(len(empty_list))  # 0 vì không có item nào trong list()

# Dùng dấu ngoặc vuông []
# Syntax : lst = []
empty_list1 = list()  # List rỗng , không có item trong list[]
print(len(empty_list1))  # 0 vì không có item nào trong list[]

#Danh sách có giá trị ban đầu. Dùng hàm len() -> để tìm độ dài của một list()
fruit = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
animal_products = ['milk', 'meat', 'butter', 'yoghurt']

print('Fruit:', fruit)
print('Number of fruit:', len(fruit))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animai product:', animal_products)
print('Number of animal product:', len(animal_products))

#List : có thể chứ nhiều kiểu dữ liệu khác nhau
lst = [
    'Le Cong Luyen',
    '20',
    True,
    {'country': 'VietNam', 'city': 'Hồ Chí Minh City'}
]
print(lst)

#Truy cập các mục trong list bằng cách sử dụng index.
# Index dương : 0 1 2 3 ...
first_fruit = fruit[0]
print(first_fruit)

second_fruit = fruit[1]
print(second_fruit)

last_fruit = fruit[3]
print(last_fruit)

#Last index.
last_index_fruit = len(fruit) - 1
print(fruit[last_index_fruit])

#Index âm : ... -4 -3 -2 -1
first_fruit_negative = fruit[-4]
last_fruit_negative = fruit[-1]
second_fruit_negative = fruit[-2]

print(first_fruit_negative)
print(last_fruit_negative)
print(second_fruit_negative)

#Unpacking list: là lấy từng phần tử trong list ra và gán vào biến
item = ['item1', 'item2', 'item3', 'item4', 'item4']
first_item, second_item, third_item, *rest = item

print(first_item)
print(second_item)
print(third_item)
print(rest)

countries = [
    'Germany',
    'France',
    'Belgium',
    'Sweden',
    'Denmark',
    'Finland',
    'Norway',
    'Iceland',
    'Estonia'
]

gr, fr, bg, *scandeic, es = countries

print(gr)
print(fr)
print(bg)
print(scandeic)
print(es)

#Cắt index từ list.
#Index dương.
print(fruit)

all_fruit = fruit[0:4]
all_fruit1 = fruit[0:]
orange_and_mango = fruit[1:3]
orange_mango_lemon = fruit[1:]
orange_and_lemon = fruit[::2]

print(all_fruit)
print(orange_and_mango)
print(orange_mango_lemon)
print(orange_and_lemon)

#Index âm.
all_fruit_nega = fruit[-4:]
orange_and_mango_nega = fruit[-3:-1]
orange_mango_lemon_neaga = fruit[-3:]
reverse_fruit = fruit[::-1]

print(all_fruit_nega)
print(orange_and_mango_nega)
print(orange_mango_lemon_neaga)
print(reverse_fruit)

#Chỉnh sửa danh sách.
print(fruit)

fruit[0] = 'avocado'
print(fruit)

fruit[1] = 'apple'
last_index_fruit1 = len(fruit) - 1
fruit[last_index_fruit1] = 'lime'

print(fruit)

#Kiểm tra index trong danh sách.
fruit = ['banana', 'orange', 'mango', 'lemon']
print(fruit)

does_exit = 'banana' in fruit
print(does_exit)  #True

does_exit1 = 'lime' in fruit
print(does_exit1)  # False

#Thêm index vào danh sách : append()
# Syntax : lst = list()
# lst.append(item)
fruit.append('apple')
print(fruit)

fruit.append('lime')
print(fruit)

#Chèn index vào danh sách : insert()
# Syntax: lst = ['item1', 'item2']
# lst.insert(index, item)
fruit = ['banana', 'orange', 'mango', 'lemon']
print(fruit)

fruit.insert(2, 'apple')
print(fruit)

fruit.insert(3, 'lime')
print(fruit)

#Xóa index khỏi danh sách : remove()
# Syntax: lst = ['item1', 'item2']
# lst.remove(item)
fruit.remove('banana')
print(fruit)

fruit.remove('lemon')
print(fruit)

# Hoặc dùng pop() :  xóa phần tử có chỉ số được chỉ định (hoặc phần tử cuối cùng nếu chỉ số không được chỉ định)
# lst.pop()       # last item
# lst.pop(index)
fruit.pop()
print(fruit)

fruit.pop(1)
print(fruit)

#Xóa toàn bộ index trong danh sách: clear()
#lst.clear()
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)

#Sao chép list : copy()
# lst = []
# lst_copy = lst.copy()
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)

# Đếm số index trong danh sách : count()
# lst.count(item)
fruits = ['banana', 'orange', 'mango', 'lemon']
count1 = fruits.count('orange')
print(count1)

ages = [22, 19, 24, 25, 26, 24, 25, 24]
count2 = ages.count(24)
print(count2)

# Tìm index của phần tử : index()
#Syntax : lst.index(item)
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))

# Đảo ngược danh sách : reverse()
# Syntax : lst.reverse()
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)

#Sắp xếp các mục trong danh sách: 
# sort(): phương thức này sửa đổi danh sách gốc
# syntax
# lst = ['item1', 'item2']
# lst.sort()                # ascending
# lst.sort(reverse=True)    # descending
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)
fruits.sort(reverse = True)
print(fruits)
#sorted(): trả về danh sách đã được sắp xếp mà không làm thay đổi danh sách gốc. 
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits, reverse = True)
print(fruits)

# Tham gia danh sách :
# Dùng toán tử + 
# list3 = list1 + list2
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = positive_numbers + zero + negative_numbers
print(integers)
# Dùng extend()
# syntax
# list1 = ['item1', 'item2']
# list2 = ['item3', 'item4', 'item5']
# list1.extend(list2) # ['item1', 'item2', 'item3', 'item4', 'item5']
num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print(num1)