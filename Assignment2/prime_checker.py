"""
File: prime_checker.py
Name:
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

# This constant controls when to stop
EXIT = -1
def main():
	print('Welcome to the prime checker')
	while True:
		num = int(input('n: '))
		check = 0
		a = 1
		if num == -1:
			break
		else:
			for i in range(num):
				if num % a == 0:
					check+=1
				a +=1
			if check ==2:
				print(str(num)+ ' is a prime number.')
			else:
				print(str(num)+ ' is not a prime number.')
	print('Have a good one!')


	"""
	TODO:
	"""

	pass


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
