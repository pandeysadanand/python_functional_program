"""
    @Author: SADANAND PANDEY
    @Date: 2022-06-01 20:36:00
    @Last Modified by: SADANAND PANDEY
    @Last Modified time: 2022-06-01 20:50:00
"""


def prime_number(initial, final):
    """
        Finding prime number between give range
    :param initial: number1
    :param final: number2
    :return: prime_number
    """

    print("Prime numbers between", initial, "and", final, "are:")

    for num in range(initial, final + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)


if __name__ == '__main__':
    lower_limit = int(input("Enter th lower limit of range : "))
    upper_limit = int(input("Enter the upper limit of range : "))
    prime_number(lower_limit, upper_limit)