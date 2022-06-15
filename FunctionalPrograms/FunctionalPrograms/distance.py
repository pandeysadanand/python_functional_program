"""
    @Author: SADANAND PANDEY
    @Date: 2022-06-02 10:30:00
    @Last Modified by: SADANAND PANDEY
    @Last Modified time: 2022-06-02 10:45:00

"""
import math


def calculate_distance(x, y):
    """
        Write a program Distance that takes two integer x and y and prints the Euclidean distance from the
        point (x, y) to the origin (0, 0).

    :param x: co-ordinate of X
    :param y: co-ordinate of Y
    :return: distance
    """

    # Formula to calculate euclidean distance
    Euclidean_Distance = math.sqrt((x**2) + (y**2))

    print(f"\nDistance from the origin (0 , 0) to the point {x, y}  : {Euclidean_Distance}\n")


if __name__ == '__main__':
    try:
        number1 = int(input("Enter first coordinate :"))
        number2 = int(input("Enter second coordinate: "))
        calculate_distance(number1, number2)
    except ValueError as ve:
        print("Please enter valid number")
