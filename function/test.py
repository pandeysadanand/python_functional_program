# -----------------------------------------------------------------
# ============================Parameters===========================
# -----------------------------------------------------------------

# Printing Hello message on console------------------

# def wish():
#     print("Hello good morning ☺")
# wish()


# : Write a function to take name of the student as input and print wish message by
# name---------------------------------------------------

# def wish(name):
#     print("Hello", name, "Good Morning ☺")
# wish("Pandey")
# wish("Ravi")


# ------------------------------------------------------------------------
# ============================Return Statements===========================
# ------------------------------------------------------------------------


# Write a function to accept 2 numbers as input and return sum-----

# def add(number1, number2):
#     return number1 + number2
#
#
# result = add(10, 20)
# print("The sum is :", result)
# print("The sum is :", add(100, 200))


# If we are not writing return statement then default return value is None---------

# def message():
#     print("Hello")
#
#
# message()
# print(message())


# Write a function to find factorial of given number-------------------------

# def fact(number):
#     """
#     Here calculating factorial of given number
#     :param number:
#     :return: factorial
#     """
#     result = 1
#     while number > 1:
#         result = result * number
#         number = number - 1
#     return result
#     # for i in range(1, 5):
#     #    print("The factorial of", i, "is :", fact(i))
# print(fact(5))


# ------------------------------------------------------------------------------
# --------------Returning multiple values from a function:-----------------------
# -------------------------------------------------------------------------------

# Example- 1:

# def sum_sub(number1, number2):
#     sum = number1 + number2
#     sub = number1 - number2
#     return sum, sub
#
#
# result1, result2 = sum_sub(100, 60)
# print("The sum is:", result1)
# print("The subtract is:", result2)


# def display(**kwargs):
#     for k, v in kwargs.items():
#         print(k, "=", v)
#
#
# display(n1=10, n2=20, n3=30)
# display(rno=100, name="Durga", marks=70, subject="Java")

#
# d = {100: 'durga', 200: 'ravi', 300: 'shiva'}
# print(type(d))
# print(d)
# print(d[400])
# # for x, y in d:
# #     print(x, y)

# from sys import argv
# args = argv[1:]
# for num in args:
#     power = int(num)**2
#     print(power)

