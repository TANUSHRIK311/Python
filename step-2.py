# ------------------------------------------------------------------------------------------------------
# String Manipulation
# ------------------------------------------------------------------------------------------------------

#Concatanation
first_name = "Tanu"
last_name = "shri"
full_name = first_name + " " + last_name
full_name = first_name + last_name
print(full_name)

#Repeating
messege = "Warning !" * 10
Notification = "Desclaimer "
print(messege)
print(Notification * 5)

#----------------------------------
# String Methods
#----------------------------------
chat = "Hi Hello "
print(chat.upper())
print(chat.lower())
print(chat.strip() *2) #spaces are removed only at the end and beginning not in between words 
# so inorder to see that repaeting 2 times as *2

#----------------------------------
# replace()
#----------------------------------

hat = "red"
print(hat.replace("red","white"))
print(hat)

#we are getting red bcz , Strings in python are Immutable
# and we are just printing and not saving the replace string 

hat = "white"
print(hat)
#we can do this also
hat = hat.replace("red", "white")
print(hat)

name = "Tanushri said 'Hello'"
print(name)
name = 'Tanushri said "Hello" '
print(name)
name = ''' Tanushri said "Hello"
           shri said "hi" '''
print(name)

# string length
messege = "Warning !"
print(len(messege))

#accessing String character
name = "tanu"
name[0] #index = position - 1
print(name[1])
print(name[3])

# Accessing substring (string slicing)
name = "tanushri"
print(name[4:8]) #output - shri
print(name[:8]) #output - tanushri
print(name[4:]) #output - shri

# Reverse Accessing string
name = "tanushri k"
print(name[-2])

