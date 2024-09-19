
#function definition
def sum(a,b): # here a and b are parameters
    sum=a+b
    print(sum) #30
sum(10,20)  # function call, here 10,20 are arguments

print("********************")

def sum(a,b):
    return a+b
sum=sum(10,30) 
print(sum)   #40

def hello():
    print("hello")   # hello
hello()  
output=hello()  
print(output) # prints "None" because hello() functon does not return anything 

# Avg marks
def avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    return avg
avg=avg(10,20,30)   
print(avg) #20.0

# Inside function we can also use loop, if etc

# I want 2 stement at same line to print even they are in 2 different line
print("surya",end=" ")
print("mishra") #surya mishra

# default parameter
#case 1
def mul(a=1,b=4):
    print(a*b) #4
mul()    

#case 2
def mul(a,b=4):
    print(a*b) #8
mul(2)

#case 3
# def mul(a=1,b):
#     print(a*b) # SyntaxError: non-default argument follows default argument
# mul(3)


# WAF to print the length of a list. ( list is the parameter)

list1=[1,5,6,9,10]
list2=[6,9,10,23,19,7]

def length(list):
    print("length of list is: ", len(list))
length(list1)  
length(list2)  

# WAF to print the elements of a list in a single line. ( list is the parameter)
   
list=["surya","mishra","ritu","mishra"]
def singleLine(el):
    for item in el:
        print(item,end=" ") # surya mishra ritu mishra 

singleLine(list)
print()

#WAF to find the factorial of n. (n is the parameter)
def factorial(n):
    fact=1
    for I in range(1,n+1):
        fact=fact*I
    print(fact)  
factorial(5)      


#WAF to convert USD to INR.

def converter(usd):
    inr=80*usd
    print(usd,"usd=", inr,"Inr")
converter(4)    

print("******* Without Recursion*************")
# without Recursion
def show(n):
    for i in range(5,0,-1):
        print(i,end=" ")  # 5 4 3 2 1 
show(5)
print("******* With Recursion*************")
# Using Recursion
def show(n):
    if(n==0):
        return
    print(n,end=" ")   # 5 4 3 2 1 end end end end end
    show(n-1)
    print("end",end=" ")
show(5)

print()
# calculate factorial of a number n using recursion
def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1) * n

print(fact(5))    #120


# Write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    if(n==0):
        return 0
    return sum(n-1)+n    
sum=sum(5)    
print(sum) #15

# WAP to calculate sum of first n namtural number
sum=0
for I in range(5,0,-1):
    sum=sum+I
print(sum)  #15

#Write a recursive function to print all elements in a list.
list=[1,5,8,9,0,3]
def recur(list1,idx=0):
    if(idx==len(list1)):
        return
    print(list1[idx])
    recur(list1,idx+1)    
print(list)
   
 # using while loop print each element of a list
list=[1,5,6,9]
def scan(list):
    i=0
    while(i<len(list)):
        print(list[i])
        i+=1
    
scan(list)

# Using for loop print each element of list
def scan(list):
    for i in list:
        print(i)
scan(list) # 1 5 6 9   






    









     
