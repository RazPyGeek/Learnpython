#!usr/bin/env python 3
import re
"""
Have the function QuestionsMarks(str) take the str string parameter, 
which will contain single digit numbers, letters, and question marks, 
and check if there are exactly 3 question marks between every pair of two numbers that add up to 10. 
If so, then your program should return the string true, otherwise it should return the string false. 
If there aren't any two numbers that add up to 10 in the string, then your program should return false as well. 

Use the Parameter Testing feature in the box below to test your code with different arguments.
"""
#test sample("arrb6???3xxbl5???eee4nn2?nn??7ee4???nn?8", "9???1???9??1???9")
def questionMark(string):
	split_term =(r'\d+\D*\?\D*\d+' )
	match = re.findall(split_term,string)
	match = [x for x in match if x.count('?') == 3]
	new_list = ['True' for x in match if int(x[1]) + int(x[-1]) == 10 ]
	print (len(new_list) > 0)
if __name__ == '__main__':
	questionMark( str(input()))