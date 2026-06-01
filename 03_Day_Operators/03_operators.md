# Day 03 - Toán Tử và Boolean Trong Python

## Mục tiêu bài học

Ở ngày thứ 3, mình sẽ học về **Boolean** và các loại **toán tử trong Python**.

Sau bài này, mình cần nắm được:

* Boolean là gì
* Giá trị `True` và `False` trong Python
* Toán tử gán
* Toán tử số học
* Toán tử so sánh
* Toán tử logic
* Cách dùng `and`, `or`, `not`
* Cách áp dụng toán tử để tính toán các bài toán cơ bản

---

## 1. Boolean trong Python

Boolean là một kiểu dữ liệu chỉ có 2 giá trị:

* `True`
* `False`

Trong Python, chữ cái đầu của `True` và `False` phải viết hoa.

Ví dụ:

```python
print(True)
print(False)
```

Kết quả:

```python
True
False
```

Boolean thường được dùng khi mình cần kiểm tra một điều kiện nào đó là đúng hay sai.

Ví dụ:

```python
print(3 > 2)
print(3 < 2)
```

Kết quả:

```python
True
False
```

Trong ví dụ trên:

* `3 > 2` là đúng nên kết quả là `True`
* `3 < 2` là sai nên kết quả là `False`

---

## 2. Toán tử trong Python

Toán tử là các ký hiệu hoặc từ khóa dùng để thực hiện phép tính hoặc so sánh trong Python.

Ví dụ:

```python
print(5 + 3)
print(10 > 5)
```

Trong Python có nhiều loại toán tử khác nhau.
Ở Day 03, mình sẽ học các nhóm toán tử chính sau:

* Toán tử gán
* Toán tử số học
* Toán tử so sánh
* Toán tử logic

---

## 3. Toán tử gán

Toán tử gán dùng để gán giá trị cho biến.

Toán tử gán cơ bản nhất là dấu `=`.

Ví dụ:

```python
name = "Luyen"
age = 20
```

Trong ví dụ trên:

* Biến `name` được gán giá trị `"Luyen"`
* Biến `age` được gán giá trị `20`

Lưu ý:

Trong Python, dấu `=` không có nghĩa là so sánh bằng.
Nó có nghĩa là **gán giá trị**.

Ví dụ:

```python
x = 10
```

Nghĩa là gán giá trị `10` cho biến `x`.

---

## 4. Một số toán tử gán thường dùng

| Toán tử | Ví dụ     | Ý nghĩa                      |
| :------ | :-------- | :--------------------------- |
| `=`     | `x = 5`   | Gán giá trị `5` cho biến `x` |
| `+=`    | `x += 3`  | Tương đương `x = x + 3`      |
| `-=`    | `x -= 3`  | Tương đương `x = x - 3`      |
| `*=`    | `x *= 3`  | Tương đương `x = x * 3`      |
| `/=`    | `x /= 3`  | Tương đương `x = x / 3`      |
| `%=`    | `x %= 3`  | Tương đương `x = x % 3`      |
| `//=`   | `x //= 3` | Tương đương `x = x // 3`     |
| `**=`   | `x **= 3` | Tương đương `x = x ** 3`     |

Ví dụ:

```python
x = 10

x += 5
print(x)
```

Kết quả:

```python
15
```

Giải thích:

Ban đầu `x = 10`.
Sau đó `x += 5` nghĩa là `x = x + 5`.
Vậy `x = 10 + 5 = 15`.

---

## 5. Toán tử số học

Toán tử số học dùng để thực hiện các phép tính toán học.

| Toán tử | Tên gọi              | Ví dụ    |
| :------ | :------------------- | :------- |
| `+`     | Cộng                 | `a + b`  |
| `-`     | Trừ                  | `a - b`  |
| `*`     | Nhân                 | `a * b`  |
| `/`     | Chia                 | `a / b`  |
| `%`     | Chia lấy dư          | `a % b`  |
| `//`    | Chia lấy phần nguyên | `a // b` |
| `**`    | Lũy thừa             | `a ** b` |

---

## 6. Ví dụ với toán tử số học

```python
print("Addition:", 1 + 2)
print("Subtraction:", 2 - 1)
print("Multiplication:", 2 * 3)
print("Division:", 4 / 2)
print("Modulus:", 3 % 2)
print("Floor division:", 7 // 2)
print("Exponentiation:", 2 ** 3)
```

Kết quả:

```python
Addition: 3
Subtraction: 1
Multiplication: 6
Division: 2.0
Modulus: 1
Floor division: 3
Exponentiation: 8
```

Giải thích nhanh:

* `+` dùng để cộng
* `-` dùng để trừ
* `*` dùng để nhân
* `/` dùng để chia, kết quả thường là số thực
* `%` dùng để lấy phần dư
* `//` dùng để chia lấy phần nguyên
* `**` dùng để tính lũy thừa

---

## 7. Sự khác nhau giữa `/`, `//` và `%`

Đây là 3 toán tử dễ bị nhầm.

### Toán tử `/`

Dùng để chia bình thường.

```python
print(7 / 2)
```

Kết quả:

```python
3.5
```

---

### Toán tử `//`

Dùng để chia lấy phần nguyên.

```python
print(7 // 2)
```

Kết quả:

```python
3
```

Vì `7 / 2 = 3.5`, nhưng `//` chỉ lấy phần nguyên là `3`.

---

### Toán tử `%`

Dùng để lấy phần dư.

```python
print(7 % 2)
```

Kết quả:

```python
1
```

Vì `7 chia 2` được `3` dư `1`.

---

## 8. Toán tử lũy thừa `**`

Toán tử `**` dùng để tính lũy thừa.

Ví dụ:

```python
print(2 ** 3)
```

Kết quả:

```python
8
```

Giải thích:

`2 ** 3` nghĩa là:

```text
2 x 2 x 2 = 8
```

Ví dụ khác:

```python
print(5 ** 2)
print(10 ** 3)
```

Kết quả:

```python
25
1000
```

---

## 9. Gán kết quả tính toán vào biến

Mình có thể thực hiện phép tính rồi lưu kết quả vào biến.

Ví dụ:

```python
a = 3
b = 2

total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

print("a + b =", total)
print("a - b =", diff)
print("a * b =", product)
print("a / b =", division)
print("a % b =", remainder)
print("a // b =", floor_division)
print("a ** b =", exponential)
```

Kết quả:

```python
a + b = 5
a - b = 1
a * b = 6
a / b = 1.5
a % b = 1
a // b = 1
a ** b = 9
```

---

## 10. Lưu ý khi đặt tên biến

Không nên đặt tên biến trùng với tên hàm có sẵn của Python.

Ví dụ không nên:

```python
sum = 10
```

Vì `sum()` là một hàm built-in trong Python.

Nên đặt tên khác rõ nghĩa hơn:

```python
total = 10
```

Tên biến nên rõ nghĩa để khi đọc lại code, mình hiểu biến đó dùng để làm gì.

---

## 11. Ứng dụng toán tử số học

Toán tử số học có thể dùng để giải các bài toán tính toán cơ bản.

Ví dụ: tính diện tích hình tròn.

```python
radius = 10
pi = 3.14

area_of_circle = pi * radius ** 2

print("Area of circle:", area_of_circle)
```

Kết quả:

```python
Area of circle: 314.0
```

---

Ví dụ: tính diện tích hình chữ nhật.

```python
length = 10
width = 20

area_of_rectangle = length * width

print("Area of rectangle:", area_of_rectangle)
```

Kết quả:

```python
Area of rectangle: 200
```

---

Ví dụ: tính trọng lượng của một vật.

```python
mass = 75
gravity = 9.81

weight = mass * gravity

print(weight, "N")
```

Kết quả:

```python
735.75 N
```

---

Ví dụ: tính khối lượng riêng.

```python
mass = 75
volume = 0.075

density = mass / volume

print(density, "Kg/m^3")
```

Kết quả:

```python
1000.0 Kg/m^3
```

---

## 12. Toán tử so sánh

Toán tử so sánh dùng để so sánh hai giá trị.

Kết quả của phép so sánh luôn là Boolean:

* `True`
* `False`

| Toán tử | Ý nghĩa           | Ví dụ    |
| :------ | :---------------- | :------- |
| `>`     | Lớn hơn           | `a > b`  |
| `<`     | Nhỏ hơn           | `a < b`  |
| `>=`    | Lớn hơn hoặc bằng | `a >= b` |
| `<=`    | Nhỏ hơn hoặc bằng | `a <= b` |
| `==`    | Bằng nhau         | `a == b` |
| `!=`    | Khác nhau         | `a != b` |

---

## 13. Ví dụ với toán tử so sánh

```python
print(3 > 2)
print(3 >= 2)
print(3 < 2)
print(2 < 3)
print(2 <= 3)
print(3 == 2)
print(3 != 2)
```

Kết quả:

```python
True
True
False
True
True
False
True
```

Giải thích:

* `3 > 2` đúng nên kết quả là `True`
* `3 < 2` sai nên kết quả là `False`
* `3 == 2` sai vì 3 không bằng 2
* `3 != 2` đúng vì 3 khác 2

---

## 14. Phân biệt `=` và `==`

Đây là phần rất quan trọng.

### Dấu `=`

Dùng để gán giá trị.

```python
x = 10
```

Nghĩa là gán giá trị `10` cho biến `x`.

---

### Dấu `==`

Dùng để so sánh hai giá trị có bằng nhau hay không.

```python
print(10 == 10)
print(10 == 5)
```

Kết quả:

```python
True
False
```

Tóm lại:

| Ký hiệu | Ý nghĩa      |
| :------ | :----------- |
| `=`     | Gán giá trị  |
| `==`    | So sánh bằng |

---

## 15. So sánh độ dài chuỗi

Mình có thể dùng `len()` kết hợp với toán tử so sánh.

Ví dụ:

```python
print(len("python") == len("dragon"))
print(len("python") > len("dragon"))
print(len("mango") < len("avocado"))
```

Kết quả:

```python
True
False
True
```

Giải thích:

* `"python"` có 6 ký tự
* `"dragon"` có 6 ký tự
* `"mango"` có 5 ký tự
* `"avocado"` có 7 ký tự

---

## 16. So sánh Boolean

Boolean cũng có thể được so sánh với nhau.

Ví dụ:

```python
print(True == True)
print(True == False)
print(False == False)
```

Kết quả:

```python
True
False
True
```

---

## 17. Toán tử `is`

Toán tử `is` dùng để kiểm tra hai biến có cùng là một đối tượng trong bộ nhớ hay không.

Ví dụ:

```python
x = 10
y = 10

print(x is y)
```

Kết quả:

```python
True
```

Tuy nhiên, khi mới học, mình nên hiểu đơn giản:

* `==` thường dùng để so sánh giá trị
* `is` dùng để so sánh đối tượng

Ví dụ:

```python
print(10 == 10)
print(10 is 10)
```

Kết quả thường là:

```python
True
True
```

Nhưng trong thực tế, khi so sánh giá trị bình thường, mình nên dùng `==`.

---

## 18. Toán tử `is not`

Toán tử `is not` dùng để kiểm tra hai biến không cùng là một đối tượng.

Ví dụ:

```python
x = 10
y = 20

print(x is not y)
```

Kết quả:

```python
True
```

---

## 19. Toán tử `in`

Toán tử `in` dùng để kiểm tra một giá trị có nằm trong một chuỗi, list hoặc tập dữ liệu nào đó hay không.

Ví dụ:

```python
print("a" in "apple")
print("z" in "apple")
```

Kết quả:

```python
True
False
```

Giải thích:

* Chữ `"a"` có trong `"apple"` nên kết quả là `True`
* Chữ `"z"` không có trong `"apple"` nên kết quả là `False`

Ví dụ khác:

```python
print("python" in "I am learning python")
```

Kết quả:

```python
True
```

---

## 20. Toán tử `not in`

Toán tử `not in` dùng để kiểm tra một giá trị không nằm trong một chuỗi, list hoặc tập dữ liệu nào đó.

Ví dụ:

```python
print("z" not in "apple")
print("a" not in "apple")
```

Kết quả:

```python
True
False
```

---

## 21. Toán tử logic

Toán tử logic dùng để kết hợp nhiều điều kiện lại với nhau.

Trong Python có 3 toán tử logic chính:

| Toán tử | Ý nghĩa  |
| :------ | :------- |
| `and`   | Và       |
| `or`    | Hoặc     |
| `not`   | Phủ định |

---

## 22. Toán tử `and`

Toán tử `and` trả về `True` khi tất cả điều kiện đều đúng.

Ví dụ:

```python
print(3 > 2 and 4 > 3)
print(3 > 2 and 4 < 3)
```

Kết quả:

```python
True
False
```

Giải thích:

* `3 > 2 and 4 > 3` là `True` vì cả hai điều kiện đều đúng
* `3 > 2 and 4 < 3` là `False` vì điều kiện thứ hai sai

Bảng dễ nhớ:

| Điều kiện 1 | Điều kiện 2 | Kết quả với `and` |
| :---------: | :---------: | :---------------: |
|     True    |     True    |        True       |
|     True    |    False    |       False       |
|    False    |     True    |       False       |
|    False    |    False    |       False       |

---

## 23. Toán tử `or`

Toán tử `or` trả về `True` nếu có ít nhất một điều kiện đúng.

Ví dụ:

```python
print(3 > 2 or 4 > 3)
print(3 > 2 or 4 < 3)
print(3 < 2 or 4 < 3)
```

Kết quả:

```python
True
True
False
```

Giải thích:

* Nếu một trong hai điều kiện đúng thì kết quả là `True`
* Chỉ khi tất cả điều kiện đều sai thì kết quả mới là `False`

Bảng dễ nhớ:

| Điều kiện 1 | Điều kiện 2 | Kết quả với `or` |
| :---------: | :---------: | :--------------: |
|     True    |     True    |       True       |
|     True    |    False    |       True       |
|    False    |     True    |       True       |
|    False    |    False    |       False      |

---

## 24. Toán tử `not`

Toán tử `not` dùng để đảo ngược giá trị Boolean.

Ví dụ:

```python
print(not True)
print(not False)
```

Kết quả:

```python
False
True
```

Ví dụ khác:

```python
print(not 3 > 2)
```

Kết quả:

```python
False
```

Giải thích:

* `3 > 2` là `True`
* `not True` thành `False`

---

## 25. Kết hợp nhiều toán tử

Mình có thể kết hợp toán tử so sánh và toán tử logic trong cùng một biểu thức.

Ví dụ:

```python
age = 20
is_student = True

print(age >= 18 and is_student == True)
```

Kết quả:

```python
True
```

Giải thích:

* `age >= 18` là `True`
* `is_student == True` là `True`
* `True and True` nên kết quả cuối cùng là `True`

Ví dụ khác:

```python
username = "admin"
password = "123456"

print(username == "admin" and password == "123456")
```

Kết quả:

```python
True
```

---

## 26. Một số lỗi dễ gặp

### Lỗi 1: Nhầm `=` với `==`

Sai:

```python
print(5 = 5)
```

Đúng:

```python
print(5 == 5)
```

---

### Lỗi 2: Viết sai `True` và `False`

Sai:

```python
print(true)
print(false)
```

Đúng:

```python
print(True)
print(False)
```

Trong Python, `True` và `False` phải viết hoa chữ cái đầu.

---

### Lỗi 3: Nhầm `/` và `//`

```python
print(7 / 2)
print(7 // 2)
```

Kết quả:

```python
3.5
3
```

* `/` là chia bình thường
* `//` là chia lấy phần nguyên

---

### Lỗi 4: Dùng `and` khi nên dùng `or`

Ví dụ:

```python
age = 16

print(age < 18 or age > 60)
```

Điều kiện này kiểm tra người có tuổi nhỏ hơn 18 hoặc lớn hơn 60.

Nếu dùng `and`:

```python
print(age < 18 and age > 60)
```

Kết quả sẽ không hợp lý, vì một người không thể vừa nhỏ hơn 18 vừa lớn hơn 60 cùng lúc.

---

## 27. Tổng kết Day 03

Sau Day 03, mình đã học được:

* Boolean là kiểu dữ liệu chỉ có hai giá trị: `True` và `False`
* Toán tử gán dùng để gán giá trị cho biến
* Dấu `=` dùng để gán giá trị
* Dấu `==` dùng để so sánh bằng
* Toán tử số học dùng để tính toán
* `/` là chia bình thường
* `//` là chia lấy phần nguyên
* `%` là chia lấy dư
* `**` là lũy thừa
* Toán tử so sánh trả về kết quả Boolean
* `in` dùng để kiểm tra một giá trị có nằm trong dữ liệu hay không
* `not in` dùng để kiểm tra một giá trị không nằm trong dữ liệu
* `and` đúng khi tất cả điều kiện đều đúng
* `or` đúng khi có ít nhất một điều kiện đúng
* `not` dùng để đảo ngược giá trị Boolean

---

# Bài tập Day 03

## Level 1

### Bài 1: Khai báo biến `age` lưu tuổi của bạn dưới dạng số nguyên

### Bài 2: Khai báo biến `height` lưu chiều cao của bạn dưới dạng số thực

### Bài 3: Khai báo một biến lưu số phức

### Bài 4: Nhập đáy và chiều cao của tam giác, sau đó tính diện tích tam giác

### Bài 5: Nhập ba cạnh của tam giác, sau đó tính chu vi tam giác

### Bài 6: Nhập chiều dài và chiều rộng của hình chữ nhật, sau đó tính diện tích và chu vi

### Bài 7: Nhập bán kính hình tròn, sau đó tính diện tích và chu vi hình tròn

### Bài 8: Tính hệ số góc, giao điểm với trục x và giao điểm với trục y của phương trình `y = 2x - 2`

### Bài 9: Tính hệ số góc và khoảng cách Euclid giữa hai điểm `(2, 2)` và `(6, 10)`

### Bài 10: So sánh hệ số góc ở bài 8 và bài 9

### Bài 11: Tính giá trị của `y = x^2 + 6x + 9` với nhiều giá trị `x` khác nhau và tìm `x` để `y = 0`

### Bài 12: Tìm độ dài của chuỗi `"python"` và `"dragon"`, sau đó tạo một phép so sánh cho kết quả `False`

### Bài 13: Dùng toán tử `and` để kiểm tra `"on"` có nằm trong cả `"python"` và `"dragon"` hay không

### Bài 14: Dùng toán tử `in` để kiểm tra từ `"jargon"` có nằm trong câu `"I hope this course is not full of jargon"` hay không

### Bài 15: Kiểm tra rằng không có `"on"` trong cả `"dragon"` và `"python"`

### Bài 16: Tìm độ dài của chuỗi `"python"`, sau đó chuyển kết quả sang `float` rồi chuyển sang `str`

### Bài 17: Kiểm tra một số có phải là số chẵn hay không

### Bài 18: Kiểm tra phép chia lấy phần nguyên của `7 // 3` có bằng giá trị `int(2.7)` hay không

### Bài 19: Kiểm tra kiểu dữ liệu của `"10"` có bằng kiểu dữ liệu của `10` hay không

### Bài 20: Kiểm tra `int("9.8")` có bằng `10` hay không

### Bài 21: Nhập số giờ làm và tiền công mỗi giờ, sau đó tính tiền lương theo tuần

### Bài 22: Nhập số năm đã sống, sau đó tính số giây tương ứng

### Bài 23: Viết chương trình hiển thị bảng số theo mẫu trong bài Day 03

---
