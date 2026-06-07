# 30 Days Of Python - Day 04: Strings

> Bản ghi chú tiếng Việt để ôn lại kiến thức **Day 04 - Strings**.  
> Nội dung được viết lại dựa trên phần lý thuyết `04_strings.md` trong repo **30-Days-Of-Python** của Asabeneh Yetayeh.

---

## Mục tiêu bài học

Sau bài này, bạn cần nắm được:

- String là gì trong Python.
- Cách tạo chuỗi bằng dấu nháy đơn, nháy kép và ba dấu nháy.
- Cách nối chuỗi.
- Cách dùng escape sequence như `\n`, `\t`, `\\`.
- Cách format chuỗi bằng `%`, `.format()` và f-string.
- Cách truy cập ký tự trong chuỗi bằng index.
- Cách cắt chuỗi bằng slicing.
- Một số method quan trọng của string.

---

## 1. String là gì?

Trong Python, **string** là kiểu dữ liệu dùng để lưu văn bản.

Bất kỳ dữ liệu nào được đặt trong:

- dấu nháy đơn `'...'`
- dấu nháy kép `"..."`
- ba dấu nháy đơn `'''...'''`
- ba dấu nháy kép `"""..."""`

đều được xem là **chuỗi**.

Ví dụ:

```python
name = 'Python'
message = "Hello, World!"
```

Có thể kiểm tra độ dài chuỗi bằng hàm `len()`:

```python
greeting = 'Hello, World!'
print(len(greeting))  # 13
```

> Ghi nhớ: `len()` đếm số ký tự trong chuỗi, bao gồm cả dấu cách, dấu phẩy, dấu chấm, ký tự đặc biệt.

---

## 2. Tạo chuỗi trong Python

### 2.1 Chuỗi một dòng

```python
letter = 'P'
print(letter)       # P
print(len(letter))  # 1

sentence = "I am learning Python"
print(sentence)
```

Chuỗi có thể chỉ gồm **1 ký tự** hoặc gồm **nhiều ký tự**.

---

### 2.2 Chuỗi nhiều dòng

Nếu muốn viết chuỗi trên nhiều dòng, dùng ba dấu nháy đơn hoặc ba dấu nháy kép.

```python
multiline_string = '''I am learning Python.
Python is easy to read.
I will practice every day.'''

print(multiline_string)
```

Hoặc:

```python
multiline_string = """I am learning Python.
Python is easy to read.
I will practice every day."""

print(multiline_string)
```

Dạng này thường dùng khi cần lưu đoạn văn bản dài.

---

## 3. Nối chuỗi - String Concatenation

**Concatenation** nghĩa là nối nhiều chuỗi lại với nhau.

Trong Python, dùng toán tử `+` để nối chuỗi.

```python
first_name = 'Nguyen'
last_name = 'Giang'
space = ' '

full_name = first_name + space + last_name
print(full_name)  # Nguyen Giang
```

Có thể kiểm tra độ dài từng chuỗi:

```python
print(len(first_name))
print(len(last_name))
print(len(full_name))
```

> Lưu ý: Nếu nối chuỗi với số nguyên hoặc số thực, cần chuyển số sang chuỗi bằng `str()`.

Sai:

```python
age = 20
print('I am ' + age)  # lỗi
```

Đúng:

```python
age = 20
print('I am ' + str(age))
```

---

## 4. Escape Sequences trong chuỗi

Escape sequence là các ký tự đặc biệt bắt đầu bằng dấu `\`.

Một số escape sequence thường dùng:

| Ký tự | Ý nghĩa |
|---|---|
| `\n` | Xuống dòng mới |
| `\t` | Tab, tạo khoảng cách ngang |
| `\\` | In ra dấu gạch chéo ngược `\` |
| `\'` | In ra dấu nháy đơn `'` |
| `\"` | In ra dấu nháy kép `"` |

Ví dụ:

```python
print('Hello\nPython')
```

Kết quả:

```text
Hello
Python
```

Ví dụ dùng tab:

```python
print('Name\tAge\tCountry')
print('Giang\t20\tViet Nam')
```

Ví dụ in dấu `\`:

```python
print('This is a backslash: \\')
```

Ví dụ in dấu nháy kép:

```python
print('Python starts with \"Hello, World!\"')
```

---

## 5. String Formatting - Định dạng chuỗi

String formatting dùng để chèn biến vào trong chuỗi một cách gọn hơn.

Python có nhiều cách format chuỗi:

1. Old style `%`
2. `.format()`
3. f-string

---

### 5.1 Old Style Formatting - dùng `%`

Một số ký hiệu thường dùng:

| Ký hiệu | Ý nghĩa |
|---|---|
| `%s` | Chuỗi hoặc dữ liệu có thể chuyển thành chuỗi |
| `%d` | Số nguyên |
| `%f` | Số thực |
| `%.2f` | Số thực lấy 2 chữ số sau dấu chấm |

Ví dụ:

```python
first_name = 'Nguyen'
last_name = 'Giang'
language = 'Python'

text = 'I am %s %s. I learn %s.' % (first_name, last_name, language)
print(text)
```

Ví dụ với số:

```python
radius = 10
pi = 3.14
area = pi * radius ** 2

result = 'The area is %.2f' % area
print(result)  # The area is 314.00
```

---

### 5.2 New Style Formatting - dùng `.format()`

Cách này dùng `{}` làm vị trí để đưa dữ liệu vào.

```python
first_name = 'Nguyen'
last_name = 'Giang'
language = 'Python'

text = 'I am {} {}. I learn {}.'.format(first_name, last_name, language)
print(text)
```

Ví dụ tính toán:

```python
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
```

Kết quả:

```text
4 + 3 = 7
4 - 3 = 1
4 * 3 = 12
4 / 3 = 1.33
```

---

### 5.3 f-string - Python 3.6+

Đây là cách nên dùng nhiều nhất vì dễ đọc và ngắn gọn.

Cú pháp:

```python
f'Text {variable}'
```

Ví dụ:

```python
first_name = 'Nguyen'
age = 20

print(f'My name is {first_name}. I am {age} years old.')
```

Ví dụ với phép tính:

```python
a = 4
b = 3

print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
```

> Ghi nhớ: `:.2f` nghĩa là lấy 2 chữ số sau dấu chấm thập phân.

---

## 6. String là một chuỗi các ký tự

Trong Python, string có thể được xem như một dãy ký tự.

Ví dụ:

```python
language = 'Python'
```

Chuỗi trên gồm các ký tự:

```text
P y t h o n
```

Mỗi ký tự có một vị trí gọi là **index**.

---

## 7. Unpacking Characters - Tách ký tự

Nếu số biến bằng đúng số ký tự trong chuỗi, ta có thể tách từng ký tự ra biến riêng.

```python
language = 'Python'
a, b, c, d, e, f = language

print(a)  # P
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f)  # n
```

> Lưu ý: Nếu số biến không bằng số ký tự, Python sẽ báo lỗi.

---

## 8. Truy cập ký tự bằng index

Trong lập trình, vị trí bắt đầu từ `0`.

```python
language = 'Python'
```

| Ký tự | P | y | t | h | o | n |
|---|---|---|---|---|---|---|
| Index dương | 0 | 1 | 2 | 3 | 4 | 5 |
| Index âm | -6 | -5 | -4 | -3 | -2 | -1 |

Ví dụ:

```python
language = 'Python'

print(language[0])   # P
print(language[1])   # y
print(language[5])   # n
print(language[-1])  # n
print(language[-2])  # o
```

Muốn lấy ký tự cuối bằng index dương:

```python
last_index = len(language) - 1
print(language[last_index])
```

> Ghi nhớ: index cuối cùng luôn bằng `len(chuoi) - 1`.

---

## 9. Slicing - Cắt chuỗi

Slicing dùng để lấy một phần của chuỗi.

Cú pháp:

```python
string[start:end]
```

Trong đó:

- `start`: vị trí bắt đầu.
- `end`: vị trí kết thúc nhưng **không lấy ký tự tại end**.

Ví dụ:

```python
language = 'Python'

print(language[0:3])  # Pyt
print(language[3:6])  # hon
```

Giải thích:

```python
language[0:3]
```

lấy ký tự ở index `0`, `1`, `2`, nhưng không lấy index `3`.

---

### 9.1 Bỏ start hoặc end

```python
language = 'Python'

print(language[:3])   # Pyt
print(language[3:])   # hon
print(language[-3:])  # hon
```

Ý nghĩa:

- `[:3]`: lấy từ đầu đến trước index 3.
- `[3:]`: lấy từ index 3 đến hết.
- `[-3:]`: lấy 3 ký tự cuối.

---

### 9.2 Đảo ngược chuỗi

Dùng slicing với bước nhảy `-1`:

```python
greeting = 'Hello, World!'
print(greeting[::-1])
```

Kết quả:

```text
!dlroW ,olleH
```

---

### 9.3 Bỏ qua ký tự khi slicing

Cú pháp đầy đủ:

```python
string[start:end:step]
```

Ví dụ:

```python
language = 'Python'
print(language[0:6:2])  # Pto
```

Giải thích:

- Bắt đầu từ index `0`.
- Đi đến trước index `6`.
- Mỗi lần nhảy `2` bước.

Chuỗi `Python` sẽ lấy: `P`, `t`, `o`.

---

## 10. Các method quan trọng của string

String method là các hàm có sẵn dùng để xử lý chuỗi.

Cú pháp chung:

```python
string.method()
```

Ví dụ:

```python
text = 'python'
print(text.upper())
```

---

### 10.1 `capitalize()`

Viết hoa chữ cái đầu tiên của chuỗi.

```python
challenge = 'thirty days of python'
print(challenge.capitalize())
```

Kết quả:

```text
Thirty days of python
```

---

### 10.2 `title()`

Viết hoa chữ cái đầu của từng từ.

```python
challenge = 'thirty days of python'
print(challenge.title())
```

Kết quả:

```text
Thirty Days Of Python
```

---

### 10.3 `upper()`

Chuyển toàn bộ chữ cái thành chữ hoa.

```python
challenge = 'thirty days of python'
print(challenge.upper())
```

Kết quả:

```text
THIRTY DAYS OF PYTHON
```

---

### 10.4 `lower()`

Chuyển toàn bộ chữ cái thành chữ thường.

```python
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.lower())
```

Kết quả:

```text
thirty days of python
```

---

### 10.5 `swapcase()`

Đổi chữ hoa thành chữ thường và chữ thường thành chữ hoa.

```python
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())
```

Kết quả:

```text
tHIRTY dAYS oF pYTHON
```

---

### 10.6 `count()`

Đếm số lần xuất hiện của một chuỗi con.

```python
challenge = 'thirty days of python'

print(challenge.count('y'))   # 3
print(challenge.count('th'))  # 2
```

Có thể giới hạn vùng tìm kiếm:

```python
print(challenge.count('y', 7, 14))
```

---

### 10.7 `find()`

Tìm vị trí xuất hiện đầu tiên của chuỗi con.

Nếu không tìm thấy, trả về `-1`.

```python
challenge = 'thirty days of python'

print(challenge.find('y'))   # 5
print(challenge.find('th'))  # 0
print(challenge.find('z'))   # -1
```

---

### 10.8 `rfind()`

Tìm vị trí xuất hiện cuối cùng của chuỗi con.

```python
challenge = 'thirty days of python'

print(challenge.rfind('y'))   # 16
print(challenge.rfind('th'))  # 17
```

---

### 10.9 `index()`

Giống `find()`, nhưng nếu không tìm thấy sẽ báo lỗi.

```python
challenge = 'thirty days of python'

print(challenge.index('da'))  # 7
```

Nếu tìm chuỗi không tồn tại:

```python
print(challenge.index('java'))  # ValueError
```

> Phân biệt nhanh:  
> `find()` không thấy thì trả về `-1`.  
> `index()` không thấy thì báo lỗi.

---

### 10.10 `rindex()`

Giống `rfind()`, nhưng nếu không tìm thấy sẽ báo lỗi.

```python
challenge = 'thirty days of python'
print(challenge.rindex('on'))
```

---

### 10.11 `startswith()`

Kiểm tra chuỗi có bắt đầu bằng một chuỗi con nào đó không.

```python
challenge = 'thirty days of python'

print(challenge.startswith('thirty'))  # True
print(challenge.startswith('30'))      # False
```

---

### 10.12 `endswith()`

Kiểm tra chuỗi có kết thúc bằng một chuỗi con nào đó không.

```python
challenge = 'thirty days of python'

print(challenge.endswith('python'))  # True
print(challenge.endswith('tion'))    # False
```

---

### 10.13 `replace()`

Thay thế chuỗi con bằng chuỗi khác.

```python
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'))
```

Kết quả:

```text
thirty days of coding
```

---

### 10.14 `split()`

Tách chuỗi thành list.

Mặc định, `split()` tách theo dấu cách.

```python
challenge = 'thirty days of python'
print(challenge.split())
```

Kết quả:

```python
['thirty', 'days', 'of', 'python']
```

Tách theo dấu phẩy:

```python
text = 'Facebook, Google, Microsoft, Apple'
print(text.split(', '))
```

Kết quả:

```python
['Facebook', 'Google', 'Microsoft', 'Apple']
```

---

### 10.15 `join()`

Nối các phần tử trong list thành một chuỗi.

```python
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']

result = ' '.join(web_tech)
print(result)
```

Kết quả:

```text
HTML CSS JavaScript React
```

Ví dụ khác:

```python
result = '# '.join(web_tech)
print(result)
```

Kết quả:

```text
HTML# CSS# JavaScript# React
```

---

### 10.16 `strip()`

Xóa ký tự thừa ở đầu và cuối chuỗi.

Thường dùng để xóa khoảng trắng.

```python
text = '   Coding For All   '
print(text.strip())
```

Kết quả:

```text
Coding For All
```

Có thể truyền ký tự muốn xóa:

```python
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth'))
```

> Lưu ý: `strip()` chỉ xóa ở đầu và cuối chuỗi, không xóa phần giữa.

---

### 10.17 `expandtabs()`

Thay ký tự tab `\t` bằng khoảng trắng.

```python
challenge = 'thirty\tdays\tof\tpython'

print(challenge.expandtabs())
print(challenge.expandtabs(10))
```

---

## 11. Các method kiểm tra chuỗi

Các method này thường trả về `True` hoặc `False`.

---

### 11.1 `isalnum()`

Kiểm tra chuỗi có phải chỉ gồm chữ và số không.

```python
print('ThirtyDaysPython'.isalnum())      # True
print('30DaysPython'.isalnum())          # True
print('thirty days of python'.isalnum()) # False vì có dấu cách
```

---

### 11.2 `isalpha()`

Kiểm tra chuỗi có phải chỉ gồm chữ cái không.

```python
print('ThirtyDaysPython'.isalpha())      # True
print('thirty days of python'.isalpha()) # False vì có dấu cách
print('123'.isalpha())                   # False
```

---

### 11.3 `isdecimal()`

Kiểm tra chuỗi có phải số thập phân từ `0-9` không.

```python
print('123'.isdecimal())   # True
print('12 3'.isdecimal())  # False
print('10.5'.isdecimal())  # False
```

---

### 11.4 `isdigit()`

Kiểm tra chuỗi có phải chữ số không.

```python
print('30'.isdigit())  # True
print('Thirty'.isdigit())  # False
```

Một số ký tự Unicode dạng số cũng có thể trả về `True`.

```python
print('\u00B2'.isdigit())  # True
```

---

### 11.5 `isnumeric()`

Kiểm tra chuỗi có phải dạng số hoặc ký tự liên quan đến số không.

```python
print('10'.isnumeric())      # True
print('\u00BD'.isnumeric())  # True, ký tự ½
print('10.5'.isnumeric())    # False
```

---

### 11.6 `isidentifier()`

Kiểm tra chuỗi có thể dùng làm tên biến hợp lệ không.

```python
print('30DaysOfPython'.isidentifier())       # False vì bắt đầu bằng số
print('thirty_days_of_python'.isidentifier()) # True
```

Tên biến hợp lệ thường:

- Không bắt đầu bằng số.
- Không có dấu cách.
- Có thể dùng chữ, số, dấu gạch dưới `_`.

---

### 11.7 `islower()`

Kiểm tra các chữ cái trong chuỗi có phải chữ thường không.

```python
print('thirty days of python'.islower()) # True
print('Thirty days of python'.islower()) # False
```

---

### 11.8 `isupper()`

Kiểm tra các chữ cái trong chuỗi có phải chữ hoa không.

```python
print('THIRTY DAYS OF PYTHON'.isupper()) # True
print('thirty days of python'.isupper()) # False
```

---

## 12. Bảng tổng hợp method cần nhớ

| Method | Công dụng ngắn gọn |
|---|---|
| `capitalize()` | Viết hoa chữ cái đầu chuỗi |
| `title()` | Viết hoa chữ cái đầu mỗi từ |
| `upper()` | Chuyển thành chữ hoa |
| `lower()` | Chuyển thành chữ thường |
| `swapcase()` | Đổi hoa thành thường, thường thành hoa |
| `count()` | Đếm số lần xuất hiện |
| `find()` | Tìm vị trí đầu tiên, không thấy trả `-1` |
| `rfind()` | Tìm vị trí cuối cùng, không thấy trả `-1` |
| `index()` | Tìm vị trí đầu tiên, không thấy báo lỗi |
| `rindex()` | Tìm vị trí cuối cùng, không thấy báo lỗi |
| `startswith()` | Kiểm tra chuỗi bắt đầu bằng gì |
| `endswith()` | Kiểm tra chuỗi kết thúc bằng gì |
| `replace()` | Thay thế chuỗi con |
| `split()` | Tách chuỗi thành list |
| `join()` | Nối list thành chuỗi |
| `strip()` | Xóa ký tự/khoảng trắng ở hai đầu |
| `isalnum()` | Kiểm tra chữ + số |
| `isalpha()` | Kiểm tra toàn chữ cái |
| `isdecimal()` | Kiểm tra số thập phân 0-9 |
| `isdigit()` | Kiểm tra chữ số |
| `isnumeric()` | Kiểm tra dạng số |
| `isidentifier()` | Kiểm tra có phải tên biến hợp lệ |
| `islower()` | Kiểm tra chữ thường |
| `isupper()` | Kiểm tra chữ hoa |

---

## 13. Ghi nhớ nhanh khi làm bài tập Day 04

### Công thức nối chuỗi

```python
result = string1 + ' ' + string2
```

### Công thức lấy độ dài

```python
len(string)
```

### Công thức lấy ký tự đầu

```python
string[0]
```

### Công thức lấy ký tự cuối

```python
string[-1]
```

hoặc:

```python
string[len(string) - 1]
```

### Công thức cắt chuỗi

```python
string[start:end]
```

### Công thức đảo chuỗi

```python
string[::-1]
```

### Công thức format nên dùng

```python
name = 'Giang'
age = 20
print(f'My name is {name}. I am {age} years old.')
```

---

## 14. Ví dụ tổng hợp

```python
company = 'Coding For All'

print(company)                 # Coding For All
print(len(company))            # 14
print(company.upper())         # CODING FOR ALL
print(company.lower())         # coding for all
print(company.capitalize())    # Coding for all
print(company.title())         # Coding For All
print(company.swapcase())      # cODING fOR aLL

print(company[0])              # C
print(company[-1])             # l
print(company[0:6])            # Coding

print(company.find('Coding'))  # 0
print(company.replace('Coding', 'Python'))
print(company.split())         # ['Coding', 'For', 'All']

print(company.startswith('Coding')) # True
print(company.endswith('coding'))   # False
```

---

## 15. Lỗi thường gặp

### Lỗi 1: Quên dấu cách khi nối chuỗi

```python
first = 'Coding'
second = 'For'
third = 'All'

print(first + second + third)  # CodingForAll
```

Đúng:

```python
print(first + ' ' + second + ' ' + third)  # Coding For All
```

---

### Lỗi 2: Nhầm `find()` và `index()`

```python
text = 'Python'

print(text.find('Java'))   # -1
print(text.index('Java'))  # lỗi ValueError
```

Nếu chưa chắc chuỗi có tồn tại hay không, nên dùng `find()` trước.

---

### Lỗi 3: Nhầm slicing lấy cả vị trí end

```python
text = 'Python'
print(text[0:3])  # Pyt
```

`0:3` chỉ lấy index `0`, `1`, `2`, không lấy index `3`.

---

### Lỗi 4: Nối chuỗi với số mà không ép kiểu

Sai:

```python
age = 20
print('Age: ' + age)
```

Đúng:

```python
age = 20
print('Age: ' + str(age))
```

Hoặc dùng f-string:

```python
age = 20
print(f'Age: {age}')
```

---

## 16. Mini practice tự ôn

Bạn có thể tự thử các câu sau:

```python
text = 'Coding For All'
```

1. In ra độ dài của `text`.
2. Chuyển `text` thành chữ hoa.
3. Chuyển `text` thành chữ thường.
4. Lấy ký tự đầu tiên.
5. Lấy ký tự cuối cùng.
6. Cắt lấy chữ `Coding`.
7. Kiểm tra `text` có bắt đầu bằng `Coding` không.
8. Kiểm tra `text` có kết thúc bằng `All` không.
9. Thay `Coding` thành `Python`.
10. Tách chuỗi thành list bằng `split()`.

Gợi ý lời giải:

```python
text = 'Coding For All'

print(len(text))
print(text.upper())
print(text.lower())
print(text[0])
print(text[-1])
print(text[0:6])
print(text.startswith('Coding'))
print(text.endswith('All'))
print(text.replace('Coding', 'Python'))
print(text.split())
```

---

## Kết luận

Ở Day 04, phần quan trọng nhất là hiểu rằng string trong Python là một dãy ký tự có thứ tự. Vì vậy, bạn có thể:

- Lấy từng ký tự bằng index.
- Cắt chuỗi bằng slicing.
- Đảo chuỗi bằng `[::-1]`.
- Format chuỗi bằng f-string.
- Xử lý chuỗi bằng các method như `upper()`, `lower()`, `replace()`, `split()`, `join()`, `find()`.

Nếu quên bài này, chỉ cần ôn lại 4 phần chính:

1. Tạo chuỗi.
2. Index và slicing.
3. Format chuỗi.
4. String methods.

---

## Nguồn tham khảo

- Asabeneh Yetayeh, **30-Days-Of-Python - Day 04: Strings**, repo GitHub `Asabeneh/30-Days-Of-Python`.
