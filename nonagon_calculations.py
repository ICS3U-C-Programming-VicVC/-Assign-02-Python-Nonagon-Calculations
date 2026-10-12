#!/usr/bin/env python3
# Created By: Victor V-C
# Date: 09 25, 2026
# This code will calculate the area and perimeter of a Nonagon. And display the result to the user.

import math
import constants


def main():

    side_length = float(input("Please enter a side length of the nonagon in cm: "))

    area = 9 / 4 * math.pow(side_length, 2) * constants.NONAGONCOT
    perimeter = side_length * 9

    print("The area of the Nonagon is {:.2f}cm^2".format(area))
    print("The perimeter of the Nonagon is {:.2f}.cm".format(perimeter))


if __name__ == "__main__":
    main()
