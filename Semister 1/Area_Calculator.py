import math


# To calculate area of circles, rectangles and triangles

def input_check(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if value < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            break
    return value


def area_circle():
    radius = input_check("Enter the value of radius: ")
    print("The area is", format((math.pi * radius ** 2), '.2f'))


def area_triangle():
    base = input_check("Enter the value of base: ")
    height = input_check("Enter the value of height: ")
    print("The area is", (format(0.5 * base * height), '.2f'))


def area_rectangle():
    base = input_check("Enter the value of base: ")
    height = input_check("Enter the value of height: ")
    print("The area is", (format(base * height), '.2f'))


def switch(case):
    if case == 'circle':
        area_circle()
    elif case == 'triangle':
        area_triangle()
    elif case == 'rectangle':
        area_rectangle()


data = (input("Would you like to find the area of a circle, a triangle or a rectangle? ")).lower()
while data not in ('circle', 'triangle', 'rectangle'):
    data = (input("Error, re-enter input: ")).lower()
switch(data)
