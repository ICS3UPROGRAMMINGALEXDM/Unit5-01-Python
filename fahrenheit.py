#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 03/25/2022
# Description: Gets a temperature in celsius and converts it to farenheit

# The function that is used for the conversions
def fahrenheit():
    tc = input("Enter the degrees in celsius: ")

    try:
        tcflt = float(tc)
        tf = ((9 / 5) * tcflt) + 32
        print("{}°C is equal to {}°F".format(tcflt, tf))
    except ValueError:
        print("The inputted value must be a valid number")


def main():
    fahrenheit()


if __name__ == "__main__":
    main()
