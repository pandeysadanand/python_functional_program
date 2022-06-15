"""
    @Author: SADANAND PANDEY
    @Date: 2022-06-02 15:30:00
    @Last Modified by: SADANAND PANDEY
    @Last Modified time: 2022-06-02 15:50:00
    @Title : Write a program for checking given number is palindrome or not

"""


def palindrome(num):
    """
        program for checking given number is palindrome or not
    :param num: number
    :return: number
    """

    num = str(input("Enter the number : "))
    reversedNum = str(num)[::-1]
    if num == reversedNum:
        print("Palindrome")
    else:
        print("Not Palindrome")

    # number = int(input("Enter the number : "))
    # reversedNum = 0
    # num = number
    # while num != 0:
    #     reminder = num % 10
    #     reversedNum = reversedNum * 10 + reminder
    #     num = num // 10
    #
    # if number == reversedNum:
    #     print(number, "is Palindrome ")
    # else:
    #     print(number, "is Not Palindrome")


if __name__ == '__main__':
    number = int(input("Enter number to check palindrome :\n"))
    palindrome(number)

