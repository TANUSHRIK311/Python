print("hello")
# ------------------------------------------------------------------------------------------------------
# VARIABLES
# ------------------------------------------------------------------------------------------------------
a=10
b=20
name = "chandan"
is_switch_on = True # make sure Boolean true T is capital
print(a) # printing a's value that is 10
print("a") # printing a as a string not a value thatit holds basically giving a as string
print(a+b)
a = 10 
b = 20
c = 30 
a, b, c = 10, 20, 30
a = b = c = 10 # which is equal to a = 10 b = 10 c = 10
name = "tanushri"
Name = "K Tanushri"
print(name)
print(Name)

# ------------------------------------------------------------------------------------------------------
# DATA TYPES
# ------------------------------------------------------------------------------------------------------

name = "Tanushri" #string
is_student = False #bool
weight = 69.5 #float
print(type(name)) # type prints the datatype of that variable
print(type(weight))
print(type(is_student)) 

is_student = "yes"
print(type(is_student)) #Dynamically typed here the datatype is changes from boolean to string

# Type Conversion 
age = 22
age_float = float(age) #type is converted
print(age_float)

s = "100"
print(type(s))
#print(s+age) 
#cannot concatenate differeent type
print(int(s)+age) 

s = "Tanu"
# print(int(s)) 
# the alphabets inside double quotes cannot be converted to int, 
# but if numbers inside double quotes can be converted to int


# ------------------------------------------------------------------------------------------------------
# OPERATORS
# ------------------------------------------------------------------------------------------------------

a = 10
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) #floor division
print(a%b)  #modulus
print(a**b) #exponential
print(a+b-c**a) # Works on BODMAS Rule

# Basic Swapping
a = 10
b = 20
temp = a
a = b
b = temp
print(a,b)
print("a =",a, "b =",b)

#declaring variable in python without assigning any value
marks = None
print(type(marks))
marks = 99.9
print(type(marks))

# ------------------------------------------------------------------------------------------------------
# I/O Operations
# ------------------------------------------------------------------------------------------------------

# output
print("Out put")

# Input
age = input("Age:")
print(age)

boy_name = input("BoyName=")
girl_name = input("GirlName=")
boy_age = int(input("BoyAge:"))
girl_age = int(input("GirlAge:"))
age_diff = boy_age - girl_age

age_diff_accurate = abs(boy_age - girl_age) 
'''
this is to avoid -ve integer 
using abs we can convert -ve int to +ve int 
it works as modulus that convets -ve to +ve
it considers Only Absolute value
'''

print(boy_name)
print(girl_name)
print(boy_name + " marries " + girl_name)
print(boy_name + " loves" + girl_name + " Age Difference is " + str(age_diff))

print(f"{boy_name} loves {girl_name} . Age Difference is {age_diff} ")

print(f"{boy_name} loves {girl_name} . Age Difference is {age_diff_accurate} ") #handled by abs 


# ------------------------------------------------------------------------------------------------------
# COMMENTS
# ------------------------------------------------------------------------------------------------------
 
 # SINGLE LINE
'''
MULTI LINE COMMENT
'''


