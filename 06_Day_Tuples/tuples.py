#Tuples : bộ dữ liệu. Tuples được viết bằng dấu gạch tròn (). Sau khi một tuples được tạo, chúng ta không thể nào thay đổi giá trị của nó.
#Ko dùng các phương thức : add() , insert() , remove() trên 1 tuples vì ko thể sửa đổi (mutable).
#Các phương thức liên quan đến tuples: 
# tuple()
# count()
# index()
# + toán tử : kết hợp 2 bộ dữ liệu.

# Create a tuple
# Syntax : 
empty_tuple = ()
# Using a constructor: 
empty_tuple1 = tuple()

# Tuples chứa giá trị ban đầu.
tpl = ('item1', 'item2', 'item3','item4')
print(tpl)
fruits = ('banana','orange','mango','lemon')
print(fruits)

# Độ dài của tuple(): Dùng phương thức len()
len(tpl)
print(f"Độ dài tuple: {len(tpl)}")
len(fruits)
print(f"Độ dài tuple: {len(fruits)}")

# Index trong tuple.
# Index dương.
first_item = tpl[0]
print(first_item)
second_item = tpl[1]
print(second_item)

first_fruit = fruits[0]
print(first_fruit)
second_fruit = fruits[1]
print(second_fruit)
last_index = len(fruits) - 1
last_fruits = fruits[last_index]
print(last_fruits)

# Index âm.
first_item_nega = tpl[-4]
print(first_item_nega)
second_item_nega = tpl[-3]
print(second_item_nega)

first_fruit_nega = fruits[-4]
print(first_fruit_nega)
second_fruit_nega = fruits[-3]
print(second_fruit_nega)
last_fruits_nega = fruits[-1]
print(last_fruits_nega)

# Cắt tuple : Slicing 
# Index dương.
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]
print(all_items)
all_items1 = tpl[0:]
print(all_items1)
middle_two_items = tpl[1:3]
print(middle_two_items)

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]
print(all_fruits)
all_fruits1 = fruits[0:]
print(all_fruits1)
orange_mango = fruits[1:3]
print(orange_mango)
orange_to_the_rest = fruits[1:]
print(orange_to_the_rest)
# Index âm.
tpl = ('item1', 'item2', 'item3','item4')
all_item_nega = tpl[-4:]
print(all_item_nega)
middle_two_items_nega = tpl[-3:-1]
print(middle_two_items_nega)

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits_nega = fruits[-4:]
print(all_fruits_nega)
orange_mango_nega = fruits[-3:-1]
print(orange_mango_nega)
orange_to_the_rest_nega = fruits[-3:]
print(orange_to_the_rest_nega)


#Chuyển đổi Tuple thành Lists
#Có thể chuyển đổi qua lại giữa tuple và list. Tuple là kiểu dữ liệu bất biến, 
#nếu muốn sửa đổi 1 tuple, thì phải chuyển nó thành list
# Syntax : tpl = ('item1','item2','item3','item4')
#          list = list(tpl)   |  list = tuple(fruits)
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)
fruits = tuple(fruits)
print(fruits)


#Kiểm tra index trong một bộ dữ liệu : có thể kiểm tra 1 index có tồn tại hay 
#không trong 1 tuple bằng cách sử dụng 'in"
#Syntax: tpl = ('item1', 'item2', 'item3','item4')
#        'item2' in tpl #TRUE
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits)
print('apple' in fruits)


#Kết hợp các bộ dữ liệu bằng toán tử +
# Syntax : 
# tpl1 = ('item1', 'item2', 'item3')
# tpl2 = ('item4', 'item5','item6')
# tpl3 = tpl1 + tpl2
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)


#Xóa các bộ dữ liệu 
#Syntax : tpl1 = ('item1', 'item2', 'item3')
#         del tpl1
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
