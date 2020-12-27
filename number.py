# !/usr/bin/env python3

# Created by: Ahmad El-khawaldeh
# Created on: December 2020
# This program prints all numbers from 1000-2000 in a for loop


def main():
    # function prints all numbers from 1000-2000

    loop_counter = 1000

    print(" The following numbers are numbers that range from 1000-2000 : ")

    for loop_counter in range(1000, 2001):
        print(loop_counter, end=" ")
        if loop_counter % 5 == 4:
            print(" ")


if __name__ == "__main__":
    main()
