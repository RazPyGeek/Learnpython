#!usr/bin/env python3

'''A simple implementation of 
   Collatz Conjecture
'''

def Collatz(N):
	is_even = lambda x: x%2 == 0
	check = lambda x: x is 0 or x is 1
	sequence = []
	if check(N) == True:
		print(N)
	else:
		sequence.append(N)
		while N != 1:
			if is_even(N) == True:
				N = int(N/2)
				sequence.append(N)
			else:
				N = (N*3) + 1
				sequence.append(N)
		print(sequence)

if __name__ == '__main__':
	Collatz(int(input('Digit: ')))

