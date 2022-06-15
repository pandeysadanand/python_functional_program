"""
    @Author: SADANAND PANDEY
    @Date: 2022-6-02 08:22:00
    @Last Modified by: SADANAND PANDEY
    @Last Modified time: 2022-06-02 08:40:00
    @Title : Write a program Quadratic.java to find the roots of the equation a*x*x + b*x + c.
            Since the equation is x*x, hence there are 2 roots.
"""
import math


def quadratic_equation(a, b, c):
    """
        Write a program to find the roots of the equation a*x*x + b*x + c.
        Since the equation is x*x, hence there are 2 roots.
    :param a: coefficient of a
    :param b: coefficient of b
    :param c: coefficient of c
    :return: root1,  root2
    """
    try:
        discriminant = b * b - 4 * a * c

        # checking condition for roots
        if discriminant > 0:
            print("real and distinct roots ")
            print((-b + discriminant) / (2 * a))
            print((-b - discriminant) / (2 * a))
            # return (-b + discriminant) / (2 * a), (-b - discriminant) / (2 * a)
        elif discriminant == 0:
            print("real and same roots")
            print(-b / (2 * a))
            # return -b / (2 * a)
        else:
            print("Complex Roots")
            real_part = - b / (2 * a)
            print("{} + ({})j".format(real_part, discriminant))
            print("{} - ({})j".format(real_part, discriminant))
            # return real_part, discriminant

    except ArithmeticError as ar:
        print("Please enter valid number")
    except Exception as e:
        print("This is exception")

if __name__ == '__main__':
    try:
        argv1 = int(input("Enter the value of a : "))
        argv2 = int(input("Enter the value of b : "))
        argv3 = int(input("Enter the value of c : "))
        quadratic_equation(argv1, argv2, argv3)

    except ValueError as ve:
        print("Please enter a valid number")
