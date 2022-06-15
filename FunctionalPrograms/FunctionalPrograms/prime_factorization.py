"""
    @Author: SADANAND PANDEY
    @Date: 2022-06-01 19:36:00
    @Last Modified by: SADANAND PANDEY
    @Last Modified time: 2022-06-01 19:50:00
"""


def prime_factor(num):
    """
        Python Program to find Prime Factors of a Number
    :param num: number
    :return: i
    """
    # Finding prime factors of number
    for i in range(2, num+1):
        while num % i == 0:
            num = num / i
            print(i)


if __name__ == '__main__':
    number = int(input("Enter number to find factor: "))
    prime_factor(number)

