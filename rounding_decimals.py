#!/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: December 2019
# This program calculates the rounded off number to a decimal place


def rounding(number, decimal):
    # this function rounds the given number to what they choose

    # process
    rounded_number1 = number[0]*(10**decimal)
    rounded_number1 = rounded_number1 + 0.5
    rounded_number1 = int(rounded_number1)
    rounded_number1 = rounded_number1 / (10**decimal)

    return rounded_number1


def main():
    # this function gets input and checks if it has any error

    # round list
    round_number = []

    # while true loop
    while True:

        # input
        f_number = input("Enter the floated number you want to round: ")
        d_points = input("How many decimal points you want number in: ")

        # try catch
        try:
            f_number = float(f_number)
            d_points = int(d_points)
            round_number.append(f_number)
            if f_number == float(f_number) and \
               d_points == int(d_points):
                rounder = rounding(round_number, d_points)
                print("")
                print("The result is:", rounder)
                break
            else:
                break
        except Exception:
            print("Invalid input")
            print("")


if __name__ == "__main__":
    main()
