"""
    @Author: SADANAND PANDEY
    @Date: 2022-06-01 19:36:00
    @Last Modified by: SADANAND PANDEY
    @Last Modified time: 2022-06-01 21:50:00

"""

def get_permutation(string, i=0):
    """
        Write static functions to return all permutation of a String using iterative method and
        Recursion method. Check if the arrays returned by two string functions are equal.

    :param string: take input string from  user
    :param i: i=0
    :return: swap string
    """

    if i == len(string):
        print("".join(string))

    for j in range(i, len(string)):
        words = [c for c in string]

        # swap
        words[i], words[j] = words[j], words[i]
        get_permutation(words, i + 1)


if __name__ == '__main__':
    inputString = str(input("Enter the string : \n"))
    get_permutation(inputString)
