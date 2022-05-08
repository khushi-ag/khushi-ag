'''
1. Write a python script that will create a library books issue system. There are only 10 copies of each book. Ram wants to issue 5 books, check for the feasibility and availability of those 5 books.

2. display unique names starting with 'M' from a csv file in python

STEPS: 
1. read the csv file
2. collect and get all the data from the file.
3. separte the line from the data.
4. check the name starting w/ 'M' in each row.(other than col name) 
5. store all names in a proper data structure.
6. sep unique name and store in another data structure.
7. print the unique names.

3. store all names from file/list into another list categorsied alphabetically.
A : [all name start w/ 'A' are like- Aa, Ab, Ac....Az]...



Q1: display unique names starting with 'M' from a csv file in python

STEPS: 
1. read the csv file
2. collect and get all the data from the file.
3. separte the line from the data.
4. check the name starting w/ 'M' in each row.(other than col name) 
5. store all names in a proper data structure.
6. sep unique name and store in another data structure.
7. print the unique names.

Q2: store all names from file/list into another list categorsied alphabetically.
A : [all name start w/ 'A' are like- Aa, Ab, Ac....Az]...

'''
import csv 
'''
#r = read; w = write
with open("students.csv",'r') as csv_file:
	csv_reader = csv.reader(csv_file) #...= csv.DictReader(csv_file) -convert it into dict & no headerline. 

	#next(csv_reader) #this will remove 1st line or header in our csv file

	with open("new_names.csv",'w') as new_file:
		csv_writer = csv.writer(new_file, delimiter= '\t')

#if this for stmt are not under with open(/...write) then it will cause ValueError: i/o oper are closed...
		for line in csv_reader:
			print(line) #print(line[2]) ...print the 2nd line.
			csv_writer.writerow(line) #write in the write file


#WITH DICTREADER
with open("students.csv",'r') as csv_file:
	csv_reader = csv.DictReader(csv_file) 

	with open("new_names.csv",'w') as new_file:
		fieldnames= ['first_name','last_name','date_of_birth'] #give all the field name for the columns
#if we dont want other fieldname then do *

		csv_writer = csv.DictWriter(new_file, fieldnames= fieldnames, delimiter= '\t')

		csv_writer.writeheader()

		for line in csv_reader:
			#del the col name by: * del line['email',other...]
			csv_writer.writerow(line) 

#GET THE NAMES STARTING W/ 'A' LETTER
test_list = ['Akash', 'Nikhil', 'Manjeet', 'akshat']
check = 'A'
print("The original list : " + str(test_list))

#res = [idx for idx in test_list if idx[0].lower() == check.lower()]
#res = [idx for idx in test_list if idx.lower().startswith(check.lower())] ...store in list

for i in test_list:
	if i.startswith('A') or i.startswith('a'):
		print("The list of matching first letter : " + i)

# print result print("The list of matching first letter : " + str(res))
'''

#swapping without another value.
a=10 
b=20
print("a: ",a," b: ",b)  #a: 10 b: 20
a,b = b,a 
print("a: ",a," b: ",b)  #a: 20 b: 10
