# Data Types
# Python has the following data types built-in by default:
# Text Type: str
# Numberic Types: int, float, complex
# Sequence Types: list, tuple, range
# Mapping Type: dict
# Set Types: set, frozenset
# Boolean Types: bool
# Binary Types: bytes, bytearray, memoryview
# None Type: NoneType

# Getting the datatype can be done by:

varType = 5
print(type(varType))

a = "Hello World"
print(type(a))
b = 20
print(type(b))
c = 20.5
print(type(c))
d = 1j
print(type(d))
e = ["apple", "banana", "cherry"]
print(type(e))
f = ("apple", "banana", "cherry")
print(type(f))
g = range(6)
print(type(g))
h = {"name" : "John", "age" : 36}
print(type(h))
i = {"apple", "banana", "cherry"}
print(type(i))
j = frozenset({"apple", "banana", "cherry"})
print(type(j))
k = True
print(type(k))
l = b"Hello"
print(type(l))
m = bytearray(5)
print(type(m))
n = memoryview(bytes(5))
print(type(n))
o = None
print(type(o))

# Setting the specific data type

A = str("Hello World")
print(A)
B = int(20)
print(B)
C = float(20.5)
print(C)
D = complex(1j)
print(D)
E = list(("apple", "pear", "orange"))
print(E)
F = tuple(("fast", "slow", "medium"))
print(F)
G = range(6)
print(G)
H = dict(name="John", age=40)
print(H)
I = set(("one", "two", "three"))
print(I)
J = frozenset(("Loud", "Quiet", "Normal"))
print(J)
K = bool(5)
print(K)
L = bytes(5)
print(L)
M = bytearray(8)
print(M)
N = memoryview(bytes(6))
print(N)