info = {
 "key" : "value",
 "name" : "surya",
 "learning" : "coding",
 "is_adult" : True,
 "age" : 21,
 "salary" : 500.50,
 "subject" : ["physics", "Math", "Hindi", "sanskrit"] ,
 "topics" : ("hello", "morning") ,
 12 : 34,
 12.5:36.5,
 list : [1,4,5],
 #tup : (1,4,6) #we donot make tupple as key else error will show as in tupple we canot change value.
 
}

print(info)
# {'key': 'value', 'name': 'surya', 'learning': 'coding', 'is_adult': True, 'age': 21, 'salary': 500.5, 'subject': ['physics', 'Math', 'Hindi', 'sanskrit'], 'topics': ('hello', 'morning'), 12: 34, 12.5: 36.5, <class 'list'>: [1, 4, 5]}
print(info["name"]) #surya
print(info["subject"]) #['physics', 'Math', 'Hindi', 'sanskrit']
print(info["topics"]) #('hello', 'morning')
print(info["salary"]) #500.5

info["name"]="Ritu"
print(info["name"]) #Ritu
print(info["subject"].keys()) # dict_keys(["physics", "Math", "Hindi", "sanskrit"])
info["lastname"]="mishra" # at run time key and its value is stored in dictionary
print(info["lastname"]) #mishra
new_dic={ } # we can create empty dictonary also

student = {
   "name":"Ritu",
   "subject": {
       "Math": 98,
       "physics": 100,
       "chem": 81,
       "Soc":100
       
   }
}
print(student) # {'name': 'Ritu', 'subject': {'Math': 98, 'physics': 100, 'chem': 81, 'Soc': 100}}
print(student["subject"]) # {'Math': 98, 'physics': 100, 'chem': 81, 'Soc': 100}
print(student["subject"]["Math"]) #98

print("**************************************")

print(student.keys()) #return all parent keys dict_keys(['name', 'subject']) but not nested/child keys
print(len(student.keys())) # print length of dict   2
print(list(student.keys())) # type casting dictonary into list ['name', 'subject']
print(len(list(student.keys()))) # 2

print(student.values()) #dict_values(['Ritu', {'Math': 98, 'physics': 100, 'chem': 81, 'Soc': 100}])
print(list(student.values())) #['Ritu', {'Math': 98, 'physics': 100, 'chem': 81, 'Soc': 100}]

#return all key value pairs as tupple
print(student.items()) #dict_items([('name', 'Ritu'), ('subject', {'Math': 98, 'physics': 100, 'chem': 81, 'Soc': 100})])
print(list(student.items())) #[('name', 'Ritu'), ('subject', {'Math': 98, 'physics': 100, 'chem': 81, 'Soc': 100})]
pairs=list(student.items())
print(pairs[0]) #('name', 'Ritu')  


# Returns the value according to key
print(student.get("name")) #Ritu
print(student.get("name1")) #None
print(student.get("subject")) #{'Math': 98, 'physics': 100, 'chem': 81, 'Soc': 100}
#Using student["name"] also we can return value but there is difference between both
print(student["name"]) #Ritu
#print(student["name1"]) #error

#update existing dictonary
new_dic={"city":"Patna", "name":"Surya"}
student.update(new_dic)
print(student) #{'name': 'Surya', 'subject': {'Math': 98, 'physics': 100, 'chem': 81, 'Soc': 100}, 'city': 'Patna'}













