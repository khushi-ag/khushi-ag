'''
import pickle
import json

class One:
	def __init__(self):
		self.a= "Hello"

	def disp(self):
		print("in class One: ",self.a)


class Two(One):
	def __init__(self):
		super().__init__()
		self.b= "_world"

	def disp(self):
		print("in class Two: ",self.a," ", self.b)



o1= One()
o2= Two()
o2.disp() #in class Two:  Hello   _world
o1.disp() #in class One:  Hello


#pickle- for call the entire obj in a file
#pickle.dump(arg1, arg2)- it contain 2 parameter: arg1- obj; arg2- fileToWrite. NO VAR TO STORE.

file = open("ab.txt","wb")
pickle.dump(o2, file)
file.close()

#pickle.laod(arg1)- it contain 1 argu1- fileToRead. HAS VAR TO STORE
filer = open("ab.txt","rb")
show= pickle.load(filer)
filer.close()

print("pickle file: ", filer) #pickle file:  <_io.BufferedReader name='ab.txt'>. it display filename as well as BufferWriter for Write
print("pickle file: ", show) #pickle file:  <__main__.Two object at 0x00000233AEFDFDF0>
print("pickle file: ", file) #pickle file:  <_io.BufferedWriter name='ab.txt'>. it display filename as well as BufferReader for Read

#json- for call the entire obj in a file
jsonIntoDump= json.dumps(o1.__dict__)

jFile = open("JsonWrite.json","w")
jFile.write(jsonIntoDump)
jFile.close()

JRead = open("JsonWrite.json","r")
data= JRead.read()
JRead.close()

print("Json file: ",data) #Json file:  {"a": "Hello"}
print("Json file: ",JRead) #Json file:  <_io.TextIOWrapper name='JsonWrite.json' mode='r' encoding='cp1252'>
# print("Json file: ",JFile) #error JFile is not defined.




import csv
import json

datafile = open("C:/Users/Khushi Agarwal/Desktop/MCA/PYTHON/Paper-20211228 -Py A/matches.csv","r") 
data = csv.reader(datafile)

# print(data) #obj display
c = 0
for r in data:
	# print(r)
	
	if r[11] == max(r[11]):
		print("Team 1: ",r[4]," ,Team 2: ", r[5])
		c= c+1

print(c) #408 out of 622 



jsondata = open("C:/Users/Khushi Agarwal/Desktop/MCA/PYTHON/Paper-20211228 -Py A/startups.json","r")
# readdata = json.load(jsondata) #print it all in one line
readdata = jsondata.read() #in proper json format.

print("JSON DATA: ",readdata)
print(readdata["State"]) #error
'''

'''
mid term- II qustion: 
Create a Python program which can perform the following functionalities:
1. Create a class called Person having 
a. following instance properties.
i. first name 
ii. middle name
II. last name
iv. date of birth

b. Create appropriate constructor
c. Create a method which can display all the instance members of the class 
d. Override the 'str' method which can display all the instance members of the class as a dictionary


2. Create an Student class, inherited from Person, and consisting of
a. following instance properties
i. unique enrolment number
ii. course name [course the student has enrolled] 
iii. date of joining the course

b. Create appropriate constructor
c. Create a method which can display all the instance members of the class 
d. Override the 'str' method which can display all the instance members of the
class as a dictionary


3. In the main method
a. Create a list consisting 5 different student objects.
b. The data of the student details should be input from console
C Once all the details are ready, store all the details in a file. 
d. The data should be stored in CSV format [details of one object per line] 
e. Every time an object is saved to file, the record number saved should be displayed on console

e.g.
Saved STUDENT 1 to fiel 
Saved STUDENT 2 to file
.....
Saved STUDENT 5 to file

Solution: 


class Person:
	def __init__(self):
		self.first = "qw"
		self.mid= "er"
		self.last= "lsatnam"
		self.dob= 125487

	def display(self):
		print("first: ",self.first)
		print("mid: ",self.mid)
		print("last: ",self.last)
		print("dob: ",self.dob)



class Student(Person):
	def __init__(self):
		self.enroll = 12121212
		self.course = "Mca"
		self.doj= 2021-02-02

	def display(self):
		print("enroll: ",self.enroll)
		print("course: ",self.course)
		print("doj: ",self.doj)

p1= Person()
s1= Student()
s2= Student()
s3= Student()
s4= Student()
s5= Student()

list = [s1,s2,s3,s4,s5]

enroll = input("enter enroll: ")
course = input("enter course: ")
doj = input("enter date of joining: ")


for i in list:
	file = open("abc.csv","w")
	file.write(enroll," ,", course," , ",doj)

file.close()

filr = open("abc.txt","r")
f= filr.read()
filr.close()