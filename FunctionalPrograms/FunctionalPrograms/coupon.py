"""
    @Author: SADANAND PANDEY
    @Date: 2022-06-01 18:22:00
    @Last Modified by: SADANAND PANDEY
    @Last Modified time: 2022-06-01 19:22:00
    @Title : Program to Given N distinct Coupon Numbers, count how many random numbers do you
            need to generate distinct coupon number

"""

import random


def generate_coupon(new_coupon_no, sample_coupon_list, coupon_count):
    """
        Function to generate coupon no of unique characters
    :param new_coupon_no: input from user as total number of coupon
    :param sample_coupon_list: list of coupon available
    :param coupon_count: total number of random function executed
    :return:
    """
    random_count = 0

    # Creating coupon of user limit
    while len(new_coupon_no) < coupon_count:
        digit = random.randint(0, len(sample_coupon_list) - 1)
        random_count = random_count + 1

        # If list is empty then adding first character
        if len(new_coupon_no) == 0:
            new_coupon_no.append(sample_coupon_list[digit])

        # If list not empty then add character after checking if it is present or not 
        else:
            if new_coupon_no.count(sample_coupon_list[digit]) == 0:
                new_coupon_no.append(sample_coupon_list[digit])
    return new_coupon_no, random_count


# Main function
if __name__ == '__main__':
    coupon_samples = "abcdefghijelmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345689!@#$%^&*()_+?|\/*<>"

    # To convert string into list
    sample_coupon = list(coupon_samples)

    # To store coupon
    coupon_no = [] # 5: a, b, c, d, 1

    try:
        # Taking input from user
        total_coupon = int(input("Enter total number of coupon : "))
        # To store return list and random count
        new_coupon, count = generate_coupon(coupon_no, sample_coupon, total_coupon)
    except ValueError as ve:
        print("Please enter valid number")

    # to convert list coupon into string
    coupon = ''
    for i in new_coupon:
        coupon += i  # todo  # use join() and avoid for loop Also string manipulation

    # Print coupon
    print("Coupon No: ", coupon)
    print("Total random no needed to generate coupon :", count)
