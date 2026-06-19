# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# Level1.
print(f"Length of it_companies : {len(it_companies)}")
# Add 1 item: add()
it_companies.add('Twitter')
print('Sau khi thêm Twitter: ',it_companies)
# Add nhiều items: update()
it_companies.update(['FPT','Viettel','Athena'])
print('Sau khi thêm nhiều công ty CNTT: ', it_companies)
# Xóa 1 item : remove()
it_companies.remove('IBM')
print('Sau khi xóa 1 công ty: ', it_companies)
# Xóa 1 ptu ngẫu nhiên : pop() -> Muốn trã về ptu bị xóa : remove_pop = .pop()
remove_pop = it_companies.pop()
print('Công ty bị xóa ngẫu nhiên là : ',remove_pop)
print('Danh sách sau khi xóa 1 công ty ngẫu nhiên: ', it_companies)
# Xóa toàn bộ các ptu : clear()
it_companies.clear()
print(it_companies) # set()

# remove() | discard()
# remove() khi xóa 1 ptu ko co trong set -> trã về KEYERROR
# discard() khi xóa 1 ptu khong co trong set -> bõ qua -> tiếp tục chạy không báo lỗi hay dừng chương trình.


A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
# Level2.
union  = A.union(B)
print('A hợp B: ',union)

intersection = A.intersection(B)
print('A giao B: ',intersection)

is_subset = A.issubset(B)
print('A có phải là tập con của B: ',is_subset)

is_disjoint = A.isdisjoint(B)
print('A và B có phải tập hợp rời nhau không: ',is_disjoint)

is_dif = A.symmetric_difference(B)
print('Hiệu đối xứng A và B là :',is_dif)

A.clear()
print('Sau khi xóa toàn bộ dữ liệu A: ',A)
del B
age = [22, 19, 24, 25, 26, 24, 25, 24]