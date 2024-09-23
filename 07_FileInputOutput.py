#Read file
# f=open("file_name","mode")
f=open("demo.txt","r") # here demo file is in same folder as current FileInputOutput file
data=f.read() # data are stored in the form of string
print(data) #surya Mishra is a good boy.
print(type(data))
# f.close() # good practise of a programmer to close file once no use 

f1=open("demo.txt","r")
data=f1.read(5) # read only 5 char from file
print(data) #surya

print("###############")
f2=open("demo.txt","r")
line1=f2.readline()
print(line1) #print line1 data

line2=f2.readline()
print(line2)

Write file
f3=open("demo.txt","w")
f3.write("\nsurya is also good") # write mode overrides existing file data

# In append mode data is added with existing data means does not overide existing data
f4=open("demo.txt","a")
f4.write("\n I will move to next line")

# If you want to create a file that does not exist then also you can do with below syntax
f5=open("sample.txt","w") # first checked exist or not and as not exist so created new one
f5.write(" Nice to meet you")

# 
f6=open("sample1.txt","a") # first checked exist or not and as not exist so created new one
f6.write(" Nice to meet you")
print(f6.read()) # print(f6.read()) io.UnsupportedOperation: not readable

If you write to the file in "r+" mode, the content will overwrite existing data from the current cursor 
position.You won't lose the entire content unless you write beyond what's already there.
f7=open("sample1.txt","r+") #  both reading and writing operations can be performed using this mode.
f7.write("abc") 
before r+ content was "Nice to meet you" so after r+ first letter "Nic" is replaced with "abc"
f8=open("sample1.txt","r+") #  both reading and writing operations can be performed using this mode.
f8.write("abc") 
print(f8.read()) # It just read mean whatever value exist in sample1.txt print here

f9=open("sample1.txt","w+") # all data is truncated from sample1.txt and in next step you dont write then f9.read will show blank data
f9.write("hello")

f10=open("sample1.txt","a+") #You can both read and append to the file
f10.write("hello")
print(f10.read()) # print(f9.read()) io.UnsupportedOperation: not readable


# Using with syntax f.close() not mandatory as its automatically close the file

with open("sample2.txt","r") as f:
    data=f.read()
    print(data) # let already in file we have "surya mishra" then it will print "surya mishra"

with open("sample2.txt","w") as f:
    f.write("new data") # remove all existing data and inserted "new data" in sample2.txt file

 # If an module is not preinstalled then to install you have to write pip install tensorflow or pip3 install tensorflow

# deleting a file using preinstalled module
import os        
os.remove("simple2.txt")


# Create a new file “practice.txt” using python. Add the following data in it:
# Hi everyone
# we are learning File I/O   
# using Java
# I like programming in Java

with open("practice1.txt","w") as f:
    f.write(" Hi everyone\n we are learning File I/O\n using Java\n I like programming in Java ")


#WAF that replace all occurrences of “java” with “python” in above file.
with open("practice1.txt","r") as f:
    data=f.read()
    print(data)

new_data=data.replace("Java","Python")
print(new_data)  # It just diplay but not overide in file in real

with open("practice1.txt","w") as f:
    f.write(new_data)   # it overrides in file and replaced java with python

# Search if the word “learning” exists in the file or not.

with open("practice1.txt","r") as f:
    data=f.read()
    print(data)
new_data=data.find("learning")
if(new_data!=-1):
    print("found and index is: ", new_data)    
else:
    print("not found")


# WAF to find in which line of the file does the word “learning”occur first.
#Print -1 if word not found.

def line_check():
    word="programming123"
    data=True
    line_no=1
    with open("practice1.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no +=1
    return -1
print(line_check())            


#From a file containing numbers separated by comma, print the count of even numbers.















