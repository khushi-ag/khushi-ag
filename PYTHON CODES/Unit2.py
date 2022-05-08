                                          #Unit-2

#Lambda Function: A function without a name is called "Anonymous function".
#Syntax: lambda argument_list : expression
#Example:
f = lambda x: x*x
value = f(5)
print("Square of 5 is",value)
#Note: Lambda function contain only one expression.

#Using lambdas with filter() function:
#The filter() function is useful to filter out the elements of a sequence depending on the result of a function.
#Syntax: filter(function, sequence)
#Example:

lst = [10,23,45,46,70,99]
lst1 = list(filter(lambda x: (x%2==0), lst))
print(lst1)
#output: [10, 46, 70] ...it will return the no. from list acc to lambda fun.

#Using lambda with map() function:
#The map() function is similar to filter() function but it acts on each element of the sequence and perhaps changes the elements.
#Syntax: map(function, sequence)
#Example:
lst1 = [1,2,3,4,5]
lst2 = [10,20,30,40,50]
lst3 = list(map(lambda x,y: x*y, lst1, lst2))
print(lst3)

#Using lambda with reduce() function:
#The reduce() function reduces a sequence of elements to a single value by processing the elements according to a function supplied.
#Syntax: reduce(function, sequence)
#Example:
from functools import *
lst = [1,2,3,4,5]
result = reduce(lambda x,y : x*y, lst)
print(result)
#1*2**4*5=120 so it multiply the no. from lst via lambda and print the result.

#-------------------------------------------------------------------------------------------

#Recursive Function: A function that calls itself is known as 'recursive function'.
#For more details: visit google

#-------------------------------------------------------------------------------------------

#How to create a class and how to create an object(Instance):
class Student:
    def __init__(self):
        self.name="Aayush"
        self.age=20
        self.marks=950
    def show(self):
        print("My name is ",self.name)
        print("My age is ", self.age)
        print("I got ", self.marks, "marks outof 1000")
s1 = Student()
s1.show()
                                    #OR

class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def show(self):
        print("My name is ",self.name)
        print("My age is ", self.age)
        print("I got ", self.marks, "marks outof 1000")
s1 = Student("Aayush",20,950)
s1.show()

#-------------------------------------------------------------------------------------------

#Types of Variables:
#Instance variable(Instance variable are the variables whose separate copy is created in every instance(or object).
#Example:
class Sample:
    #constructor
    def __init__(self):
        self.x=10

    def modify(self):
        self.x+=1
s1 = Sample()
s2 = Sample()

print(s1.x)
print(s2.x)
s1.modify()
print(s1.x)
print(s2.x)
#class and static variable: class variables are the variables whose single copy is available to all the instances of the class.
#Example:
class Sample:
    #this is a class variable
    x = 10
    #this is a class method
    @classmethod
    def modify(cls):
        cls.x+=1

s1 = Sample()
s2 = Sample()
print(s1.x)
print(s2.x)
s1.modify()
print(s1.x)
print(s2.x)

#-------------------------------------------------------------------------------------------

#Types Of Method:
#Instance Methods: a.Accessor Method b.Mutator Method
#Instance methods are the methods which act upon the instance variables of the class.
#Example:
class Student:
    #constructor
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    #instance method
    def show(self):
        print("My name is ",self.name)
        print("My age is ", self.age)
        print("I got ", self.marks, "marks outof 1000")
s1 = Student("Aayush",20,950)
s1.show()
#Example using Accessor method:Accessor method simply access or read data of the variables they are also called as getter method
#Example using Mutator method:Mutator method are the methods which not only read the data but also modify them they also called as setter method
class Student:
    #mutator method
    def setName(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    #accessor method
    def getName(self):
        print("My name is ",self.name)
        print("My age is ", self.age)
        print("I got ", self.marks, "marks outof 1000")
s1 = Student()
s1.setName("Aayush",20,950)
s1.getName()

#Class Method:Class methos are the methods which act on the class variables or static variables.These methods are written using @classmethod decorator.
#Example:
class Bird:
    #This is class variable
    wings = 2

    #This is class method
    @classmethod
    def fly(cls,name):
        print(name, "flies with", cls.wings, "wings")

Bird.fly('Sparrow')
Bird.fly('Pigeon')

#Static Method: When some processing is related to the class but does not need the class or its instances to perform any work.
#Example:
class Myclass:
    #This is class var or static var
    n=0
    #constructor that increments n when an instance is created
    def __init__(self):
        Myclass.n = Myclass.n+1
    #This is a static method to display the no. of instances
    @staticmethod
    def noObjects():
        print('No. of instances created:',Myclass.n)

#Create 3 instances
obj1 = Myclass()
obj2 = Myclass()
obj3 = Myclass()
Myclass.noObjects()

#-------------------------------------------------------------------------------------------

#Constructors in Inheritance: We can inherit the constructor of base class into child class using child class object.
#Example:
class Father:
    def __init__(self):
        self.property = 8000000
    def show_property(self):
        print("Total Property is",self.property)

class Son(Father):
    pass
s = Son()
s.show_property()

#Overriding Super Class Construtors and Methods:
#For more details read textbook page no.379
#Example:
class Father:
    def __init__(self):
        self.property = 8000000
    def show_property(self):
        print("Total Property is",self.property)

class Son(Father):
    def __init__(self):         #Constructor Overriding
        self.property = 8000000
    def show_property(self):    #Method Overriding
        print("Child Property is",self.property)
s = Son()
s.show_property()      #It will not print parent class method, it'll print child property method
#In this case, how to call the super class constructor so that we can access the father's property
#from the son class? For this purpose, we should call the constructor of the super class from the
#constructor of the sub class using the super() method.
#Super Method: super() is a built-in method which is useful to call the super class constructor or
              #methods from the sub class. Any constructor written in the super class is not available
              #to the sub class if the sub class has a constructor.
#Syntax: super().__init__()  call super class constructor
        #super().__init__(arguments) call super class constructor and pass arguments
        #super().method()  call super class method
#Example:
class Square:
    def __init__(self,x):
        self.x = x
    def area(self):
        print("Area of Square is",self.x*self.x)

class Rectangle(Square):
    def __init__(self,x,y):
        super().__init__(x)  #calling constructor of base class using super method
        self.y = y
    def area(self):
        super().area()      #calling method of base class using super method
        print("Area of Rectangle is",self.x * self.y)
r = Rectangle(10,12)
r.area()    #it ll print both classes area

#-------------------------------------------------------------------------------------------

#Types of Inheritance:
#1.Single Inheritance: Deriving one or more sub classes from a single base class is called single inheritance
#Example:
class Bank(object):
    cash = 1000
    @classmethod
    def available_cash(cls):
        print(cls.cash)
class AndhraBank(Bank):  #Single Inheritance
    pass
class StateBank(Bank):   #Single Inheritance
    cash = 2000
    @classmethod
    def available_cash(cls):
        print(cls.cash + Bank.cash)
a=AndhraBank()
a.available_cash()
s=StateBank()
s.available_cash()

#2.Multiple Inheritance:Deriving sub classes from multiple base classes is called multiple inheritance
#Example:
class Father:
    def height(self):
        print("Height is 6.0 foot")
class Mother:
    def color(self):
        print("Color is brown")
class Child(Father,Mother):  #Multiple Inheritance
    pass
c = Child()
c.height()
c.color()
#Problem in Multiple Inheritance :It will not showing the output of B class viz on right side (class c(A,B))
class A():
    def __init__(self):
        self.a = 'a'
        print(self.a)
class B():
    def __init__(self):
        self.b = 'b'
        print(self.b)
class C(A,B):
    def __init__(self):
        self.c = 'c'
        print(self.c)
        super().__init__()
o = C()
#Solution:
class A():
    def __init__(self):
        self.a = 'a'
        print(self.a)
        super().__init__()       #Solution
class B():
    def __init__(self):
        self.b = 'b'
        print(self.b)
class C(A,B):
    def __init__(self):
        self.c = 'c'
        print(self.c)
        super().__init__()
o = C()
#This solution is known as Method Resolution Order(MRO):
#First it will print c class data and then it will check from left side that which is the next class
#i have to check c(A,B). So, on the left side A class is there so they goto A class and print their
#data then in A class compiler check that is there any super method if yes then they go to the B class
#and print the data of B class.

#-------------------------------------------------------------------------------------------

#Polymorphism: If something exhibits various forms, it is called polymorphism.
#Abstractmethod: use @abstractmethod decorator.