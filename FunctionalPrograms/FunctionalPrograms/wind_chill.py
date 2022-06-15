"""
    @Author: SADANAND PANDEY
    @Date: 2022-06-01 00:22:00
    @Last Modified by: SADANAND PANDEY
    @Last Modified time: 2022-06-01 00:30:00
    @Title : Write a program wind_chill.py that takes two input from user as t
            and v and prints the wind chill
"""


def wind(speed, temp):
    """
        Write a program wind_chill.py that takes two double command-line arguments t
        and v and prints the wind chill

    :param speed: take input velocity from user
    :param temp: take input temperature from user
    :return: wind
    """
    try:
        if 3 <= speed <= 120 and temp < 50:
            wind = 35.74 + 0.6215 * temp + (0.4275 * temp - 35.75) * pow(speed, 0.16)
            print("\nChilly Wind \n", wind)
        else:
            print("\nVelocity should be in range 3 - 120 mile/hr \nTemperature should be less than 50 F\n")
    except TypeError:
        print("Please don not interrupt")


if __name__ == '__main__':
    try:
        velocity = int(input("Enter velocity: "))
        temp = int(input("Enter temperature: "))
        wind(velocity, temp)
    except ValueError:
        print("Please enter valid input")
    except Exception:
        print("This is error")