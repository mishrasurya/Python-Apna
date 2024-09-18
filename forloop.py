list=[1,6,8,9,10, "hello"]
for el in list:
    print(el) # 1 6 8 9 10 hello

tup=(1,6,9,"surya")
for el in tup:
    print(el) # 1 6 9 surya

str="surya"
for el in str:
    print(el) # s u r y a end
else:
    print("end")

print("#############################")
# Print the elements of the following list using for loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
list=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
for el in list:
    print(el) # 

print("#############################")
# Search for a number x in this tuple using loop:
#[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
tup=(1, 4, 9, 16, 25, 36, 49, 64, 81,100)
idx=0
for el in tup:
    if(el==49):
        print(el,"found at index",idx) # 49 found at index 6
    idx+=1
    
# Range functions returns a sequence of numbers, starting from 0 by default, and increments by
# 1 (by default), and stops before a specified number.
# range( start?, stop, step?)
print("#############################")
for el in range(5): #range(stop)
    print(el) # 0 1 2 3 4
print("#############################")
for el in range(1,5): #range(start,stop)
    print(el) # 1 2 3 4
print("#############################")
for el in range(1,10,2): #range(start,stop)
    print(el) # 1 3 5 7 9

print("print 2 to 20, all even numbers ")
for el in range(2,21,2):
    print(el)

print("print 1 to 20, all odd numbers ")
for el in range(1,21,2):
    print(el)

print("print 1 to 100 using for and range")   
for el in range(1,101):
    print(el)
print("print 100 to 1 using for and range") 
for el in range(100,0,-1):
    print(el)

print(" Print multiplication table of number n")
num=int(input("enter the number: "))
for el in range(1,11):
    print(el*num) # 3 6 9.....30

# pass stetement used when you donot write anything in loop and without pass you will see error in this case so we use pass

print("WAP to find sum of first n number using for and range")
num=int(input("enter the number: "))
temp=0
for el in range(1, num+1):
    temp=temp+el
print(temp) 

print("WAP to find sum of first n number using while loop")
temp=0
num=int(input("enter the number: "))
i=1
while(i<num+1):
    temp=temp+i
    i+=1
print(temp)    

print("#############################")
print("WAP to find factorial of first n number using for")
num=int(input("enter the number: "))
fact=1
for el in range(1,num+1):
    fact=fact*el
print(fact)    #120

print("#############################")
print("WAP to find factorial of first n number using while loop")
num=int(input("enter the number: "))
fact=1
i=1
while(i<=num):
    fact=fact*i
    i+=1
print("Factorial of",num, "is: ", fact)    #120






