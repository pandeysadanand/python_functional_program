def fact(number):
    """
    Here calculating factorial of given number
    :param number: range(1 ,5)
    :return: result
    """
    result = 1
    while number > 1:
        result = result * number
        number = number - 1
    return result


for i in range(1, 5):
    print("The factorial of", i, "is :", fact(i))