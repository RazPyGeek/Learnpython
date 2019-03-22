#!usr/bin/ env python 3
'''A simple program to convert Binary numbers
   To Decimals and Vice Versa
   '''
from os import name,system
from time import sleep

def clear():
	""" A simple functiom to clear the screen """
	if name == 'nt':
		system('cls')
	else:
		system('clear')

def dec_to_binary(num):
	'''Converts the input to binary digits'''
	result,new_list,val,mod = '', [], 0, 0
	while val!=1:
		mod, val = num%2, int(num/2)
		num = val
		new_list.append(mod)
	new_list.append(1)
	new_list.reverse()
	result = ''.join(str(val) for val in new_list)
	print(result)

def binary_to_dec(num):
	'''Converts the input to binary digits'''
	num = str(num)
	expo,iters,result = len(num)-1, 0, 0
	while iters!= len(num):
		result+=int(num[iters])*pow(2,expo)
		iters,expo = iters+1,expo-1
	print(result)

if __name__ == '__main__':
	print('Select an option\n1) Decimal to binary\n2) Binary to decimal')
	option = int(input('Input: '))
	choice = True
	if option == 1:
		print('\n\n----------------Decimal to Binary----------------\nEnter 0 to quit app \n')
		while choice:
		    state = int(input('Digit:'))
		    if state == 0:
		        choice = False
		    else:
		    	dec_to_binary(state)
		    
	else:
		print('\n\n----------------Binary to Decimal----------------\nEnter 0 to quit app \n')
		while choice:
		    state = int(input('Digit:'))
		    if state == 0:
		        choice = False
		    else:
		    	binary_to_dec(state)
		    
	print('Quiting...')
	sleep(1)
	clear()