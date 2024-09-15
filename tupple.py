#tupple
tup=(1,2,4,"hello",'d')
print(tup)  #(1, 2, 4, 'hello', 'd')
print(type(tup)) #<class 'tuple'>
tup=(1)
print(type(tup)) #<class 'int'>
tup=(1,) # comma is mandatory if only one element
print(type(tup)) #<class 'tuple'>
tup=(1,2,) # If multiple element then comma is optional
print(type(tup)) #<class 'tuple'>
#Print value at index
print(tup[1]) #2
#slicing in tupple
tup=[1,4,5,4]
print(tup[0:1]) #[1]
# find element index at 1st occurence
print(tup.index(4)) #1
# count an element ocuurence
print(tup.count(4)) #2

# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
list=[ ]
first=input("enter first movie: ")
second=input("enter second movie: ")
third=input("enter third movie: ")
list=[first,second,third]
print(list)





