# For loop

saman = ["aalo", "pyaaz", "tamatar", 1,2,3, 1.2, 2.3, True, False]
for i in saman[1:5]: #only printing the values from index 1 to 4
    print (i)
    
    
# if else conditional statements 
age = 18
if age < 18:
    print ("You are a minor and less than 18")
    
elif age == 18:
    print ("You are 18 years old")
    
else:
    print ("You are an adult and greater than 18")
    
    
# While loop 

names = ["ali", "ahmed", "sara", "fatima", "hassan"]

i=0
while i < len(names):
    if names[i] == "sara":
        i=i+1
        continue # This will skip the iteration when the name is "sara"
    
    print (names[i])
    i+=1
