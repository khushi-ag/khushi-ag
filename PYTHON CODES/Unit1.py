do read import csv ..file read 
                                        #UNIT-1

#Creating a boolean data type
a = 5 > 10
print(a)
a = 10 > 5
print(a)

#-------------------------------------------------------------------------------------------

#Creating a list(It can be modified)
list = [10,-20,15.5,"Aayush","Gandhi"]
print(list)
print(list[0:3])
print(list[-2])
print(list * 2)
list[1]= -40    #Modify
print(list)

#-------------------------------------------------------------------------------------------

#Creating a Tuple(It can't modified)
tpl = (10,-20,15.5,"Aayush")
print(tpl)
print(tpl[0:2])
print(tpl[-2])
print(tpl * 2)

#-------------------------------------------------------------------------------------------

#Creating a Set :(unorder collection of elements, only print unique values)
#we cannot retrieve the values using indexing and slicing in Set.

#1.set datatype (It can be modified)
s = {10,20,30,40,50,20}
print(s)
#We can also print like these
ch = set("Hello")
print(ch)
#We can use update method
s.update([60,70])
print(s)
#We can use remove method
s.remove(60)
print(s)

#2.Frozenset datatype(It can't modified)
s = {10,20,30,20,40,30}
print(s)
#We can also print lisk these.
fs = frozenset(s)
print(fs)
fs = frozenset("abcdefg")
print(fs)
#In frozenset we cannot use update and remove method because it is immutable

#-------------------------------------------------------------------------------------------

#Creating a Disctinary
dict = {1:"Mouse",2:"CPU",3:"Monitor",4:"Printer"}
print(dict)
print(dict[1])
dict[1] = "Keyboard"  #Modify
print(dict)
dict[5] = "Mouse"     #Adding new pair
print(dict)
del dict[5]           #Deleting a pair
print(dict)

#-------------------------------------------------------------------------------------------

#None means null and None represents false

#-------------------------------------------------------------------------------------------

#Assignment Operator
# =,+=,-=,/=,*=,%=,**=,//=

#-------------------------------------------------------------------------------------------

#Relational Operator: It is used for comparing two values is it same or not.
#>,>=,<,<=,==,!=

#-------------------------------------------------------------------------------------------

#Logical Operator:
# and,or,not

a=10
b=20
c=30
print(a and b)
print(a or b)
print(not a)
if(a<b and b>c): print("Yes")
else:print("No")
if(a>b or b>c): print("Yes")
else:print("No")

#-------------------------------------------------------------------------------------------

#Bitwise Operator
#~,&,|,^,<<,>>

#-------------------------------------------------------------------------------------------

#Boolean Operator
#and,or,not

a = True
b = False
print(a and a)
print(a and b)
print(a or a)
print(a or b)
print(not a)
print(not b)

#Membership Operator:
#in,not in

names = ["Mouse","Keyboard","Monitor","Printer"]
for name in names:
    print(name)

#-------------------------------------------------------------------------------------------

#Identity Operator: It will compare the memory location of two objects.
#is,is not
#The memory location of an object can be seen using id() function.

a=25
b=26
print(id(a))
print(id(b))
if(a is b):
    print("Same")
else:
    print("Different")

#== operator is used to compare two values.
x=[1,2,3,4]
y=[1,2,3,4]
if(x == y):
    print("same")
else:
    print("Different")

#-------------------------------------------------------------------------------------------

#Output Statement: Read into the TextBook

#-------------------------------------------------------------------------------------------

#Input Statement: To accept input from the keyboard we can use input() function.
#for more details: Read the Textbook
'''str = input("Enter your name:")
print("Your name is:", str)

#-------------------------------------------------------------------------------------------

#Command Line Argument:
import sys
n = len(sys.argv)
args = sys.argv
print("No. of command line args= ", n)
print("The args are: ", args)
print("The args one by one: ")
for a in args:
    print(a)'''

#Control Statements: The group of statements in python is called a suite.
#if statement
#Syntax: if condition:statements
#Example:
num=1
if num==1:
    print("One")

#if else statement
#Syntax: if condition: statements else: statement2
#Example:
num=0
if num==1:
    print("One")
else:
    print("Zero")

#if elif else statement
#Syntax: if condition: statements elif: statement2 elif: statement3 else: statement4
#Example:
num=2
if num==1:
    print("One")
elif num>=2:
    print("Zero")
else:
    print("Two")

#while loop:
#Syntax: while condition: statements
#Example:
x=1
while x<=10:
    print(x)
    x+=1
print("End")

#for loop:
#Syntax: for var in sequence: statements
#Example:
str = "Hello"
for ch in str:
    print(ch)
for i in range(1,10,2):
    print(i)

#break statement:
#Example:
x=10
while x>=1:
    print('x= ', x)
    x-=1
    if x==5:
        break
print("Out of loop")

#Continue Statement
#Example:
x=10
while x>=1:
    print('x= ', x)
    x-=1
    if x==5:
        continue
print("Out of loop")

#Pass Statement:
#Example:
x=10
while x>=1:
    print('x= ', x)
    x-=1
    if x==5:
        pass
print("Out of loop")

#return statement:
#Syntax: return expression
#Example:
def sum(a,b):
    return a+b
res = sum(5,10)
print("The result is", res)

#-------------------------------------------------------------------------------------------

#Creating an Array:
#Syntax: arrayname = array(type code, [elements])
#Example:
from array import *
a = array('i', [1,2,3,4,5])
print(a)

#Processing an Array:
#a.append(x): Add an element x at the end of the existing array a.
#a.count(x): Returns the numbers of occurences of x in the array a.
#a.insert(i,x): Inserts x in the position i in the array.
#a.pop(x): Removes the item x from the array a and returns it.
#a.pop(): Remove last item from the array a.
#a.remove(x): Removes the first occurrence of x in the array a. Raises "ValueError" if not found.
#a.reverse(): Reverses the order of elements in the array a.
#Example:
from array import *
arr = array('i',[1,2,3,4,5])
arr.append(5)
print(arr)
arr.count(4)
print(arr)
arr.insert(3,6)
print(arr)
arr.pop(6)
print(arr)
arr.pop()
print(arr)
arr.remove(3)
print(arr)
arr.reverse()
print(arr)

#Comparing Array:
#>,>=,<,<=,!=  It will return the output in true and false statement.
#Example:
from array import *
a = array('i',[0,1,2,3])
b = array('i',[0,2,2,4])
c = a==b
print(c)
c = a>b
print(c)
c = a<=b
print(c)

#Aliasing an array: Aliasing is not copying. Aliasing means giving another name to the existing object.
#b=a b is a new name of an exiting array a
from array import *
a = array('i',[1,2,3,4,5])
b = a
print("Original Array", a)
print("Aliasing Array", b)
b[0]=99
print("After Modification: ")
print("Original Array", a)
print("Aliasing Array", b)

#Slicing of an array: A slice represents a piece of the array.
#Syntax: arrayname[start:stop:stride]
#Example:
from array import *
a = array('i',[1,2,3,4,5])
b = a[0:2]
print(b)

#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------


