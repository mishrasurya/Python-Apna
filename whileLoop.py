# while loop
# print surya 5 times
# print 1 to 5
i=1
while i<=5:
    print("Surya",i)
    i+=1

# print 5 to 1
i=5
while i>=1:
    print(i)   
    i-=1 
print("#############################")
# Print numbers from 1 to 100.
i=1
while i<=100:
    print(i)
    i+=1

# Print numbers from 100 to 1.
i=100
while i>=1:
    print(i)
    i-=1
print(" Print the multiplication table of a number from 1 to 10.")
i=1
while i<=10:
    print(3*i)
    i+=1

print("######################################")
# Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

list= [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
i=0
while i<len(list):
    print(list[i])
    i+=1

print("######################################")
#Search for a number x in this tuple using loop and once find break the loop
#[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

tup= (1,4,9,16,25,36,25,49,64,81,100)
i=0
while i<len(tup):
    if(tup[i]==25):
        print(tup[i]," found at index",i) # 25  found at index 4
        break
    i+=1

print("######################################")
# continue , 0 to 5 print except 3
i=0
while i<=5:
    if(i==3):
        i+=1
        continue
    print(i)   
    i+=1

print("######################################")
# print only odd numbers from 1 to 10
i=1
while i<=10:
    if(i%2==0):
        i+=1
        continue
    print(i)   # 1 3 5 7 9
    i+=1  

print("######################################")
# print only even numbers from 1 to 10
i=1
while i<=10:
    if(i%2!=0):
        i+=1
        continue
    print(i)   # 1 3 5 7 9
    i+=1  
