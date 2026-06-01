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
