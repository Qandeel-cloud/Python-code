#  "is"  vs "==" is compares exact location of object in memory  and == compares values

a = 3
b = 3
print(a is b)
print(a == b)

a = "string"
b = 3
print( a is b)
print(a == b)

a = [1,2,3]
b = [1,2,3]
print( a is b)
print(a == b)

