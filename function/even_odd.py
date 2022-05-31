def even_odd(number):
    """
    Write a function to check whether the given number is even or odd?------------
    :param number: number
    :return: none
    """
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")


even_odd(int(input("Enter number1 :")))
even_odd(156)
