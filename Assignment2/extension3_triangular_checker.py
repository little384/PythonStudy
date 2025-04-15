"""
File: extension3_triangular_checker.py
Name:
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""

EXIT = -1
def main():
    """
    To do:
    """
    print('Welcome to the triangular number checker!')
    while True:
        a = 0
        ans = 0
        num = int(input('n: '))
        if num == -1:
            break
        for i in range(num):
            a +=1
            check = a*(a+1)/2
            if num == check :
               ans = 1
        if ans == 1:
            print(str(num)+' is a triangular number.')
        else:
            print(str(num)+' is not a triangular number.')
    print('Have a good one!')

    pass


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
