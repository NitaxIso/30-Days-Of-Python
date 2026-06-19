# Tạo 1 tập hợp.
# Syntax : st = set()
st = {'item1','item2','item3','item4'}
fruits = {'banana', 'orange', 'mango', 'lemon'}

# Độ dài của sets.
len(st)
len(fruits)

# Accessing Items in sets.
# Checking a item.
print('Does set st contain item3? :', 'item3' in st)
print('mango ' in fruits)
# Adding items to a sets.
# One item.
st = {'item1','item2','item3','item4'}
st.add('item5')
print(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
print(fruits)
# Mutiple item.
st.update(['item6','item7'])
print(st)

vegetables = ('tomato','potato','onion','carrot')
fruits.update(vegetables)
print(fruits)

# Remove Items from a sets.
st = {'item1','item2','item3','item4'}
st.remove('item2')
print(st)
#pop() : loại bỏ một phần tử ngẫu nhiên khỏi danh sách và trả về phần tử đã bị loại bỏ.
fruits = {'banana','orange','mango','lemon'}
fruits.pop()
print(fruits)

fruits = {'banana','orange','mango','lemon'}
remove_fruits = fruits.pop()
print(remove_fruits)

#Clearing items in sets.
st.clear()
print(st)  # set()
fruits.clear()
print(fruits)  # set()

# Deleting a sets
st = {'item1', 'item2', 'item3', 'item4'}
del st

fruits = {'banana','orange','mango','lemon'}
del fruits

# Convert Lists -> Sets
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)
print(st)

fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
set_fruits = set(fruits)
print(set_fruits)

# Joining Sets : union(): hợp nhất  or update(): cập nhật
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2) #st3 = st1 | st2

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits_vegetables = fruits.update(vegetables)

# Finding Intersection Items : các mục giao nhau -> intersection()
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item1','item5'}
st3 = st1.intersection(st2)
print(st3)


# Checking Subset and Super Set
# Tập con : issubset()
# Tập cha : issuperset()
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2','item3'}
st3 = st2.issubset(st1)
st4 = st1.issuperset(st2)
print(st3)
print(st4)

# Checking the Difference Between Two Sets : different()
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2','item3'}
st3 = st1.difference(st2)
st4 = st2.difference(st1)
print(st3) # Srt1 khác set2 không -> có trã về ptu khac
print(st4) # Set2 khác set1 không -> ko thì trã về set()

python = {'p','y','t','h','o','n'}
dragon = {'d','r','a','g','o','n'}
python_dragon = python.difference(dragon)
dragon_python = dragon.difference(python)
print(python_dragon)
print(dragon_python)

# Finding Symmetric Difference Between Two Sets : Hiệu đối xứng 2 tập hợp.
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'} : st2 ^ st1

# Joining Sets : isdisjoint() : kiểm tra 2 tập hợp là chung hay rời rạc 
even_number = {2,4,6,8,10}
old_number = (1,3,5,7,9)
check_number = even_number.isdisjoint(old_number)
print(check_number)

python = {'p','y','t','h','o','n'}
dragon = {'d','r','a','g','o','n'}
check_python_dragon = python.isdisjoint(dragon)
print(check_python_dragon)
