# Day 02 - Biến và Các Hàm Tích Hợp Sẵn Trong Python

## Mục tiêu bài học

Ở ngày thứ 2, mình sẽ học về **biến**, **kiểu dữ liệu cơ bản** và một số **hàm tích hợp sẵn** thường dùng trong Python.

Sau bài này, mình cần nắm được:

* Hàm tích hợp sẵn là gì
* Cách khai báo biến trong Python
* Quy tắc đặt tên biến
* Cách khai báo nhiều biến trên một dòng
* Các kiểu dữ liệu cơ bản trong Python
* Cách kiểm tra kiểu dữ liệu bằng `type()`
* Cách ép kiểu dữ liệu bằng `int()`, `float()`, `str()`, `list()`
* Các kiểu dữ liệu số trong Python

---

## 1. Hàm tích hợp sẵn trong Python

Trong Python có rất nhiều hàm được xây dựng sẵn.
Các hàm này gọi là **built-in functions**.

Điều đặc biệt là mình có thể sử dụng các hàm này ngay lập tức mà không cần cài thêm thư viện hay import gì cả.

Một số hàm tích hợp sẵn thường dùng:

| Hàm        | Công dụng                                             |
| :--------- | :---------------------------------------------------- |
| `print()`  | In dữ liệu ra màn hình                                |
| `len()`    | Đếm độ dài của chuỗi, list, tuple,...                 |
| `type()`   | Kiểm tra kiểu dữ liệu                                 |
| `int()`    | Chuyển dữ liệu sang kiểu số nguyên                    |
| `float()`  | Chuyển dữ liệu sang kiểu số thực                      |
| `str()`    | Chuyển dữ liệu sang kiểu chuỗi                        |
| `input()`  | Nhập dữ liệu từ bàn phím                              |
| `list()`   | Chuyển dữ liệu sang list                              |
| `dict()`   | Tạo dictionary                                        |
| `min()`    | Lấy giá trị nhỏ nhất                                  |
| `max()`    | Lấy giá trị lớn nhất                                  |
| `sum()`    | Tính tổng                                             |
| `sorted()` | Sắp xếp dữ liệu                                       |
| `help()`   | Xem hướng dẫn sử dụng                                 |
| `dir()`    | Xem các thuộc tính hoặc phương thức của một đối tượng |

Ví dụ:

```python
print("Hello, World!")
print(len("Python"))
print(type(10))
print(type("Hello"))
```

Kết quả:

```python
Hello, World!
6
<class 'int'>
<class 'str'>
```

---

## 2. Sử dụng một số hàm built-in cơ bản

### Ví dụ với `print()`

Hàm `print()` dùng để in dữ liệu ra màn hình.

```python
print("Hello, Python!")
print("My name is Luyen")
```

Hàm `print()` cũng có thể nhận nhiều giá trị cùng lúc.

```python
print("Hello", "Python", "Day", 2)
```

Kết quả:

```python
Hello Python Day 2
```

---

### Ví dụ với `len()`

Hàm `len()` dùng để lấy độ dài của chuỗi hoặc các kiểu dữ liệu dạng tập hợp.

```python
print(len("Python"))
print(len("Hello World"))
```

Kết quả:

```python
6
11
```

Lưu ý:
Dấu cách cũng được tính là một ký tự.

---

### Ví dụ với `type()`

Hàm `type()` dùng để kiểm tra kiểu dữ liệu của một giá trị.

```python
print(type("Luyen"))
print(type(18))
print(type(3.14))
print(type(True))
```

Kết quả:

```python
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

---

### Ví dụ với `min()`, `max()`, `sum()`

```python
numbers = [5, 10, 15, 20]

print(min(numbers))
print(max(numbers))
print(sum(numbers))
```

Kết quả:

```python
5
20
50
```

---

## 3. Biến trong Python

Biến được dùng để **lưu trữ dữ liệu** trong bộ nhớ máy tính.

Có thể hiểu đơn giản:

> Biến giống như một cái hộp dùng để chứa giá trị.

Ví dụ:

```python
name = "Luyen"
age = 20
country = "Viet Nam"
```

---

## 4. Quy tắc đặt tên biến

Khi đặt tên biến trong Python, cần chú ý các quy tắc sau:

* Tên biến phải bắt đầu bằng chữ cái hoặc dấu gạch dưới `_`
* Tên biến không được bắt đầu bằng số
* Tên biến chỉ được chứa chữ cái, số và dấu gạch dưới
* Tên biến có phân biệt chữ hoa và chữ thường
* Không nên dùng từ khóa có sẵn của Python để đặt tên biến

---

## 5. Tên biến hợp lệ

Các tên biến dưới đây là hợp lệ:

```python
first_name = "Luyen"
last_name = "Le"
age = 20
country = "Viet Nam"
city = "Ho Chi Minh"
is_student = True
year_2026 = 2026
_num = 10
```

---

## 6. Tên biến không hợp lệ

Các tên biến dưới đây là không hợp lệ:

```python
first-name = "Luyen"
first@name = "Luyen"
first$name = "Luyen"
1num = 10
num-1 = 20
```

Lý do sai:

* Có dấu `-`
* Có ký tự đặc biệt như `@`, `$`
* Bắt đầu bằng số

---

## 7. Quy tắc đặt tên nên dùng

Trong Python, cách đặt tên biến phổ biến là **snake_case**.

Tức là nếu tên biến có nhiều từ, mình dùng dấu gạch dưới `_` để nối các từ lại.

Ví dụ:

```python
first_name = "Luyen"
last_name = "Le"
full_name = "Luyen Le"
current_year = 2026
is_light_on = True
```

Không nên đặt tên biến quá ngắn hoặc khó hiểu.

Ví dụ không nên:

```python
x = "Luyen"
y = 20
z = "Viet Nam"
```

Nên viết rõ nghĩa hơn:

```python
name = "Luyen"
age = 20
country = "Viet Nam"
```

---

## 8. Khai báo biến

Khai báo biến là việc tạo biến và gán giá trị cho biến đó.

Trong Python, mình dùng dấu `=` để gán giá trị.

```python
first_name = "Luyen"
last_name = "Le"
age = 20
country = "Viet Nam"
is_student = True
```

Lưu ý:

Dấu `=` trong Python là toán tử gán, không phải dấu bằng trong toán học.

Ví dụ:

```python
age = 20
```

Nghĩa là: gán giá trị `20` cho biến `age`.

---

## 9. In giá trị của biến

Sau khi khai báo biến, mình có thể dùng `print()` để in giá trị ra màn hình.

```python
first_name = "Luyen"
last_name = "Le"
age = 20
country = "Viet Nam"

print("First name:", first_name)
print("Last name:", last_name)
print("Age:", age)
print("Country:", country)
```

Kết quả:

```python
First name: Luyen
Last name: Le
Age: 20
Country: Viet Nam
```

---

## 10. Dùng `len()` với biến

Mình có thể dùng `len()` để lấy độ dài của chuỗi được lưu trong biến.

```python
first_name = "Luyen"

print("First name:", first_name)
print("Length:", len(first_name))
```

Kết quả:

```python
First name: Luyen
Length: 5
```

---

## 11. Khai báo nhiều biến trên một dòng

Python cho phép khai báo nhiều biến trên cùng một dòng.

Ví dụ:

```python
first_name, last_name, age, country = "Luyen", "Le", 20, "Viet Nam"

print(first_name)
print(last_name)
print(age)
print(country)
```

Kết quả:

```python
Luyen
Le
20
Viet Nam
```

Cách này tiện, nhưng không nên lạm dụng nếu dòng code quá dài hoặc khó đọc.

---

## 12. Nhập dữ liệu từ người dùng với `input()`

Hàm `input()` dùng để nhập dữ liệu từ bàn phím.

Ví dụ:

```python
name = input("Enter your name: ")
age = input("Enter your age: ")

print("Your name is:", name)
print("Your age is:", age)
```

Khi chạy chương trình, người dùng sẽ nhập dữ liệu vào.

Lưu ý quan trọng:

Dữ liệu lấy từ `input()` luôn có kiểu là `str`.

Ví dụ:

```python
age = input("Enter your age: ")

print(type(age))
```

Dù người dùng nhập `20`, kiểu dữ liệu vẫn là:

```python
<class 'str'>
```

Nếu muốn dùng tuổi như một số, cần ép kiểu sang `int`.

```python
age = int(input("Enter your age: "))

print(type(age))
```

---

## 13. Kiểu dữ liệu trong Python

Python có nhiều kiểu dữ liệu khác nhau.

Một số kiểu dữ liệu cơ bản:

| Kiểu dữ liệu | Tên trong Python | Ví dụ               |
| :----------- | :--------------- | :------------------ |
| Chuỗi        | `str`            | `"Hello"`           |
| Số nguyên    | `int`            | `10`                |
| Số thực      | `float`          | `3.14`              |
| Số phức      | `complex`        | `1 + 2j`            |
| Boolean      | `bool`           | `True`, `False`     |
| Danh sách    | `list`           | `[1, 2, 3]`         |
| Tuple        | `tuple`          | `(1, 2, 3)`         |
| Set          | `set`            | `{1, 2, 3}`         |
| Dictionary   | `dict`           | `{"name": "Luyen"}` |

---

## 14. Kiểm tra kiểu dữ liệu bằng `type()`

Để biết một biến hoặc giá trị thuộc kiểu dữ liệu nào, mình dùng hàm `type()`.

Ví dụ:

```python
first_name = "Luyen"
age = 20
height = 1.70
is_student = True
skills = ["Python", "HTML", "CSS"]
person = {
    "name": "Luyen",
    "age": 20
}

print(type(first_name))
print(type(age))
print(type(height))
print(type(is_student))
print(type(skills))
print(type(person))
```

Kết quả:

```python
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'list'>
<class 'dict'>
```

---

## 15. Ép kiểu dữ liệu

Ép kiểu là chuyển dữ liệu từ kiểu này sang kiểu khác.

Ví dụ:

* Từ `int` sang `float`
* Từ `float` sang `int`
* Từ `int` sang `str`
* Từ `str` sang `int`
* Từ `str` sang `list`

---

### Chuyển `int` sang `float`

```python
num_int = 10
num_float = float(num_int)

print(num_int)
print(num_float)
print(type(num_float))
```

Kết quả:

```python
10
10.0
<class 'float'>
```

---

### Chuyển `float` sang `int`

```python
gravity = 9.81
gravity_int = int(gravity)

print(gravity_int)
```

Kết quả:

```python
9
```

Lưu ý:

Khi chuyển từ `float` sang `int`, phần thập phân sẽ bị bỏ đi, không phải làm tròn.

---

### Chuyển `int` sang `str`

```python
age = 20
age_str = str(age)

print(age)
print(age_str)
print(type(age_str))
```

Kết quả:

```python
20
20
<class 'str'>
```

---

### Chuyển `str` sang `int`

```python
num_str = "10"
num_int = int(num_str)

print(num_int)
print(type(num_int))
```

Kết quả:

```python
10
<class 'int'>
```

Nếu chuỗi không phải số hợp lệ thì sẽ bị lỗi.

Ví dụ:

```python
num_str = "hello"
num_int = int(num_str)
```

Chương trình sẽ báo lỗi vì `"hello"` không thể đổi sang số nguyên.

---

### Chuyển `str` sang `float`

```python
num_str = "10.5"
num_float = float(num_str)

print(num_float)
print(type(num_float))
```

Kết quả:

```python
10.5
<class 'float'>
```

---

### Chuyển `str` sang `list`

```python
name = "Luyen"
name_list = list(name)

print(name_list)
```

Kết quả:

```python
['L', 'u', 'y', 'e', 'n']
```

---

## 16. Các kiểu dữ liệu số trong Python

Trong Python có 3 kiểu dữ liệu số chính:

### 1. Integer

`int` là kiểu số nguyên.

Ví dụ:

```python
age = 20
year = 2026
temperature = -5

print(type(age))
```

Kết quả:

```python
<class 'int'>
```

---

### 2. Float

`float` là kiểu số thực, có phần thập phân.

Ví dụ:

```python
height = 1.70
price = 99.99
gravity = 9.81

print(type(height))
```

Kết quả:

```python
<class 'float'>
```

---

### 3. Complex

`complex` là kiểu số phức.

Ví dụ:

```python
complex_number = 1 + 2j

print(complex_number)
print(type(complex_number))
```

Kết quả:

```python
(1+2j)
<class 'complex'>
```

---

## 17. Tổng kết Day 02

* Python có nhiều hàm built-in dùng sẵn
* `print()` dùng để in dữ liệu
* `len()` dùng để lấy độ dài
* `type()` dùng để kiểm tra kiểu dữ liệu
* Biến dùng để lưu trữ dữ liệu
* Tên biến nên đặt rõ nghĩa và dùng dạng `snake_case`
* Có thể khai báo nhiều biến trên một dòng
* `input()` dùng để nhập dữ liệu từ bàn phím
* Dữ liệu nhập từ `input()` mặc định là chuỗi
* Có thể ép kiểu dữ liệu bằng `int()`, `float()`, `str()`, `list()`
* Các kiểu số chính gồm `int`, `float`, `complex`

---

# Bài tập Day 02

## Level 1

### Bài 1: Tạo thư mục cho Day 02 và tạo file Python để thực hành

### Bài 2: Viết comment `Day 2: 30 Days of Python programming`

### Bài 3: Khai báo biến lưu tên của bạn

### Bài 4: Khai báo biến lưu họ của bạn

### Bài 5: Khai báo biến lưu họ tên đầy đủ

### Bài 6: Khai báo biến lưu quốc gia

### Bài 7: Khai báo biến lưu thành phố

### Bài 8: Khai báo biến lưu tuổi

### Bài 9: Khai báo biến lưu năm hiện tại

### Bài 10: Khai báo biến `is_married`

### Bài 11: Khai báo biến `is_true`

### Bài 12: Khai báo biến `is_light_on`

### Bài 13: Khai báo nhiều biến trên một dòng

---

## Level 2

### Bài 1: Kiểm tra kiểu dữ liệu của các biến bằng `type()`

### Bài 2: Dùng `len()` để kiểm tra độ dài tên của bạn

### Bài 3: So sánh độ dài tên và họ

### Bài 4: Khai báo hai biến `num_one` và `num_two`

### Bài 5: Cộng `num_one` và `num_two`

### Bài 6: Trừ `num_two` khỏi `num_one`

### Bài 7: Nhân `num_one` và `num_two`

### Bài 8: Chia `num_one` cho `num_two`

### Bài 9: Lấy phần dư khi chia `num_two` cho `num_one`

### Bài 10: Tính `num_one` mũ `num_two`

### Bài 11: Chia lấy phần nguyên `num_one` cho `num_two`

### Bài 12: Tính diện tích và chu vi hình tròn với bán kính 30 mét

### Bài 13: Nhập bán kính từ bàn phím và tính diện tích hình tròn

### Bài 14: Nhập tên, họ, quốc gia và tuổi từ người dùng

### Bài 15: Chạy lệnh `help("keywords")` để xem các từ khóa trong Python

---
