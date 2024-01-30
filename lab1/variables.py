x = 5 #int
y = "Argyn" #str
print(x)
print(y)

a = str(3)    # x will be '3'
b = int(3)    # y will be 3
c = float(3)  # z will be 3.0
print(a, b, c)

d = 5
e = "John"
print(type(d))
print(type(e))

#VAR NAMES
myvar = "John"
my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print(myvar, my_var, myVar, MYVAR, myvar2)

#ASSIGN MULTI VALUES

fruits = ["apple", "banana", "cherry"]
s, f, h = fruits
print(s)
print(f)
print(h)

#OUTPUT VARIABLES
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = "John"
print(x, y)

#GLOBAL VARIABLES
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)