# Variables
# Python has no command for declaring a variable.
# A variable is created the moment you assign a value to it.

x = 5
y = "pr0gr4mma"
print(x)
print(y)

# A variable does not need to be declared with any particular type and can change after they have been set.

a = 10
a = "Dave"
print(a)

# Casting is a process where we can specify the data type of the variable.

b = str(3)
c = int(3)
d = float(3)
print(b)
print(c)
print(d)

# You can get the data type of a variable with the type() function.

e = 1
f = "Johnny"
print(e)
print(f)

# Strings can be set in either single or double quotes.

g = "Mark"
h = 'Mark' 
print(g)
print(h)

# Variables are case sensitive

i = "Tom"
I = 10
print(i)
print(I)

# I will not overwright i

# Variable names
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

# Multi word Variables can be used as techiques to help you read the variable

# Camel Case

myVariableName = "Dan"
# Pascal Case

MyVariableName = "Matt"

# Snake Case

my_variable_name = "Harry"

# Assign multiple variabes

j, k, l = "Banana", "Orange", "Grape"
print(j)
print(k)
print(l)

# One Value to multiple variables

m = n = o = "Cars"
print(m)
print(n)
print(o)

# Unpack a collection

fruits = ["Cherry", "Mango", "Dragon fruit"]
p, q, r = fruits
print(p)
print(q)
print(r)

# Global variables
# These are variables that are used outside of a function (all the examples above are global variables).
# These can be used by everyone inside and outside the function.

s = "greatest!"

def myfunc():
    print("I am the " + s)

myfunc()

# Local variables are when you create a variable within a function.

def myfunction():
    s = "best!"
    print("I am the " + s)

myfunction()

# If we use the global keyword it shows that variable belongs to the global scope

def myfunction():
    global s
    print("I am the " + s)

myfunction()

# Use the global keyword if you want to change a global variable inside a function
t = "fastest!"
def lesgo():
    global t
    t = "best!"
    print("I am the " + t)

lesgo()