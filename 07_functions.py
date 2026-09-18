# Functions 
# Recursive function 
# Lambda function 

# Simple function 
def baba():
    print("baba je dam krana ha")

baba()

# function with return statement 
def baba_1():
    return "baba je kuch dam krana ha"

print(baba_1())


# recursive function 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))


# lambda function
square = lambda x: x ** 2
print(square(5))    