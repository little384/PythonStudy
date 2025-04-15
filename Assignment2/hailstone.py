"""
File: hailstone.py
Name:
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    TODO:
    """
    num1 = int(input('Enter a number: '))
    step = 0
    while num1 != 1:
        if num1 % 2 == 1:
            num2 = 3 * num2 + 1
            print(str(num1) + ' is odd, so I make it 3n+1: ' + str(num2))
        else:
            num2 = num1 / 2
            print(str(num1) + ' is even,so I take half: ' + str(num2))
        num1 = num2
        step += 1
    print('It took ' + str(step) + ' steps to reach 1.')
    pass


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
