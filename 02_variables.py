x = 10    #simple assignment
name = "Ali"

a, b = 1, 2     #multiple assignment(one line)

x = y = z = 0          #chain assignment

x = 5                    #Augmented assignment (update in-place)
x += 2   # x becomes 7
x *= 3   # x becomes 21

total = sum([1, 2, 3])        #Assignment from function / expression
msg = f"Hello {name}"

(major, minor) = (3, 14)      #destructuring assignment (tuple unpacking)

head, *middle, tail = [1, 2, 3, 4, 5]           # Unpacking with * (for “rest”)
# head=1, middle=[2,3,4], tail=5

person = {}              #Assignment from dictionary
person["age"] = 25

class Student:    #assignment to object attributes
    pass
s = Student()
s.name = "Sara"


for i in range(5):         #loop variable assignment
    x = i
    
    
squares = [x*x for x in range(5)]      #comprehension variable assignment


first, _ = (10, 20)   # _ is commonly used when you don't care       Temporary “throwaway” variables in unpacking


