# # WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
# # 1st approach
# movies=[ ]
# mov=input("enter first movie: ")
# movies.append(mov)
# mov=input("enter second movie: ")
# movies.append(mov)
# mov=input("enter third movie: ")
# movies.append(mov)
# print(movies) #['dlj', 'kobra', 'mohra']
# # Second approach
# movies=[ ]
# movies.append(input("enter first movie: "))
# movies.append(input("enter second movie: "))
# movies.append(input("enter third movie: "))
# print(movies)

#WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
list=[1,2,3,2,1]
list1=list.copy()
list1.reverse()
if(list1==list):
    print("Palindrom of element")
else:
    print("Not palindrome")    

# WAP to count the number of students with the “A” grade in the following tuple.
tup=["C","D","A","A","B","A"]  
print(tup.count("A"))  #3
tup.sort()
print(tup)