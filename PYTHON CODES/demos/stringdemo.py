'''
#Initializing a string

s1 = "Welcome to the demo program"
print(s1)

s2  = 'welcome to the "Core  demo" program' 
print(s2)

s3 = "Welocme to the \t Core Demo program"
print(s3)


#to find the length of  a string
n = len(s1)
print("The length of the string S1 is ", n)


#Indexing in strings
print("Indexing the elements of the string")
for i in range ( n-1,-1,-1):
	print( s1[i], end  =' ')

# output: m a r g o r p   o m e d   e h t   o t   e m o c l e W


#Slicing the string stringname [ start:  stop :  stepsize ] 
name = "RamKumar Bhadauria"
print("Slice 1 = " ,  name [ 0 : 9 : 1])   

print("Slice 2 = " ,name[::2])

print("Slice 3 = " , name[-4:-1:])

print("Slice 4 = ", name[-1:-4:-1])


#Repeating the string
name = "RamKumar Bhadauria"
print(name*2)

#Concatenating the string

s4 = s1+name
print(s4)


#checking the membership

if name in s4:
	print(name , "exsist in ", s4)


#comparing two strings
name2 = "Rajkumar Bhadauria"
if name2 < name:
	print(name2 ,"is less than ", name)

else:
	print("Nothing can be said")

	
#Removing spaces from a string
name3 = "    Suresh"
if name3 =="Suresh":
	print("String Equal")
else:
	print("String not equal")


if name3.lstrip() == "Suresh":
	print("String Equal")
else:
	print("String not equal")


#Finding sub string  mainstring.find(substring, beinging, ending)
str_main= input("Enter main string ")
sub = input("Enter string to find")
n=str_main.find(sub,0,len(str_main))
if n== -1:
	print("string not found")
else :
	print("Substring found")

#Counting the substring
n = str_main.count(sub,0,len(str_main))
print("Occurences of substring ", sub , " in ", str_main, "is" , n)


#Replacing a string with another string
statement = "This is first lecture on strings."
s1 = "first"
s2 = "second"
new_state = statement.replace(s1,s2)

print(new_state)


#This is second lecture on strings

#Splitting and joining the strings
words = statement.split(" ")
print("The words fetched are ",words)


sep = ":"
join_str = sep.join(words)
print(join_str)


#Changing the case of string
print(statement.upper())
print(statement.lower())
print(statement.swapcase())
print(statement.title())


#Checking the starting and Ending of a String
print(statement.startswith('This'))

print(statement.endswith('strings.'))

#String Testing methods
password = "RamKumar123"

print(password.isalnum())
print(password.isalpha())
print(password.isdigit())
print(password.islower())
print(password.isupper())
print(password.istitle())
print(password.isspace())  #returns true if the string contains only spaces

'''

#Working with characters
greet = "Hello Ram"
print(greet[0])
print(greet[6:7]) #6th letter - R an 7 end no.= so r is on 7th no. from 1 
ch = greet[2]   #ch =l
print(ch.isalpha())


#Sorting Strings
names = ["Ram" , "Rahul", "Reema", "Ramesh", "Rajan"]

sort_names = sorted(names)
print(sort_names)


#Q.1  Write a program in python to display all positions of a sub string in a given main string
#Q.2 Write a program in python to find length of a string without using the len() function.
