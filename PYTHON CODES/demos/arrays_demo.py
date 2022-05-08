import array
#from array import *
#from array import array

#to declare an array
#arrayname = array(type code , [elements])
#i = signed integer
#I=unsigned integer
#f = floating point
#d = double precision floating pint
#u = unicode character

#e=Employee("Ram", 34)
a = array .array ('i' , [2,4,6,8]) #0 1 2 3
b = array .array ('i' , [8,6,4,2])
'''
print(a)

for i in a:
	print(i)
	
b = array.array(a.typecode , (i*3 for i in a))
for i in b:
	print(i)
	
#Indexing and slicing
n = len(a)
for i in range(n):
	print (a[i], end = '\n')
	
for i in a[3:4]:
	print(i)

Methods of array class of array module
a.append(x), a.count(x) , a.extend(x),  a.fromfile(f,n) , a.fromlist(lst)
a.fromstring(s), a.index(x) , a.insert(x,i) , a.pop(x) , a.pop()
a.remove(x), a.reverse() , a.tofile(f), a.tolist() , a.tostring()

Variable of array class
a.typecode , a.itemsize

a.append(10)
print("After appending" , a)

a.insert(4,88)
print("After insertion", a)

n  = a.pop(2)
print("After removal ", a)

n = a.pop()
print(n , "is the iten popped from ", a)

n=a.index(88)
print("The first occurence of 88 is at position ", n)

lst = b.tolist()
print("List: " , lst)
a.extend(b)
#print(type(c))
print("Elements of a")
for i in a:
	print(i)
'''
#comparing two arrays
c = a>b
print(c)
	
#Aliasing
new_a = a
a.append(99)
print("alias of a " , new_a)

if (id(a) ==  id( new_a)):
	print("True")
else:
	print("False")
print(id(a))
print(id(new_a))

