print("\n--- 1. Declare an empty list. ---")
empty_list = list ()
print('Danh sách rỗng:',empty_list)


print("\n--- 2. Declare a list with more than 5 items. ---")
my_list = ['Python', 'JavaScript', 'HTML', 'CSS', 'SQL', 'Git']
print(my_list)


print("\n--- 3. Find the length of your list. ---")
print('Độ dài danh sách :',len(my_list))


print("\n--- 4. Get the first item, the middle item and the last item of the list. ---")
first_item = my_list[0]
middle_item = my_list[len(my_list) // 2]
last_item = my_list[len(my_list) - 1]
print('Phần tử đầu tiên : {}. Phần tử ở giữa :{}. Phần tử cuối cùng : {}'.format(first_item,middle_item,last_item))


print("\n--- 5. Declare a list called mixed_data_types. ---")
mixed_date_types = ['Le Cong Luyen','20','170','False','Ho Chi Minh City']


print("\n--- 6. Declare a list variable named it_companies. ---")
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']


print("\n--- 7. Print the list using print(). ---")
print('Mixed data type: ',mixed_date_types)
print('IT-companies: ',it_companies)


print("\n--- 8. Print the number of companies in the list. ---")
print('Số lượng công ty:', len(it_companies))
 

print("\n--- 9. Print the first, middle and last company. ---")
first_cpn = it_companies[0]
last_cpn = it_companies[len(it_companies) - 1]
middle_cpn = it_companies[len(it_companies) // 2]
print(f"Đầu: {first_cpn}'. Giữa: {middle_cpn}. Cuối: {last_cpn}")


print("\n--- 10. Print the list after modifying one of the companies. ---")
it_companies[0] = 'Meta' 
print('Sau khi sửa: ',it_companies)


print("\n--- 11. Add an IT company to it_companies. ---")
it_companies.append('Netflix')
print(f"Sau khi thêm: {it_companies}")


print("\n--- 12. Insert an IT company in the middle of the companies list. ---")
it_companies.insert(len(it_companies) // 2 ,'FPT')
print(f"Sau khi chèn: {it_companies}")


print("\n--- 13. Change one of the it_companies names to uppercase (except IBM!). ---")
it_companies[1] = it_companies[1].upper()
print(f"Sau khi đổi thành in hoa: {it_companies}")


print("\n--- 14. Join the it_companies with a string '#; '. ---")
joined_cpn = '#; '.join(it_companies)
print(f"Sau khi joined: {joined_cpn}")


print("\n--- 15. Check if a certain company exists in the it_companies list. ---")
does_cpn_exit = 'Apple' in it_companies
print('Apple có tồn tại trong companies: ',does_cpn_exit)


print("\n--- 16. Sort the list using sort() method. ---")
it_companies.sort()
print(f"Sau khi sort: {it_companies}")


print("\n--- 17. Reverse the list in descending order using reverse() method. ---")
it_companies.reverse()
print(f"Sau khi reverse: {it_companies}")


print("\n--- 18. Slice out the first 3 companies from the list. ---")
del it_companies[:3]
print(f"Sau khi loại bỏ 3 cpn đầu danh sách: {it_companies}")


print("\n--- 19. Slice out the last 3 companies from the list. ---")
del it_companies[-3:]
print(f"Sau khi loại bỏ 3 cpn cuối danh sách: {it_companies}")


print("\n--- 20. Slice out the middle IT company or companies from the list. ---")
middle_cpn_del = len(it_companies) // 2
del it_companies[middle_cpn_del]
print(f"Sau khi loại bỏ cpn giữa danh sách: {it_companies}")


print("\n--- 21. Remove the first IT company from the list. ---")
del it_companies[0]
print(f"Sau khi xóa công ty đầu tiên: {it_companies}")


print("\n--- 23. Remove the last IT company from the list. ---")
last_cpn23 = len(it_companies) - 1
del it_companies[last_cpn23]
print(f"Sau khi xóa công ty cuối danh sách: {it_companies}")


print("\n--- 24. Remove all IT companies from the list. ---")
it_companies.clear()
print(f"Xóa toàn bộ công ty: {it_companies}")


print("\n--- 25. Destroy the IT companies list. ---")
del it_companies
print('Đã xóa IT Company khỏi bộ nhớ:')


print("\n--- 26. Join the following lists: front_end and back_end. ---")
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(f"Danh sách full stack sau khi join: {full_stack}")


print("\n--- 27. Copy the joined list and insert Python and SQL after Redux. ---")
full_stack_copy = full_stack.copy()
redux_index = full_stack_copy.index('Redux')
full_stack_copy.insert(redux_index + 1 , 'Python')
full_stack_copy.insert(redux_index + 2 , 'SQL')
print(f"Sau khi chèn là: {full_stack_copy}")