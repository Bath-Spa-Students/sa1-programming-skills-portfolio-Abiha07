#  analysing keys in the dictionary 

dictionary  = { 'Name' : 'abiha' , 'Roll No ' :  '1122' , 'Fathers name ': 'asad' } 
print(dictionary.keys())


# evaluating the keys

dictionary  = { 'Name' : 'abiha' , 'Roll No' :  '1122' , 'Fathers name ': 'asad' } 
del dictionary ["Name"]
print(dictionary.items())


# using pop method to remove a key

dictionary  = { 'Name' : 'abiha' ,
                'Roll No' :  '1122' , 
                'Fathers name ': 'asad' } 
print(dictionary.pop("Roll No"))
print(dictionary.keys())
print(dictionary.values()) 
