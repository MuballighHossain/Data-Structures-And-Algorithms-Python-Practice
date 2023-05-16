# set is the collection of unique elements

# defined using curly braces similar to dictionary data structures

s = set()
print(s)

s1 = set("hello")
print(s1)

s2 = set([1,2,3,4])
print(s2)

s2 = {1,2,3,4}
print(type(s2))

# duplicate values will not be taken
s3 = {1,2,3,1,2,3}
print(s3)

# set is unordered

# set is mutable

s3.add(4)

# set can only contain immutable types as objects
# s4 = {[1,2,3],3} ---> will throw error

# set cannot be nested

# set can have different types of elements, but they should be immutable

# mathematical functions like union, intersection can be performed

# to access elements we have to use looping or we have to use in operator

print(1 in s3)

for i in s:
    print(i)

#test
