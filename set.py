collection = { 1,3,2,2,"hello","world",4,5.8,'a','f'} # In set duplicate values are ignored

print(collection) #{1, 2, 3, 4, 5.8, 'a', 'world', 'hello', 'f'}
#print(collection[0]) #error indexing not allowed
print(type(collection)) #<class 'set'>
print(len(collection)) #9

# collection={ } this is empty dict
collect=set()
print(type(collect)) #<class 'set'>

collection.add(10)
print(collection) # 10 is added to set {1, 2, 3, 'hello', 4, 'world', 5.8, 'a', 'f', 10}
collection.add("surya") # surya added to set
collection.add((11,31)) # (11, 31) tupple added to set
#collection.add([31,33]) # [31,33] list is not added to set, TypeError: unhashable type: 'list'
# remove 1 from the set
collection.remove(1)
print(collection) #{2, 3, 4, 5.8, 'hello', 'f', 10, 'surya', 'a', (11, 31), 'world'}
# Make set empty 
collection.clear()
print(collection) # set()

# Removes item randomly from the set
set1={ "surya","ritu","Bandana","ravi"}
set1.pop() # Randomly removing items for the 1st time it removed bandana and on next time it removes ritu 
print(set1) 

# union of 2 set = only gives unique values inside new set
set1={1,2,3}
set2={3,4,5}
print(set1.union(set2)) #{1, 2, 3, 4, 5}
print(set1) #{1,2,3} means union does not do any changed in old set 
print(set2) #{3,4,5} 

# intersection return common value
print(set1.intersection(set2)) # {3}
print(set1)

















