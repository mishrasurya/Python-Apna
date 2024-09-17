# Store following word meanings in a python dictionary :
# table : “a piece of furniture”, “list of facts & figures”
# cat : “a small animal”

dict={

"table": ["a piece of furniture", "list of facts & figures"],
"cat":"a small animal",
"name":"surya",
"name":"ritu" # only one key print means in dict on 2 times same key write its overide the value of 1st one

}
print(dict)

# You are given a list of subjects for students. Assume one classroom is required for 1
# subject. How many classrooms are needed by all students.
# ”python”, “java”,“C++”,“python”, “javascript”, “java”,“python”,“java”,“C++”,“C”  

subjects={
    "python", "java", "C++" ,"python", "javascript", "java","python","java","C++","C"
}
print(subjects) # {'C', 'java', 'python', 'C++', 'javascript'} as it is a set
print("classrooms needed by all students are: ", len(subjects)) #classrooms needed by all students are:  5

# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
#an empty dictionary & add one by one. Use subject name as key & marks as value.
# 1st way
dict={ }
dict["Math"]=50
dict["Phy"]=70
dict["Chem"]=80
print(dict) # {'Math': 50, 'Phy': 70, 'Chem': 80}


#2nd way
dict={ }
x=int(input("enter marks for phy: "))
dict.update({"phy":x})
y=int(input("enter marks for chem: "))
dict.update({"chem":y})
z=int(input("enter marks for math: "))
dict.update({"math":z})

print(dict) #{'phy': 60, 'chem': 50, 'math': 40}

# Figure out a way to store 9 & 9.0 as separate values in the set. ( you can take help of built in data types)
# 1st way
set1={9,"9.0"}
print(set) #{9, '9.0'}
set2={"9",9.0}
print(set2) #{9.0, '9'}

#2nd way using tupple 
set3={
    ("float",9.0),
    ("int",9)
}
print(set3)






