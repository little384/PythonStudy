"""
File: extension2_number_checker.py
Name:
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""

EXIT = -1
def main():
    print('Welcome to the number checker!')
    while True:
        num = int(input('n: '))
        time = num-1
        x = 1
        ans = 0
        if num == -1:
            break
        else:
            for i in range(time):
                if num%x == 0:
                    ans += x
                x +=1
        if ans < num:
            print(str(num) +' is a deficient number.')
        elif ans > num:
            print(str(num) + ' is an abundant number.')
        else:
            print(str(num) + ' is a perfect number.')
    print('Have a good one!')

    """
    TODO:
    """
    pass


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
