def calculate(num1=1, num2=5):
    """
    Doing arithmetic operation
    :param num1: number1
    :param num2: number2
    :return: sum ,sub, mul, div
    """
    print(num1)
    print(num2)
    sum = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    return sum, sub, mul, div


result1, result2, result3, result4 = calculate(num2 = 100,num1= 500)
print("The sum is:", result1)
print("The subtract is:", result2)
print("The multiplication is:", result3)
print("The division is :", result4)




