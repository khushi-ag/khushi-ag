'''
A generator is a special type of function which does not return a single value, instead, it returns an iterator object with 
a sequence of values. In a generator function, a YIELD statement is used rather than a return statement.
'''
def gen (x,y):
	while x <= y :	#6<=10; 11%2=1
		if (x%2==0):
			yield x 	#yield is like a return stmt in fun.
		x  +=1


g = gen(6,10)
print (type(g))	#<class 'generator'>

print("Elements of generator element by element")
print(next(g))
print(next(g))
print(next(g))
print(next(g))	#error..bcuz no element left to print.
'''

for i in g:
	print (i)
	
'''
