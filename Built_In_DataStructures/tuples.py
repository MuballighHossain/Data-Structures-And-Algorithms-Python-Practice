# comma separated elements enclosed within parenthesis

tuple1 = (1,2,3,4)
print(type(tuple1))

tuple2 = 1,2,3,4
print(tuple2)

tuple3 = tuple()

print(tuple3)

tuple4 = (2)
print(type(tuple4))
tuple5 = (2,)
print(type(tuple5))

# tuples are immutable

tuple6 = (2,3,4)
# tuple6.append(5) -> will throw error

# stores the data of different type
# to access the elements from the tuple, use indexing -> first element is 0, also it supports negative indexing
# tuples can be nested

# tuples are faster than lists and are used when data is not supposed to be modified

