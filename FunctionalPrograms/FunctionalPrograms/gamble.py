"""
    @Author: SADANAND PANDEY
    @Date: 2022-06-01 21:55:00
    @Last Modified by: SADANAND PANDEY
    @Last Modified time: 2022-06-01 21:55:00
    @Title :
"""

import random


def start_gamble(stake, goal):
    """
        Simulates a gambler who start with $stake and place fair $1 bets until
             he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
             times he/she wins and the number of bets he/she makes.
    :param stake: Take input as player stack
    :param goal: winning goal
    :return: none
    """

    win_count = 0
    loss_count = 0
    total_gambles = 0

    while not (stake == 0 or goal == stake):
        gamble_random = random.randint(0, 1)
        total_gambles += 1

        if gamble_random == 0:
            win_count += 1
            stake += 1
        else:
            loss_count += 1
            stake -= 1

    print(f"\nStake : {stake} \n Goal : {goal}")
    if stake == goal:
        print("\nYou won !!")
    else:
        print("\nYou lost !!")

    print(f"\nYou won {win_count} times\nYou lost {loss_count} times")

    win_percentage = round(float(win_count / total_gambles) * 100, 2)
    print(f"\nWin Percentage : {win_percentage} %")

    loss_percentage = 100 - win_percentage
    print(f"\nLoss Percentage : {loss_percentage} %")


if __name__ == '__main__':
    print("\nWelcome to Gambler Program !!")
    try:
        play = True
        while play:
            stake = int(input("Enter your stake :"))
            while stake < 1:
                print("\nPlease enter an stack amount greater than 0 ")
                stake = int(input("Enter your stake :"))

            goal = int(input("Enter your goal :"))
            if goal < stake:
                print("Your goal should greater than your stake !")
                goal = int(input("Enter your goal :"))

            # Calling start gamble function
            start_gamble(stake, goal)

            # Taking choice of player whether he wants to continue or not
            choice = int(input("\nIf you want play again  \nPress 1 for continue  \nPress 2 for Exit \n"))
            if choice == 1:
                play = True
            else:
                print("Thank you for playing !! ☺")
                play = False
    except ValueError as ve:
        print("Please enter valid input")
