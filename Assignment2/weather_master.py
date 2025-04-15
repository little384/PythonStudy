"""
File: weather_master.py
Name:
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

EXIT = -100
def main():
	"""
	the four variable should be recorded independently.
	thus I use three [if statement] to detect.\
	"""
	print('stanCode "Weather Master 4.0"!')
	big = -100
	small = 100
	cold = 0
	sum = 0
	time = 0
	while True:
		data = int(input('Next temperature: (or-100 to quit)?'))
		if data == -100:
			break
		else:
			if data > big:
				big = data
			if data < small:
				small = data
			if data < 16:
				cold +=1
			sum += data
			time +=1
	if time !=0:
		sum = sum / time
		print('Highest temperature = '+str(big))
		print('Lowest temperature = '+str(small))
		print('Average = '+str(sum))
		print(str(cold) + ' cold day(s)')
	else:
		print('No temperatures were entered.')
	pass


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
