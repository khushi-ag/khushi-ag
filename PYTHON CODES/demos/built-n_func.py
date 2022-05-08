import string
from functools import *
from random import randint, choice

'''
#anonymous function

lambda:1  #garbage collected

true = lambda:1 #assigned to a variable
print(true())

add1 = lambda x,y : x+y  #as equivalent to def add(x,y):return x+y 

def add(x,y):
	return x+y 

print(add1(3,4))

add2 = lambda x ,y=2 : x+y  #lambda also takes default arguments
print(add2(3))

add3 = lambda *z : z		#lambda also takes variable arguments
print(add3('abc','xyz'))


#filter() built in function



#map() built in function

def add(n, inc = 2): return n+inc

def test_map():
	num = []
	for i in range(10):
		num.append(randint(1,101))
	print (num)
	print("the mapped list of numbers is")	
	o = list(map(lambda n : n + 2 , num))   #map(function,sequence)
	#o= map(add,num)
	print (len(o), o)

print(test_map())

'''

print(reduce((filter(lambda x : x >100,num),num) 

#reduce() built in function

def sum(x,y):return x+y

nums = range(5)
total  = 0
for i in nums:
	total = sum(total,i)

print(total)

#using reduce()
print ('the total is:', reduce ((lambda x,y: x*y), range(5)))

'''
#((0+1)+2)+3)+4) => 10

0+1
1+2
3+3
6+4
10
'''
