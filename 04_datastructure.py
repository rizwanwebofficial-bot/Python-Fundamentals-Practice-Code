# List 
saman = ["aalo", "pyaaz", "tamatar", 1,2,3, 1.2, 2.3, True, False]

print (saman)

print (saman[0]) # aalo
print (saman[-1]) # False

# saman[10] = "gobhi" # False method of adding a new value at index 10
saman.append("gobhi") # Correct method of adding a new value at the end of the list
saman.insert(11, "mirchain") # Correct method of adding a new value at the specific index of the list
print (saman)

# Tuples 
tuples = ("aalo", "pyaaz", "tamatar", 1,2,3, 1.2, 2.3, True, False)
print (tuples)

tuples[10]="gobhi" # This will give an error because tuples are immutable

tuples[0] = "Bhindi" # This will give an error because tuples are immutable


# set 
saman = {"aalo", "pyaaz", "tamatar", 1,2,3, 1.2, 2.3, True, False}
print (saman)                #very important to note that true is not present in the set output because it is already present as 1 in the set.

# Dictionary 
cars = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print (cars)

