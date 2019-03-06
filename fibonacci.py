#!usr/bin/env python 3

'''A simple python program to calculate the Fibonacci sequence to the nth term'''
  
def fibo_func(precission): 
    ''' fibonacci sequence generator'''
    num1 = 0
    num2 = 1
    for digit in range(precission):
        yield num1
        num1, num2 = num2, num1+num2

if __name__ == '__main__':
    print(list(fibo_func(int(input('Enter a value to generater the sequence to: ')))))