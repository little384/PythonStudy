"""
File: quadratic_solver.py
Name:
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	print('stanCode Quadratic Solver!')
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	discriminant = b*b - 4 * a * c
	if discriminant < 0:
		print('No real roots')
	elif discriminant == 0:
		ans = -b/(2*a)
		print('One root: '+str(ans))
	else:
		n1 = (-b + math.sqrt(discriminant))/(2*a)
		n2 = (-b - math.sqrt(discriminant)) / (2 * a)
		print('Two root: '+ str(n1)+','+str(n2))
	"""
	TODO:
	"""
	pass


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
