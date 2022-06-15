"""
    @Author: SADANANDPANDEY
    @Date: 2022-05-33 14:36:00
    @Last Modified by: SADANAND PANDEY
    @Last Modified timE: 2022-06-02 10:02:00

"""

import random


def flip_coin(num):
    """
    :description:    Program to Flip Coin and print percentage of Heads and Tails
    :param num: total number of coin flip
    :return: head_percentage
    """

    try:
        head_count = 0
        tail_count = 0
        # Flipping coin as per user input
        for x in range(1, num + 1):

            # Taking random number between 0 and 1
            coin_flip = (random.randint(0, 1))

            if coin_flip == 1:
                head_count = head_count + 1
            else:
                tail_count = tail_count + 1

        # Calculating head and tail count percentage i
        return (head_count / num) * 100
    except ZeroDivisionError as zde:
        print("Can not divide by zero")


if __name__ == '__main__':
    try:
        number = int(input("\nEnter how many times you want to flip coin : "))
        head_percentage = flip_coin(number)

        print("\nHead Percentage : {}%".format(head_percentage))
        print("\nTail Percentage : {}%".format(100-head_percentage))
    except ValueError as ve:
        print("Please enter valid number")
    except TypeError as te:
        print("This is types error")
