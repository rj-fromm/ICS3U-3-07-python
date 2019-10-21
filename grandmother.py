#!user/bin/env python3

# Created by: RJ Fromm
# Created on: September 2019
# This program is a number guessing game


def main():

    rich = input("Are you well off? (yes or no) : ")

    goodlooking = input("Are you good looking? (yes or no) : ")

    if goodlooking == "yes" and rich == "yes":
        print("You can date my dear Gladice")

    elif goodlooking == "no" or rich == "no":
        print("you cannot date my dear Gladice")

    else:
        print("Please enter yes or no")


if __name__ == "__main__":
    main()
