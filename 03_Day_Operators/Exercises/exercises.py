age = 20
high = 1.76 
complex_number = 1 + 1j


print("--- 4.Calculate an area of triangle. ---")
base = float(input('Enter base: '))
height = float(input('Enter height: '))
area_of_triangle = base * height * 0.5
print('The area of the triangle is : ', area_of_triangle)


print("--- 5.Calculate the perimeter of the triangle. ---")
side_a = float(input('Enter side a: '))
side_b = float(input('Enter side b: '))
side_c = float(input('Enter side c: '))
perimeter_of_triangle = side_a + side_b + side_c
print('The perimeter of the triangle is: ',perimeter_of_triangle)


print("--- 6.Calculate its area and circumference. ---")
length = float(input('Enter length: '))
width = float(input('Enter width: '))
area = length * width
perimeter = 2 * (length + width)
print('Area is: ',area)
print('Perimeter is: ',perimeter)


print("--- 7.Calculate the area and circumference. ---")
import math
radius = float(input('Enter radius: '))
area_of_circle = math.pi * (radius ** 2)
circumference_of_circle = 2 * math.pi * radius
print('The area is: ',area_of_circle)
print('The circumference is: ',circumference_of_circle)


print("--- 8.Calculate the slope, x-intercept, y intercept. ---")
print("--- 9. Slope and Euclidean distance. ---")
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_2 = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print('The slope is: ',slope_2)
print('The Euclidean distance is: ',distance)


print("--- 10. Compare slopes. ---")
print("--- 11. Calculate y = x^2 + 6x + 9. ---")
print("--- 12. Falsy comparison ('python' & 'dragon'). ---")


print("--- 13. Check 'on' in both strings. ---")
print('on' in 'python' and 'on' in 'dragon')

print("--- 14. Check 'jargon' in sentence. ---")
sentences = 'I hope this course is not full of jargon.'
print('jargon' in sentences)


print("--- 15. Check 'on' not in both strings. ---")
print('on' not in 'dragon' and 'on' not in 'python')


print("--- 16. Convert string length (int -> float -> str). ---")
leng_str = len('PYTHON')
leng_str_to_float = float(leng_str)
leng_float_to_str = str(leng_str_to_float)


print("--- 17. Check even number. ---")
number = int(input('Enter number: '))
is_even = number % 2 == 0
print(f'Number {number} is even: {is_even}')

print("--- 18. Floor division vs int conversion. ---")
result = 7 // 3
print('Result of floor division == int(2.7) is: ', result == int(2.7))


print("--- 19. Compare types. ---")
print(type('10'))
print(type(10))
print(f"Type of '10' and 10 is: {type('10') == type(10)}")


print("--- 20. Check int('9.8') == 10. ---")
try:
    print(int(float('9.8')) == 10)
except ValueError:
    print("Cannot convert directly")


print("--- 21. Calculate weekly earning. ---")
hours = float(input('Enter hours: '))
rate_per_hours = float(input('Enter rate per hours: '))
weekly_earning = hours * rate_per_hours
print(f"Your weekly earning is : {weekly_earning}")


print("--- 22. Calculate lived seconds. ---")
numbers_of_years = int(input('Enter number of years you lived: '))
numbers_of_seconds = numbers_of_years * 365 * 24 * 60 * 60
print(f"You have lived for {numbers_of_seconds} seconds")


print("--- 23. Display table of powers. ---")
for i in range(1,6):
    print(f"{i} 1 {i} {i ** 2} {i ** 3}")
