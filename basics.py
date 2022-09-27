from enum import Enum

#variables
name = "Lonagin"
age = 28
print(name, age)

#string stuff
print("""Name: Lonagin

Address: 55 Sicilian Ave, NewYork, NY

Zip: 21344
""")

print("lonagin".upper())

print("to be or not to be".title())

noun = "Jabberwocky"
print(len(noun))
print("bb" in noun)

#escapement
name = "Lon\"agin"
print(name)

#new line
name = "Lonagin\nWest"
print(name)

#index and slice
name = "Jabberwocky"
#want to get just the letters bb so slice name at index 2 and 4
print(name[2:4])

#Booleans
#numbers are all truthy values except for 0
#strings are truthy unless the string is empty
done = 0
if done:
  print("yes")
else: 
  print("no")

#numbers and data types
num = 2+3j
num1 = complex(2,3)

print(num)
print(num1.real, num1.imag)

#built in methods
print(abs(-5.5))
print(round(5.5))
print(round(3.23, 1))

#Enums
#this is used to create a const variable
class State(Enum):
  INACTIVE = 0
  ACTIVE = 1
print(State['ACTIVE'])
print(State.ACTIVE.value)
print(list(State))