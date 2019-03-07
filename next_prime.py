#!usr/bin/env python 3

'''A simple python program to find the next
   prime number until the user chooses 
   to stop asking for the next one
'''

def next_prime():
	'''Generates the next prime number untill the user requests the program to terminate'''
	tups = (2,3,5,7)
	not_prime = [num for x in tups for num in range(2,1000) if num%x == 0 and num!=x]
	for digit in range(2,1000):
		if digit not in not_prime:
			yield digit 


if __name__ == '__main__':
	'''Main python functions'''
	prime = next_prime()
	print('\n\tThis program returns the next prime number\n\t---------------------------------------')
	print('\nEnter Yes or Y to continue\n')
	state = input('Input: ')
	try:
		while state[0].casefold() == 'Y'.casefold():
			print(next(prime)) #keeps current value in memory
			state = input('Continue: ')
	except:
		print ('Exiting program.....')