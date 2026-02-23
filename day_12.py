# TUPLE
# a tuple is a collection of values stored in a single variable similar to a list
# immutable,ordeed,allow duplicate values

data=(10,20,30,40,50,60)
print(data)
print(type(data))
print(data[0])
print(data[-1])
print(data[1:5])


# count()
t=(1,2,2,3,4,5,7,9,3,2)
print(t.count(2))
# index()
print(t.index(3))
# len()
print(len(t))
# max()
print(max(t))
# min()
print(min(t))
# sum()
print(sum(t))

# Create a tuple and print its length.
t=(1,2,3,4,5)
print(len(t))

# Find the index of value 5 in (1, 3, 5, 7).
t1=(1,3,5,7)
print(t1.index(5))

# Count how many times 2 appears in (2,2,3,4).
t2=(2,2,3,4)
print(t2.count(2))