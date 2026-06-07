# Day 04 - Strings Trong Python

## Mục tiêu bài học

Ở ngày thứ 4, mình sẽ học về String trong Python.

String là kiểu dữ liệu dùng để lưu trữ văn bản. Đây là một kiểu dữ liệu rất quan trọng vì khi lập trình, mình thường xuyên phải làm việc với tên, địa chỉ, email, câu văn, dữ liệu nhập từ người dùng,...

Sau bài này, mình cần nắm được:

* String là gì
* Cách tạo chuỗi trong Python
* Cách nối chuỗi
* Cách dùng escape sequence
* Cách định dạng chuỗi
* Cách truy cập từng ký tự trong chuỗi
* Cách cắt chuỗi bằng slicing
* Cách đảo ngược chuỗi
* Các string methods thường dùng

---

## 1. String trong Python

String là kiểu dữ liệu dùng để biểu diễn văn bản.

Trong Python, string có thể được viết bằng:

* Dấu nháy đơn `' '`
* Dấu nháy kép `" "`
* Ba dấu nháy đơn `''' '''`
* Ba dấu nháy kép `""" """`

Ví dụ:

```
letter = 'P'
print(letter)

name = "Lê Công Luyến"
print(name)

sentence = "Tôi đang học Python"
print(sentence)
```

Kết quả:

```
P
Lê Công Luyến
Tôi đang học Python
```

Trong ví dụ trên:

* Biến `letter` lưu một ký tự
* Biến `name` lưu họ tên
* Biến `sentence` lưu một câu văn

---

## 2. Kiểm tra độ dài của chuỗi

Để kiểm tra độ dài của một chuỗi, mình dùng hàm `len()`.

Hàm `len()` sẽ trả về số lượng ký tự có trong chuỗi.

Ví dụ:

```
name = "Lê Công Luyến"

print(len(name))
```

Kết quả:

```
13
```

Lưu ý:

Khoảng trắng cũng được tính là một ký tự.

Ví dụ:

```
first_name = "Lê Công"
last_name = "Luyến"
full_name = "Lê Công Luyến"

print(len(first_name))
print(len(last_name))
print(len(full_name))
```

Kết quả:

```
7
5
13
```

Giải thích:

* `"Lê Công"` có 7 ký tự, tính cả khoảng trắng
* `"Luyến"` có 5 ký tự
* `"Lê Công Luyến"` có 13 ký tự, tính cả 2 khoảng trắng

---

## 3. Chuỗi nhiều dòng

Khi muốn viết một chuỗi có nhiều dòng, mình dùng ba dấu nháy đơn hoặc ba dấu nháy kép.

Ví dụ:

```
information = '''Tôi tên là Lê Công Luyến.
Tôi 20 tuổi.
Tôi sống ở Hồ Chí Minh City, Việt Nam.'''

print(information)
```

Kết quả:

```
Tôi tên là Lê Công Luyến.
Tôi 20 tuổi.
Tôi sống ở Hồ Chí Minh City, Việt Nam.
```

Cách này thường dùng khi mình muốn viết đoạn văn bản dài hoặc nhiều dòng.

---

## 4. Nối chuỗi trong Python

Nối chuỗi là ghép nhiều chuỗi lại với nhau.

Trong Python, mình dùng dấu `+` để nối chuỗi.

Ví dụ:

```
first_name = "Lê Công"
last_name = "Luyến"

full_name = first_name + last_name

print(full_name)
```

Kết quả:

```
Lê CôngLuyến
```

Kết quả bị dính liền vì giữa `first_name` và `last_name` chưa có khoảng trắng.

Muốn có khoảng trắng, mình thêm một chuỗi `" "` ở giữa.

Ví dụ:

```
first_name = "Lê Công"
last_name = "Luyến"
space = " "

full_name = first_name + space + last_name

print(full_name)
```

Kết quả:

```
Lê Công Luyến
```

Giải thích:

* `first_name` chứa `"Lê Công"`
* `space` chứa khoảng trắng
* `last_name` chứa `"Luyến"`
* Khi nối lại sẽ được `"Lê Công Luyến"`

---

## 5. Ví dụ nối nhiều chuỗi

Mình có thể nối nhiều chuỗi để tạo thành một câu hoàn chỉnh.

Ví dụ:

```
first_name = "Lê Công"
last_name = "Luyến"
age = "20"
country = "Việt Nam"
city = "Hồ Chí Minh City"

sentence = "Tôi tên là " + first_name + " " + last_name + ". Tôi " + age + " tuổi. Tôi sống ở " + city + ", " + country + "."

print(sentence)
```

Kết quả:

```
Tôi tên là Lê Công Luyến. Tôi 20 tuổi. Tôi sống ở Hồ Chí Minh City, Việt Nam.
```

Lưu ý:

Nếu muốn nối số với chuỗi bằng dấu `+`, số đó cần được chuyển thành string trước.

Ví dụ sai:

```
age = 20
print("Tôi " + age + " tuổi")
```

Ví dụ đúng:

```
age = 20
print("Tôi " + str(age) + " tuổi")
```

Kết quả:

```
Tôi 20 tuổi
```

---

## 6. Escape Sequence trong Python

Escape sequence là các ký tự đặc biệt trong chuỗi.

Nó bắt đầu bằng dấu gạch chéo ngược `\`.

Một số escape sequence thường dùng:

Escape Sequence Ý nghĩa
`\n` Xuống dòng mới
`\t` Tạo khoảng tab
`\\` In ra dấu gạch chéo ngược
`\'` In ra dấu nháy đơn
`\"` In ra dấu nháy kép

Ví dụ:

```
print("Tôi tên là Lê Công Luyến.\nTôi 20 tuổi.")
print("Tên\tTuổi\tQuốc gia")
print("Luyến\t20\tViệt Nam")
```

Kết quả:

```
Tôi tên là Lê Công Luyến.
Tôi 20 tuổi.
Tên    Tuổi    Quốc gia
Luyến  20      Việt Nam
```

Giải thích:

* `\n` dùng để xuống dòng
* `\t` dùng để tạo khoảng cách dạng tab

---

## 7. In dấu nháy trong chuỗi

Nếu trong chuỗi có dấu nháy, mình có thể dùng escape sequence để tránh lỗi.

Ví dụ:

```
print("Python bắt đầu bằng câu: \"Hello, World!\"")
```

Kết quả:

```
Python bắt đầu bằng câu: "Hello, World!"
```

Ví dụ khác:

```
print('It\'s Python')
```

Kết quả:

```
It's Python
```

Giải thích:

* `\"` giúp in dấu nháy kép
* `\'` giúp in dấu nháy đơn

---

## 8. Định dạng chuỗi trong Python

Định dạng chuỗi giúp mình đưa giá trị của biến vào trong chuỗi dễ hơn.

Trong Python có nhiều cách định dạng chuỗi:

* Dùng `%`
* Dùng `.format()`
* Dùng f-string

Trong đó, f-string là cách dễ đọc và thường được dùng nhiều nhất hiện nay.

---

## 9. Định dạng chuỗi bằng `%`

Đây là cách định dạng chuỗi kiểu cũ.

Một số ký hiệu thường dùng:

Ký hiệu Ý nghĩa
`%s` Chuỗi
`%d` Số nguyên
`%f` Số thực
`%.2f` Số thực lấy 2 chữ số sau dấu phẩy

Ví dụ:

```
first_name = "Lê Công"
last_name = "Luyến"
age = 20
country = "Việt Nam"
city = "Hồ Chí Minh City"

sentence = "Tôi tên là %s %s. Tôi %d tuổi. Tôi sống ở %s, %s." % (first_name, last_name, age, city, country)

print(sentence)
```

Kết quả:

```
Tôi tên là Lê Công Luyến. Tôi 20 tuổi. Tôi sống ở Hồ Chí Minh City, Việt Nam.
```

Ví dụ với số thực:

```
radius = 10
pi = 3.14
area = pi * radius ** 2

result = "Diện tích hình tròn có bán kính %d là %.2f." % (radius, area)

print(result)
```

Kết quả:

```
Diện tích hình tròn có bán kính 10 là 314.00.
```

---

## 10. Định dạng chuỗi bằng `.format()`

Cách này dùng dấu `{}` để đánh dấu vị trí cần chèn dữ liệu.

Ví dụ:

```
first_name = "Lê Công"
last_name = "Luyến"
age = 20
country = "Việt Nam"
city = "Hồ Chí Minh City"

sentence = "Tôi tên là {} {}. Tôi {} tuổi. Tôi sống ở {}, {}.".format(first_name, last_name, age, city, country)

print(sentence)
```

Kết quả:

```
Tôi tên là Lê Công Luyến. Tôi 20 tuổi. Tôi sống ở Hồ Chí Minh City, Việt Nam.
```

Ví dụ với phép toán:

```
a = 4
b = 3

print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))
```

Kết quả:

```
4 + 3 = 7
4 - 3 = 1
4 * 3 = 12
4 / 3 = 1.33
```

---

## 11. Định dạng chuỗi bằng f-string

f-string là cách định dạng chuỗi ngắn gọn và dễ đọc.

Để dùng f-string, mình đặt chữ `f` trước chuỗi, sau đó đặt biến vào trong dấu `{}`.

Ví dụ:

```
first_name = "Lê Công"
last_name = "Luyến"
age = 20
country = "Việt Nam"
city = "Hồ Chí Minh City"

print(f"Tôi tên là {first_name} {last_name}.")
print(f"Tôi {age} tuổi.")
print(f"Tôi sống ở {city}, {country}.")
```

Kết quả:

```
Tôi tên là Lê Công Luyến.
Tôi 20 tuổi.
Tôi sống ở Hồ Chí Minh City, Việt Nam.
```

Ví dụ với phép toán:

```
a = 4
b = 3

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
```

Kết quả:

```
4 + 3 = 7
4 - 3 = 1
4 * 3 = 12
4 / 3 = 1.33
```

Ghi nhớ:

Nên ưu tiên dùng f-string vì nó dễ đọc và dễ viết hơn.

---

## 12. String là một chuỗi các ký tự

Trong Python, string được xem như một dãy các ký tự.

Mỗi ký tự trong string có một vị trí gọi là index.

Index trong Python bắt đầu từ `0`.

Ví dụ:

```
language = "Python"

print(language[0])
print(language[1])
print(language[2])
print(language[3])
print(language[4])
print(language[5])
```

Kết quả:

```
P
y
t
h
o
n
```

Giải thích:

Chuỗi `"Python"` có các index như sau:

```
P   y   t   h   o   n
0   1   2   3   4   5
```

---

## 13. Truy cập ký tự bằng index

Mình có thể lấy từng ký tự trong chuỗi bằng cách dùng dấu ngoặc vuông `[]`.

Ví dụ:

```
name = "Luyến"

first_letter = name[0]
second_letter = name[1]
last_letter = name[-1]

print(first_letter)
print(second_letter)
print(last_letter)
```

Kết quả:

```
L
u
n
```

Giải thích:

* `name[0]` lấy ký tự đầu tiên
* `name[1]` lấy ký tự thứ hai
* `name[-1]` lấy ký tự cuối cùng

---

## 14. Index âm trong Python

Ngoài index dương, Python còn hỗ trợ index âm.

Index âm sẽ đếm từ cuối chuỗi về đầu chuỗi.

Ví dụ:

```
language = "Python"

print(language[-1])
print(language[-2])
print(language[-3])
```

Kết quả:

```
n
o
h
```

Giải thích:

* `-1` là ký tự cuối cùng
* `-2` là ký tự gần cuối
* `-3` là ký tự đứng trước `-2`

---

## 15. Tách ký tự trong chuỗi

Mình có thể tách các ký tự trong chuỗi và gán cho nhiều biến.

Ví dụ:

```
language = "Python"

a, b, c, d, e, f = language

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
```

Kết quả:

```
P
y
t
h
o
n
```

Lưu ý:

Số lượng biến phải bằng số lượng ký tự trong chuỗi.

---

## 16. Cắt chuỗi - Slicing

Slicing dùng để lấy một phần của chuỗi.

Cú pháp:

```
string[start:end]
```

Trong đó:

* `start` là vị trí bắt đầu
* `end` là vị trí kết thúc
* Ký tự ở vị trí `end` sẽ không được lấy

Ví dụ:

```
language = "Python"

first_three = language[0:3]
last_three = language[3:6]

print(first_three)
print(last_three)
```

Kết quả:

```
Pyt
hon
```

Giải thích:

* `language[0:3]` lấy từ index `0` đến trước index `3`
* `language[3:6]` lấy từ index `3` đến trước index `6`

---

## 17. Một số cách slicing thường dùng

Ví dụ:

```
city = "Ho Chi Minh City"

print(city[0:2])
print(city[3:6])
print(city[7:11])
print(city[-4:])
```

Kết quả:

```
Ho
Chi
Minh
City
```

Giải thích:

* `city[0:2]` lấy `"Ho"`
* `city[3:6]` lấy `"Chi"`
* `city[7:11]` lấy `"Minh"`
* `city[-4:]` lấy 4 ký tự cuối

---

## 18. Bỏ trống start hoặc end khi slicing

Khi slicing, mình có thể bỏ trống `start` hoặc `end`.

Ví dụ:

```
language = "Python"

print(language[:3])
print(language[3:])
print(language[:])
```

Kết quả:

```
Pyt
hon
Python
```

Giải thích:

* `language[:3]` lấy từ đầu đến trước index `3`
* `language[3:]` lấy từ index `3` đến hết
* `language[:]` lấy toàn bộ chuỗi

---

## 19. Đảo ngược chuỗi

Để đảo ngược chuỗi, mình dùng slicing với cú pháp `[::-1]`.

Ví dụ:

```
greeting = "Hello, World!"

print(greeting[::-1])
```

Kết quả:

```
!dlroW ,olleH
```

Ví dụ khác:

```
name = "Luyen"

print(name[::-1])
```

Kết quả:

```
neyuL
```

Giải thích:

`[::-1]` nghĩa là đi từ cuối chuỗi về đầu chuỗi.

---

## 20. Bỏ qua ký tự khi slicing

Slicing có thể có thêm bước nhảy.

Cú pháp:

```
string[start:end:step]
```

Ví dụ:

```
language = "Python"

result = language[0:6:2]

print(result)
```

Kết quả:

```
Pto
```

Giải thích:

* Chuỗi ban đầu là `"Python"`
* Lấy từ index `0` đến trước index `6`
* Mỗi lần nhảy 2 bước
* Kết quả là `"Pto"`

---

## 21. String Methods trong Python

String methods là các hàm có sẵn để xử lý chuỗi.

Một số string methods thường dùng:

Method Ý nghĩa
`capitalize()` Viết hoa chữ cái đầu tiên
`count()` Đếm số lần xuất hiện của chuỗi con
`endswith()` Kiểm tra chuỗi có kết thúc bằng một chuỗi khác không
`find()` Tìm vị trí xuất hiện đầu tiên của chuỗi con
`rfind()` Tìm vị trí xuất hiện cuối cùng của chuỗi con
`format()` Định dạng chuỗi
`isalnum()` Kiểm tra chuỗi có gồm chữ và số không
`isalpha()` Kiểm tra chuỗi có toàn chữ cái không
`isdigit()` Kiểm tra chuỗi có toàn chữ số không
`isidentifier()` Kiểm tra chuỗi có hợp lệ làm tên biến không
`islower()` Kiểm tra chuỗi có toàn chữ thường không
`isupper()` Kiểm tra chuỗi có toàn chữ hoa không
`join()` Nối các phần tử thành chuỗi
`strip()` Xóa khoảng trắng ở đầu và cuối chuỗi
`replace()` Thay thế chuỗi con
`split()` Tách chuỗi thành list
`title()` Viết hoa chữ cái đầu của mỗi từ
`swapcase()` Đổi chữ hoa thành chữ thường và ngược lại
`startswith()` Kiểm tra chuỗi có bắt đầu bằng một chuỗi khác không

---

## 22. Method `capitalize()`

Method `capitalize()` dùng để viết hoa chữ cái đầu tiên của chuỗi.

Ví dụ:

```
challenge = "thirty days of python"

print(challenge.capitalize())
```

Kết quả:

```
Thirty days of python
```

Giải thích:

Chỉ chữ cái đầu tiên của cả chuỗi được viết hoa.

---

## 23. Method `count()`

Method `count()` dùng để đếm số lần xuất hiện của một ký tự hoặc một chuỗi con.

Ví dụ:

```
challenge = "thirty days of python"

print(challenge.count("y"))
print(challenge.count("th"))
```

Kết quả:

```
3
2
```

Giải thích:

* Chữ `"y"` xuất hiện 3 lần
* Chuỗi `"th"` xuất hiện 2 lần

---

## 24. Method `endswith()`

Method `endswith()` dùng để kiểm tra chuỗi có kết thúc bằng một chuỗi khác hay không.

Ví dụ:

```
challenge = "thirty days of python"

print(challenge.endswith("on"))
print(challenge.endswith("tion"))
```

Kết quả:

```
True
False
```

Giải thích:

* `"thirty days of python"` kết thúc bằng `"on"` nên kết quả là `True`
* Chuỗi này không kết thúc bằng `"tion"` nên kết quả là `False`

---

## 25. Method `find()`

Method `find()` dùng để tìm vị trí xuất hiện đầu tiên của một ký tự hoặc chuỗi con.

Ví dụ:

```
challenge = "thirty days of python"

print(challenge.find("y"))
print(challenge.find("th"))
```

Kết quả:

```
5
0
```

Giải thích:

* Ký tự `"y"` đầu tiên nằm ở index `5`
* Chuỗi `"th"` đầu tiên bắt đầu ở index `0`

Nếu không tìm thấy, `find()` sẽ trả về `-1`.

Ví dụ:

```
challenge = "thirty days of python"

print(challenge.find("java"))
```

Kết quả:

```
-1
```

---

## 26. Method `rfind()`

Method `rfind()` dùng để tìm vị trí xuất hiện cuối cùng của một ký tự hoặc chuỗi con.

Ví dụ:

```
challenge = "thirty days of python"

print(challenge.rfind("y"))
```

Kết quả:

```
16
```

Giải thích:

`rfind()` tìm từ bên phải qua bên trái, nhưng kết quả vẫn là index tính từ trái sang phải.

---

## 27. Method `isalnum()`

Method `isalnum()` kiểm tra chuỗi có chỉ gồm chữ cái và chữ số hay không.

Ví dụ:

```
print("Python3".isalnum())
print("Python 3".isalnum())
```

Kết quả:

```
True
False
```

Giải thích:

* `"Python3"` chỉ gồm chữ và số nên kết quả là `True`
* `"Python 3"` có khoảng trắng nên kết quả là `False`

---

## 28. Method `isalpha()`

Method `isalpha()` kiểm tra chuỗi có chỉ gồm chữ cái hay không.

Ví dụ:

```
print("Python".isalpha())
print("Python3".isalpha())
```

Kết quả:

```
True
False
```

Giải thích:

* `"Python"` chỉ có chữ cái nên kết quả là `True`
* `"Python3"` có số `3` nên kết quả là `False`

---

## 29. Method `isdigit()`

Method `isdigit()` kiểm tra chuỗi có chỉ gồm chữ số hay không.

Ví dụ:

```
print("123".isdigit())
print("123abc".isdigit())
```

Kết quả:

```
True
False
```

Giải thích:

* `"123"` chỉ gồm chữ số nên kết quả là `True`
* `"123abc"` có chữ cái nên kết quả là `False`

---

## 30. Method `isidentifier()`

Method `isidentifier()` kiểm tra chuỗi có hợp lệ để làm tên biến trong Python hay không.

Ví dụ:

```
print("first_name".isidentifier())
print("first-name".isidentifier())
print("1first_name".isidentifier())
```

Kết quả:

```
True
False
False
```

Giải thích:

* `first_name` hợp lệ vì có chữ cái và dấu gạch dưới
* `first-name` không hợp lệ vì có dấu `-`
* `1first_name` không hợp lệ vì tên biến không được bắt đầu bằng số

---

## 31. Method `islower()` và `isupper()`

Method `islower()` kiểm tra chuỗi có toàn chữ thường hay không.

Method `isupper()` kiểm tra chuỗi có toàn chữ hoa hay không.

Ví dụ:

```
print("python".islower())
print("Python".islower())
print("PYTHON".isupper())
print("Python".isupper())
```

Kết quả:

```
True
False
True
False
```

Giải thích:

* `"python"` toàn chữ thường nên `islower()` trả về `True`
* `"PYTHON"` toàn chữ hoa nên `isupper()` trả về `True`

---

## 32. Method `join()`

Method `join()` dùng để nối các phần tử trong một list thành một chuỗi.

Ví dụ:

```
words = ["Thirty", "Days", "Of", "Python"]

sentence = " ".join(words)

print(sentence)
```

Kết quả:

```
Thirty Days Of Python
```

Ví dụ khác:

```
words = ["30", "Days", "Python"]

result = "-".join(words)

print(result)
```

Kết quả:

```
30-Days-Python
```

Giải thích:

* `" ".join(words)` nối các phần tử bằng khoảng trắng
* `"-".join(words)` nối các phần tử bằng dấu gạch ngang

---

## 33. Method `strip()`

Method `strip()` dùng để xóa khoảng trắng ở đầu và cuối chuỗi.

Ví dụ:

```
city = "   Hồ Chí Minh City   "

print(city.strip())
```

Kết quả:

```
Hồ Chí Minh City
```

Giải thích:

Khoảng trắng ở đầu và cuối chuỗi đã bị xóa.

---

## 34. Method `replace()`

Method `replace()` dùng để thay thế một chuỗi con bằng chuỗi khác.

Ví dụ:

```
challenge = "thirty days of python"

print(challenge.replace("python", "coding"))
```

Kết quả:

```
thirty days of coding
```

Giải thích:

Chuỗi `"python"` đã được thay bằng `"coding"`.

---

## 35. Method `split()`

Method `split()` dùng để tách một chuỗi thành list.

Ví dụ:

```
sentence = "Tôi sống ở Hồ Chí Minh City"

print(sentence.split())
```

Kết quả:

```
['Tôi', 'sống', 'ở', 'Hồ', 'Chí', 'Minh', 'City']
```

Giải thích:

Mặc định, `split()` sẽ tách chuỗi dựa trên khoảng trắng.

Ví dụ khác:

```
data = "Lê Công Luyến,20,Việt Nam,Hồ Chí Minh City"

print(data.split(","))
```

Kết quả:

```
['Lê Công Luyến', '20', 'Việt Nam', 'Hồ Chí Minh City']
```

---

## 36. Method `title()`

Method `title()` dùng để viết hoa chữ cái đầu tiên của mỗi từ.

Ví dụ:

```
text = "le cong luyen"

print(text.title())
```

Kết quả:

```
Le Cong Luyen
```

Giải thích:

Mỗi từ trong chuỗi đều được viết hoa chữ cái đầu.

---

## 37. Method `swapcase()`

Method `swapcase()` dùng để đổi chữ hoa thành chữ thường và chữ thường thành chữ hoa.

Ví dụ:

```
text = "Python Is Fun"

print(text.swapcase())
```

Kết quả:

```
pYTHON iS fUN
```

Giải thích:

* Chữ hoa đổi thành chữ thường
* Chữ thường đổi thành chữ hoa

---

## 38. Method `startswith()`

Method `startswith()` dùng để kiểm tra chuỗi có bắt đầu bằng một chuỗi khác hay không.

Ví dụ:

```
city = "Hồ Chí Minh City"

print(city.startswith("Hồ"))
print(city.startswith("Đà"))
```

Kết quả:

```
True
False
```

Giải thích:

* `"Hồ Chí Minh City"` bắt đầu bằng `"Hồ"` nên kết quả là `True`
* Chuỗi này không bắt đầu bằng `"Đà"` nên kết quả là `False`

---
## 40. Tổng kết bài học

Sau Day 04, mình đã học được:

* String là kiểu dữ liệu dùng để lưu văn bản
* Có thể tạo string bằng nháy đơn, nháy kép hoặc ba dấu nháy
* Dùng `+` để nối chuỗi
* Dùng `len()` để kiểm tra độ dài chuỗi
* Dùng escape sequence như `\n`, `\t`, `\\`, `\"`, `\'`
* Có thể định dạng chuỗi bằng `%`, `.format()` hoặc f-string
* String có index bắt đầu từ `0`
* Có thể dùng index âm để lấy ký tự từ cuối chuỗi
* Có thể dùng slicing để cắt chuỗi
* Có thể dùng `[::-1]` để đảo ngược chuỗi
* String methods giúp xử lý chuỗi nhanh hơn

---

* * *

## Bài tập - Day 04

1. Nối các chuỗi `'Thirty'`, `'Days'`, `'Of'`, `'Python'` thành một chuỗi duy nhất: `'Thirty Days Of Python'`.

2. Nối các chuỗi `'Coding'`, `'For'`, `'All'` thành một chuỗi duy nhất: `'Coding For All'`.

3. Khai báo một biến tên là `company` và gán giá trị ban đầu là `"Coding For All"`.

4. In biến `company` bằng hàm `print()`.

5. In độ dài của chuỗi trong biến `company` bằng hàm `len()` và `print()`.

6. Chuyển tất cả ký tự trong biến `company` thành chữ hoa bằng method `upper()`.

7. Chuyển tất cả ký tự trong biến `company` thành chữ thường bằng method `lower()`.

8. Sử dụng các method `capitalize()`, `title()`, `swapcase()` để định dạng chuỗi `"Coding For All"`.

9. Cắt từ đầu tiên ra khỏi chuỗi `"Coding For All"`.

10. Kiểm tra chuỗi `"Coding For All"` có chứa từ `"Coding"` hay không bằng method `index()`, `find()` hoặc method khác.

11. Thay thế từ `"Coding"` trong chuỗi `"Coding For All"` thành `"Python"`.

12. Thay đổi chuỗi `"Python for Everyone"` thành `"Python for All"` bằng method `replace()` hoặc method khác.

13. Tách chuỗi `"Coding For All"` thành list bằng khoảng trắng làm dấu phân tách.

14. Tách chuỗi `"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"` thành list bằng dấu phẩy.

15. Lấy ký tự ở index `0` trong chuỗi `"Coding For All"`.

16. Tìm index cuối cùng của chuỗi `"Coding For All"`.

17. Lấy ký tự ở index `10` trong chuỗi `"Coding For All"`.

18. Tạo từ viết tắt cho tên `"Python For Everyone"`.

19. Tạo từ viết tắt cho tên `"Coding For All"`.

20. Dùng `index()` để tìm vị trí xuất hiện đầu tiên của ký tự `"C"` trong chuỗi `"Coding For All"`.

21. Dùng `index()` để tìm vị trí xuất hiện đầu tiên của ký tự `"F"` trong chuỗi `"Coding For All"`.

22. Dùng `rfind()` để tìm vị trí xuất hiện cuối cùng của ký tự `"l"` trong chuỗi `"Coding For All People"`.

23. Dùng `index()` hoặc `find()` để tìm vị trí xuất hiện đầu tiên của từ `"because"` trong câu: `"You cannot end a sentence with because because because is a conjunction"`.

24. Dùng `rindex()` để tìm vị trí xuất hiện cuối cùng của từ `"because"` trong câu: `"You cannot end a sentence with because because because is a conjunction"`.

25. Cắt cụm từ `"because because because"` ra khỏi câu: `"You cannot end a sentence with because because because is a conjunction"`.

26. Tìm vị trí xuất hiện đầu tiên của từ `"because"` trong câu: `"You cannot end a sentence with because because because is a conjunction"`.

27. Cắt cụm từ `"because because because"` ra khỏi câu: `"You cannot end a sentence with because because because is a conjunction"`.

28. Kiểm tra chuỗi `"Coding For All"` có bắt đầu bằng chuỗi con `"Coding"` hay không.

29. Kiểm tra chuỗi `"Coding For All"` có kết thúc bằng chuỗi con `"coding"` hay không.

30. Xóa khoảng trắng ở đầu và cuối chuỗi `"   Coding For All      "`.

31. Kiểm tra biến nào sau đây là tên biến hợp lệ trong Python: `"30DaysOfPython"` và `"thirty_days_of_python"`.

32. Danh sách sau chứa tên một số thư viện Python: `['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']`. Hãy nối các phần tử trong list thành một chuỗi, cách nhau bằng khoảng trắng.

33. Sử dụng escape sequence để in các dòng sau:

    I am enjoying this challenge.
    I just wonder what is next.

34. Sử dụng escape sequence để in bảng sau:

    Name      Age     Country   City
    Lê Công Luyến  20      Việt Nam  Hồ Chí Minh City

35. Sử dụng string formatting để hiển thị kết quả sau:

    8 + 6 = 14
    8 - 6 = 2
    8 * 6 = 48
    8 / 6 = 1.33
    8 % 6 = 2
    8 // 6 = 1
    8 ** 6 = 262144

36. Khai báo các biến `first_name`, `last_name`, `age`, `country`, `city` với thông tin của bạn.

37. Nối `first_name` và `last_name` để tạo biến `full_name`.

38. In ra câu giới thiệu bản thân bằng f-string với thông tin: họ tên, tuổi, quốc gia và thành phố.

39. Lấy 3 ký tự đầu tiên trong chuỗi `"Hồ Chí Minh City"`.

40. Đảo ngược chuỗi `"Lê Công Luyến"` bằng slicing.