'''

def add(a,b): # positional arguments
	return(a+b)

c = add(4,3)
print("c is ", c)

def add(item=1,price = 40): #Default Arguments
	return(item * price)

print(add())
print(add(2))
print(add(3,60))
print(add(price = 80))  #keyword

#reference of the function can be assigned to a variable
sub = add
print(sub())
print("id of func add() ",id(add))
print("id of func sub() ", id (sub))

a  = 1
b = a
c = b
print(id (a))
print(id (b))
print(id (c))

a = 2
b = a
c = b
print(id (a))
print(id (b))
print(id (c))


#function can be passed as an argument
def calc(add):
	c = add(3,4)
	return(c)

print(calc(add))


#variable length arguments
def varargs(a,b=5,*c):
	print ("a =" ,a)
	print('b= ' , b)
	print(type(c))
	print(c[0])
	
	for i in c:
		print (i)

print(varargs(2,4,4,4,5))


#keyword variable arguments(Dictionary)

def dictargs (a, b="helo", **c):
	print ("a =" ,a)
	print('b= ' , b)
	print(type(c))
	for i in c.keys():
		print (i , str(c[i]))

print(dictargs(3,4, e= 'zoo' , men = ('Rahul' , 'Ravi')))




#keyword and non keyword arguments
def mix (a,b = "Hi", *c, **d):		# ** = dict; * = tuple
	print ("a =" ,a)
	print('b= ' , b)
	print(type(c))
	print(type(d))
	for i in c:
		print (i)
	for i in d.keys():
		print (i , d[i])

print(mix(2,"hello", 'projects' , name = "Pooja", age = 23))

'''

#5 = 1*2*3*4*5 = 120

#5!

def fact (n):
	if n==0:
		factorial = 1
	else:
		factorial = n*(fact(n-1))
	return factorial
	
ans  = fact(5)
print(ans)
		
fact(5) = 5==0 , else factorial  = 5(fact(4))  = 5*24
fact (4) = 4 == 0 , else factorial  = 4(fact(3)) = 4*6
fact (3) = 3 == 0 , else factorial = 3 *(fact(2)) = 3*2
fact(2)  = 2== 0 , else factorial = 2*(fact(1)) = 2*1
fact(1) = 1 == 0, else fcatorial = 1*(fact(0)) = 1*1
fact(0) = 0 == 0 factorial  = 1

1*2*3*4*5 = 120

5(fact(4)

