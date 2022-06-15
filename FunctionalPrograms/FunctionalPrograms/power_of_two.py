"""
    @Author: SADANAND PANDEY
    @Date: 2022-06-02 10:36:00
    @Last Modified by: SADANAND PANDEY
    @Last Modified time: 2022-06-02 10:55:00

"""


def power_of_two(number):
    """
        This program takes a command-line argument N and prints a table of the
        powers of 2 that are less than or equal to 2^N.

    :param number: number
    :return: result
    """

    # To print 2 power in range 1 to 32 for user entered number
    try:
        result = 1    # for data types length, taking 32
        if number < 33:
            for i in range(1, number + 1):
                result = result * 2
                # print("2 ^", i, "=", result)
                print("2^{} = {}".format(i, result))

        else:
            print("Number should be less than 33")

    except Exception:
        print("This is exception")
        raise ValueError("This is value error")


if __name__ == '__main__':
    try:
        argv = int(input("Enter number to calculate power: "))
        power_of_two(argv)
    except Exception as e:
        # print("Please enter valid number")
        print(e)
