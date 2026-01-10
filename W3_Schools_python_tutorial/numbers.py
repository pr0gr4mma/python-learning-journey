# There are three numeric types in Python
# Int
# Float
# Complex

a = 1 # int
b = 3.4 # float
c = 1j

# To verify the type of onbject in python use the type() function

print(type(a))
print(type(b))
print(type(c))


# Print Numbers
# You can also use print() function to display numbers.
# However, numbers are not put inside quotes.

print(3)
print(10)
print(5000)

# You can also do Math inside a print() function.

print(4 + 6)
print(5 * 8)

# You are also able to mix text and number

print("I am", 30, "next year.")

# Integers is a whole number positive or negative number without decimals of unlimited length.

d = 1
e = 2384734
f = -204332

print(type(d))
print(type(e))
print(type(f))

# Float numbers are a positive or negative number with one or more decimals

g = 1.3
h = 1232.24124321
i = -24432982.23412

print(type(g))
print(type(h))
print(type(i))

# Float can also be scientific numbers with an "e" to indicate the power of 10.

j = 35e3
k = 2349E23
l = -23e4

print(type(j))
print(type(k))
print(type(l))

# Complex numbers are written with a "j" as the imaginary part

m = 3+5j
n = 5j
o = -5j

print(type(m))
print(type(n))
print(type(o))

# You can convert from one type to another using the int(), float() and, complex() methods

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
A = float(x)

#convert from float to int:
B = int(y)

#convert from int to complex:
C = complex(x)

print(A)
print(B)
print(C)

print(type(A))
print(type(B))
print(type(C))

# You cannot convert complex numbers into another number type.You cannot convert complex numbers into another number type.

# Random number
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
import random
print(random.randrange(1, 10))
