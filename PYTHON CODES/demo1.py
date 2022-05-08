import pickle
import json


# create a class with at least one data member
# the data member must contain any pre - defined text
# create an instance method to display all the data members of the class


class COne:
#construtor and instance method...stor str in var

    def __init__(self):
        self.member1 = "[COne]: Member 1"
        self.member2 = "[COne]: Member 2"

#instan mthod- print str.
    def show_members(self):
        print("Member 1:", self.member1)
        print("Member 2:", self.member2)


# Inherit the existing class to a new class
# The new class must contain TWO new data members
# The name of the FIRST data member must be same as ANY of the data member from class 1
# The name of the SECOND data member can be any thing [different from base class members]


class CTwo(COne):

    def __init__(self):
        super().__init__()      #super()- calls the COne class constructor.
        self.member1 = "[CTwo]: Member 1"
        # here the MEMBER1 will override/shadow the inherited MEMBER 1 from BASE CLASS

        self.memberNew = "[CTwo]: Member NEW"

    def show_members(self):
        print("Member 1:", self.member1)
        print("Member 2:", self.member2) #COne class var with same value.
        print("Member NEW:", self.memberNew)

    def get_csv(self):      #create a .csv file viz sep by comma. store the values...for csv file only.
        return self.member1 + ", " \
               + self.member2 + ", " \
               + self.memberNew


# creating object of first/base class
cObject = COne()
print("Printing from COne")
cObject.show_members()


# creating object of second/derived class
print("Printing from CTwo")
cObject2 = CTwo()
cObject2.show_members()


# store the entire object to a file
# Method 1: Store each data member of the object to the file
# Method 2: Store the ENTIRE OBJECT to the file [we can use PICKLE or JSON or CSV]


# The following section demonstrates the Method 1
# i.e. storing members of the object to a file

# if storing individual members in CSV format,
# then first need to get all members from object in CSV format
csvFileToWrite = open("testCSV.csv", "w")   #it will create the file w/ write()
csvFileToWrite.write(cObject2.get_csv())    #get_csv() method in class two.
csvFileToWrite.close()

# demonstrating the read of CSV values from the file
fileToFetchCSV = open("testCSV.csv", "r")
fetched_data = fileToFetchCSV.read()
fileToFetchCSV.close()

print("Fetched data [CSV]:", fetched_data)

print("====================entire obj via Pickle=========================================")
# The following section demonstrates the Method 2
# i.e. storing entire object to a file

# if using pickle to dump an object to file,
# the file must be opened with the BINARY mode ON
fileToWrite = open("testWriteUsingPickle.txt", "wb")
pickle.dump(cObject2, fileToWrite)
fileToWrite.close()

# read back the object from the file
# if reading using 'pickle' then the file must be opened using BINARY mode ON
object_fetched_from_file = CTwo()   #obj of class CTwo()
fileToRead = open("testWriteUsingPickle.txt", "rb")
object_fetched_from_file = pickle.load(fileToRead) #obj values inside file.
fileToRead.close()

print("Fetched object [using pickle]:", object_fetched_from_file)
object_fetched_from_file.show_members()


print("====================entire obj via Json=========================================")

#call the entire obj into json format.
# if the object is to dumped in JSON format then 'json.dumps' can be used to convert the object to JSON format
# the '__dict__' member of the object can be used to convert the object contents to dictionary
json_data_to_dump = json.dumps(cObject2.__dict__)


# any content in dictionary format can be dumped to a file using native methods of file management
jsonFileToWrite = open("testJSON.json", "w")
jsonFileToWrite.write(json_data_to_dump)
jsonFileToWrite.close()

# the contents of the file can be read directly
# [if in normal format e.g. if dictionary format]
fileToFetchJson = open("testJSON.json", "r")
fetched_data = fileToFetchJson.read()
fileToFetchJson.close()

print("Fetched data [JSON]:", fetched_data)
