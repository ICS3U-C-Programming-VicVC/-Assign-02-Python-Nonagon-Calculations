#!/usr/bin/env python3
# Created By: Victor V-C
# Date: 10 12, 2026
# This code will calculate the area and perimeter of a Nonagon. And display the result to the user.

import math
import constants


def main():

    # Get a side length  from the user in cm.
    side_length = float(input("Please enter a side length of the nonagon in cm: "))

    # using the side length  from above, calculate the area and perimeter of the nonagon.
    area = 9 / 4 * math.pow(side_length, 2) * constants.NONAGONCOT
    perimeter = side_length * 9

    # Display back to the user both the area and perimeter rounded to 2 decimal places.
    print("The area of the Nonagon is {:.2f}cm^2".format(area))
    print("The perimeter of the Nonagon is {:.2f}.cm".format(perimeter))


if __name__ == "__main__":
    main()
