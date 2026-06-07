#String Methods
challenge = 'fourth day learning PYTHON'


#capitalize() : Chuyển kí tự đầu tiên của chuỗi thành chữ cái viết hoa.
print(challenge.capitalize())

#count() : trã về số lần xuất hiện của chuỗi con trong chuỗi chính.
# Command : count(chuỗi con , index start , index finish)
print(challenge.count('y'))
print(challenge.count('y',1,30))
print(challenge.count('th'))

#endswith() : kiểm tra xem 1 chuỗi có kết thúc bằng ký tự kết thúc được chỉ định không.
print(challenge.endswith('on'))
print(challenge.endswith('tion'))

#expandtabs() : hàm này thay đổi ký tự tab = dấu cách, kích thức tab mặc định = 8.
#Command : expandtabs() : mặc định
#          expandtabs(x) : thay thế kí tự tab = x dấu cách
challenge_tabs = 'fouth\tday\tlearning\ttPYTHON'
print(challenge_tabs.expandtabs())
print(challenge_tabs.expandtabs(10))

#find() : Trã về chỉ số xuất hiện đầu tiên của một chuỗi con, ko thấy trã về -1.
print(challenge.find('y'))
print(challenge.find('th'))

#rfind() : Trã về chỉ số xuất hiện cuối cùng của một chuỗi con , ko thấy trã về -1.
print(challenge.rfind('y'))
print(challenge.rfind('th'))

#format(): định dạng chuỗi thành dạnh đầu ra dễ nhìn hơn.
first_name = 'Le Cong'
last_name = 'Luyen'
age = '20'
job = 'student'
country = 'VietNam'
print('I am {}{}. I am a {}.I am {} years old. I live in {}.'.format(first_name,last_name,job,age,country))

#index() : Trã về chỉ số thấp nhất của 1 chuỗi con.Đối số là chỉ số start và finish. Ko tìm thấy chuỗi con trã về kết quả : VALUEERROR
sub_string = 'PY'
print(challenge.index(sub_string))
print(challenge.index(sub_string,9))

#rindex() : Trã về chỉ số cao nhất của 1 chuỗi con. Đối số là chỉ số start và finish.
print(challenge.rindex(sub_string))
print(challenge.rindex(sub_string,9))

#isalnum() : Kiểm tra ký tự chữ và số.
string_letter = 'FourthDaysPython'
print(string_letter.isalnum())
string_numberletter = '30DaysPython'
print(string_numberletter.isalnum())
string = 'Fourth days python'
print(string.isalnum())
string1 = '30 Days Python'
print(string1.isalnum())

#isalpha() : Kiểm tra các ký tự trong chuỗi có phải chữ cái ko (a-zA-Z)
#isdecimal(): Kiểm tra xem tất cả các ký tự trong một chuỗi có phải là số thập phân (0-9) hay không.
#isdigit(): Kiểm tra xem tất cả các ký tự trong một chuỗi có phải là số hay không (0-9 và một số ký tự Unicode khác dùng để chỉ số).
#islower(): Kiểm tra xem tất cả các ký tự chữ cái trong chuỗi có phải là chữ thường hay không.
#isupper(): Kiểm tra xem tất cả các ký tự chữ cái trong chuỗi có phải là chữ hoa hay không.

#join() : Trã về 1 chuỗi được nối lại.
tech = ['C','Jave','Python']
result  = '# '.join(tech)
print(result)

#strip() : loại bỏ các kí tự được chỉ định trong chuỗi.
print(challenge.strip('PYTHON'))

#replace() : thay thế chuỗi con bằng 1 chuỗi đã cho.
print(challenge.replace('PYTHON','coding'))

#split() :Tách chuỗi , sử dụng chuỗi đã cho hoặc dấu cách bằng dấu phân cách.
print(challenge.split())
challenge1 = 'fourth,day,learning,python'
print(challenge1.split(', '))

#title() : Trã về chuỗi viết hoa chữ cái đầu mỗi từ
print(challenge.title())

# swapcase(): Chuyển đổi tất cả các ký tự viết hoa thành chữ thường và tất cả các ký tự viết thường thành chữ hoa.
print(challenge.swapcase())

#startswith(): Kiểm tra xem chuỗi có bắt đầu bằng chuỗi được chỉ định hay không.
print(challenge.startswith('fourth'))
print(challenge.startswith('30 Days'))
