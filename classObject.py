# class and object creation
class Student:
    name="surya"

obj1= Student()
print(obj1.name) #surya

obj2=Student()
print(obj2.name) # surya
# Note: object is also called instance of class

print("*****************")

class Student:
    name="Ritu"
    def __init__(self):
        print(self.name)
        print("surya")

obj1=Student()
print(obj1.name) # obj1 and self both are same
0/p: 
Ritu
surya
Ritu

========================================
# data/variables are also called attributes example here name is attribute
Note: Here self.name means object name 
class Student:
   # name="Ritu"
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks #here marks in right side is parameter and left side marks is object marks attribute
        print("constructor call")
       
obj1=Student("surya",50)
print(obj1.name,obj1.marks) # obj1 and self both are same

obj2=Student("mishra",70)
print(obj2.name,obj2.marks) # obj1 and self both are same

O/P:
constructor call
surya 50
constructor call
mishra 70

===================================

class Student:
    # If object and class attribute have same name then precedence of object attribute is higher than 
    # class attribute means object attribute value will be printed
    college_name="CGU" # That is common for all objects we make them class attribute
    name="annonymns"
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks #here left side marks is instance attribute and for every object its different
        print("constructor call")
 # To access object atrributes we use object.attribute and to access class attributes we use class.attribute      
obj1=Student("surya",50)
print(obj1.name,obj1.marks) #  surya 50
print(obj1.college_name) #CGU
print(Student.college_name) # CGU
print(obj1.name) #surya
print(Student.name) #annonymns

obj2=Student("mishra",70)
print(obj2.name,obj2.marks) # obj2 and self both are same
print(obj2.college_name)

O/P:
constructor call
surya 50
CGU
CGU
surya
annonymns
constructor call
mishra 70
CGU

============================================================

class Student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def welcome(self):
        print("welcome student, ",self.name) #welcome student,  Karan

    def get_marks(self):
        return self.marks

s1= Student("Karan",50)
s1.welcome()   
print(s1.get_marks()) # 50

O/P:
welcome student,  Karan
50


================================================

# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.

class Student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print(marks,name)

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Name is: ",self.name," and average marks is: ",sum/3)     

s1=Student("surya",[20,30,40])
s1.get_avg()

s1.name="Ritu"
s1.get_avg()


o/p:
[20, 30, 40] surya
Name is:  surya  and average marks is:  30.0
suryamishra@suryas-MBP-2 Python-Apna % python3 Practise.py
[20, 30, 40] surya
Name is:  surya  and average marks is:  30.0
Name is:  Ritu  and average marks is:  30.0

====================================================

# Method execution using Static , here no need to write self






