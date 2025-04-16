"""
File: extension4_narcissistic_checker.py
Name:
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""

EXIT = -1
def main():
    """
    透過除以十找出輸入值得位數，再將每一位數分開，分別乘以該次方，加總後確認是否為水仙花數
    """
    c = 0
    print('Welcome to the Narcissistic number checker!')
    while True:
        digit = 0 #位數
        num = int(input('n: ')) #輸入值
        check1 = check2 = num 
        if num == -1:  #是否結束整個程式
            break
        while check1 !=0:         
            check1 = check1 // 10
            digit +=1
        for i in range(digit):
            a = check2 % 10
            b = 1
            for i in range(amount):
                if a !=0:
                    b = b*a
            c += b
            check2 = check2//10
        if c == num:
            print(str(num) +' is a narcissistic number')
        else:
            print(str(num) +' is not a narcissistic number')
        c = 0
    print('Have a good one!')
    pass


if __name__ == '__main__':
    main()
