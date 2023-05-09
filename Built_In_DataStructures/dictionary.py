# Dictionary_name = {key1:value1, key2:value2.....}

# values can be mutable but keys are constant and cannot be changed

d = {}

d1 = {"muba":"muba.xyz", "hossain":"hossain@xyz"}

print(d1)

d2 = dict()
print(d2)

# keys cannot be duplicate or else it will throw error

d3 = {"j":1, "k":2, "j":3}
print(d3)   # second j will not be shown

# mutable elements cannot be used as keys for e.g. lists cannot be used as keys
# d4 = {[1,2]:1} -> will throw error

# dictionary is unordered -> no indexing is used, to access value keys are used

print(d1["muba"])

# dictionary is mutable

d1["muba"] = 1
print(d1)

d4 = {"1": {1:2}}
print(d4)


