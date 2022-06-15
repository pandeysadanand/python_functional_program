"""
    @Author: SADANAND PANDEY
    @Date: 2022-05-31 15:30:00
    @Last Modified by: SADANAND PANDEY
    @Last Modified time: 2022-06-02 15:30:00
    @Title : Program to find factorial of number
"""


def fact(num):
    """
    Description:
        Function to calculate factorial

    :param num:
        take input number from user

    :return:
        factorial
    """

    factorial = 1
    while num >= 1:
        factorial = factorial * num
        num = num - 1
    return factorial


if __name__ == '__main__':
    try:
        number = int(input("Enter the number to find factorial: "))
        print(f"Factorial of {number}:", fact(number))
    except ValueError as ve:
        print("Please enter valid number\n")
