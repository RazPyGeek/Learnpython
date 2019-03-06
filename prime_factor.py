#!usr/bin/env python 3

'''A simple python program to find
   all prime factors of an inputed value'''


def has_prime(digit):
	'''A function to find all prime element with a range'''
	tups = (2,3,5,7)
	not_prime = [num for x in tups for num in range(2,digit+1) if num%x == 0 and num!=x]
	is_prime = [num for num in range(2,digit+1) if num not in not_prime]
	is_prime_factor = [prime for prime in is_prime if digit%prime== 0 ]
	if len(is_prime_factor)>=1:
		print(is_prime_factor)
	else:
		print('This number has no prime factors')
	

if __name__ == '__main__':
	'''Main python functions'''
	has_prime(int(input('Enter a value to see if it has prime factors: ')))