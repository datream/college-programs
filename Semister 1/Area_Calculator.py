import math


# To calculate area

def area_circle():
    radius = input("Enter the value of radius: ")
    if radius.isalpha():
        #For string Input
        print("Error, wrong input")
        area_circle()
    else:
        print("The area is", format(math.pi * (float(radius) ** 2), '.2f'))


def area_triangle():
    base = input("Enter the value of base: ")
    height = input("Enter the value of height: ")
    if base.isalpha() == True or height.isalpha() == True:
        #For string Input
        print("Error, wrong input")
        area_triangle()
    else:
        print("The area is", format(0.5 * abs(float(base)) * abs(float(height)), '.2f'))


def area_rectangle():
    base = input("Enter the value of base: ")
    height = input("Enter the value of height: ")
    if base.isalpha() == True or height.isalpha() == True:
        #For string Input
        print("Error, wrong input")
        area_triangle()
    else:
        print("The area is", format(abs(float(base)) * abs(float(height)), '.2f'))


def switch(case):
    if case == 'circle':
        area_circle()
    elif case == 'triangle':
        area_triangle()
    elif case == 'rectangle':
        area_rectangle()
    else:
        switch((input("Error, re-enter input: ")).lower())


switch((input("Would you like to find the area of a circle, a triangle or a rectangle? ")).lower())
