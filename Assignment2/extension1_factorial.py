"""
File: extension1_factorial.py
Name: 黃彥勳
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""


def main():
	"""
	3! = 1X2X3, 4! = 1X2X3X4
	view the number as how many times should the program calculate.
	a will be 1 in the beginning, each time calculate a will plus one.
	"""
	print('Welcome to stanCode factorial master!')
	while True:
		a = 1
		sum = 1
		num = int(input('Give me a number, and I will list the answer of the factorial: '))
		if num >= 1:
			for i in range(num):
				sum = a * sum
				a += 1
			print('Answer: ' + str(sum))
		else:
			print('- - - - - - See ya! - - - - - -')
			break
	pass


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
	main()