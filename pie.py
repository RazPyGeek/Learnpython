#!/usr/bin/env python3

#-------Imports------------
from decimal import Decimal, getcontext
#--------------------------

''' A Program To Find Pi
	To the Nth Term Using
	BBP Formula
	link:https://math.stackexchange.com/questions/948312/bailey-borwein-plouffe-formula'''

def calc_pi(place): #Function to generater value of pi to nth position
    getcontext().prec = (place+1)
    total = 0
    for num in range(place):
        total += Decimal(1)/(16**num)*(Decimal(4)/(8*num+1) - 
                 Decimal(2)/(8*num+4) - Decimal(1)/(8*num+5) -
                 Decimal(1)/(8*num+6))
    print(total)

#--------Main Method-----------------
if __name__ == '__main__':
    print('\t\t______________________________________________')
    print('\t\t\tWelcome To Pie Pie calculate')
    print('\t\t______________________________________________\n')
    calc_pi(int(input('Enter the number of decimals places to calculate to: \n')))