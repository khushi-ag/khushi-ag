import sys

#Operators ib python

a = 10
b= 3
'''
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a//b) #floor division, gives only integer quotient
print(a%b)

print(a>b)
print(a>=b)
print(a<b)
print(a<=b)
print(a==b)
print(a!=b)

#Logical operators
x = 100
y = 200

print( x and y)  #if x is False returns x otherwise it returns y              Here false means 0
print( x or y)   #if x false it returns y, otherwise returns x
print( not x)	#if x is false , it returns true, otherwise true    !0  =true

#boolean operators

x=True
y=False

print(x and y)     #T and T = T ,          T and F = F  ,  F and T = F
print(x or y)		# T or F = T  ,  F or F = F , T or T = T
print( not x)		# !F = T     , !T = F

#Membership operator

names = ["Ram" , "Rahul", "Reema", "Ramesh", "Rajan"]

print("Ram" not in names)
print("Mona"  in names)

#identity operator
x = 100
y = 200
print(id(x))
print(id(y))

x1 = x
print(id(x1))
print(x is x1)
print(x is not y)

#Command Line argument

n= len(sys.argv)
print("The number of arguments provided are: " ,n)
args = sys.argv
print("The data type of args is " , type(args))
print(args)
print("the arguments are:" )
for i in args:
	print(i)


#python3 basics.py Pooja Ram Rehan Ruhan 
#args[0] = basics.py
#args[1] = Pooja
#args[2] = Ram

#["basics.py" , "Pooja", "Ram", "Rehan", "Ruhan" ] 


looping statements : for while break continue pass 
conditional statement : if else return statement
'''

list_num = sys.argv
length = len (list_num)
for i in range(1,length):
	num = int (list_num[i])
	if num > 50:
		continue
		
	print(num)
	
	

def display (name): #formal argument
	return name
	
print(display("Hello")	) #Actal argument
