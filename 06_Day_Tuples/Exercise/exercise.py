#Level1
print("\n--- 1. Declare an empty tuple. ---")
empty_tpl = tuple()
print('Empth Tuple:',empty_tpl)

print("\n--- 2. Create a tuple containing names of your sisters and your brothers. ---")
brothers = ('Luu' , 'Hai' , 'Hieu')
sisters = ('Hien' , 'Hau')
print("Sisters:", sisters)
print("Brothers:", brothers)

print("\n--- 3. Join brothers and sisters tuples and assign it to siblings. ---")
siblings = brothers + sisters
print("Siblings:", siblings)

print("\n--- 4. How many siblings do you have? ---")
num_siblings = len(siblings)
print('Number siblings :',num_siblings)

print("\n--- 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members. ---")
family_members_list = list(siblings)
family_members_list.append('Luan')
family_members_list.append('Loan')
family_members = tuple(family_members_list)
print('Family Member :', family_members)


#Level2
print("\n--- 1. Unpack siblings and parents from family_members. ---")
*siblings_unpacked, father, mother = family_members
print("Siblings unpacked:", siblings_unpacked)
print("Father:", father)
print("Mother:", mother)


print("\n--- 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable named food_stuff_tp. ---")
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
animal_products = ('meat', 'milk', 'egg')

food_stuff_tp = fruits + vegetables + animal_products
print("food_stuff_tp:", food_stuff_tp)


print("\n--- 3. Change the food_stuff_tp tuple to a food_stuff_lt list. ---")
food_stuff_lt = list(food_stuff_tp)
print("food_stuff_lt:", food_stuff_lt)


print("\n--- 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list. ---")
length = len(food_stuff_lt)
middle_index = length // 2

if length % 2 == 0:
    middle_items = food_stuff_lt[middle_index - 1 : middle_index + 1]
else:
    middle_items = food_stuff_lt[middle_index : middle_index + 1] # Hoặc chỉ lấy food_stuff_lt[middle_index]

print("Middle item(s):", middle_items)


print("\n--- 5. Slice out the first three items and the last three items from food_stuff_lt list. ---")
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("First three items:", first_three)
print("Last three items:", last_three)


print("\n--- 6. Delete the food_stuff_tp tuple completely. ---")
del food_stuff_tp
print("food_stuff_tp has been deleted.")


print("\n--- 7. Check if 'Estonia' and 'Iceland' are nordic countries. ---")
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print("Is Estonia a nordic country?", 'Estonia' in nordic_countries)
print("Is Iceland a nordic country?", 'Iceland' in nordic_countries)