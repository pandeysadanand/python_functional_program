"""
    @Author: SNEHAL PATIL
    @Date: 2022-05-31
    @Last Modified by: SNEHAL PATIL
    @Last Modified time: 2022-06-02
    @Title : Program to Given N distinct Coupon Numbers, count how many random numbers do you
             need to generate distinct coupon number

"""

import random


def generate_coupon(coupon_count, coupon_length):
    """
           Description:
               Function to generate coupon no of unique characters

           Parameter:
               Take input coupon_count-how many coupon wants to create and
               coupon_length-how many digit coupon you want to create

           Return: none
       """

    coupon_list = []
    count = 0

    # loop will run until given number of coupon is created
    while len(coupon_list) < coupon_count:

        no = []
        # Loop will run until given length coupon is not created
        while len(no) < coupon_length:
            digit = random.randint(0, 9)
            count = count + 1

            no.append(digit)

        # To covert list coupon into string coupon
        string_ints = [str(int) for int in no]
        coupon_str = "".join(string_ints)

        # To append created coupon into list
        if len(coupon_list) == 0:
            coupon_list.append(coupon_str)
        else:
            if coupon_list.count(coupon_str) == 0:
                coupon_list.append(coupon_str)

    print("\nCoupon No List : ", coupon_list)
    print(f"\nTotal random no needed to generate coupon : {count}\n")


# Main function
if __name__ == '__main__':

    try:
        coupon_count = int(input("\nEnter how many coupon you want : "))
        coupon_length = int(input("\nEnter how many digits you want in coupon: "))

        generate_coupon(coupon_count, coupon_length)

    except ValueError:
        print("\nplease enter valid number\n")
