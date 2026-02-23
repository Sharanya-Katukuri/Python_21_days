# SET
# set is a collection of unique values
# written using curly braces {}
# unoredered,not allow duplicate values,mutable

nums={1,2,3,3}
print(nums)
print(type(nums))
num={}
print(type(num))

# add()
s={1,2,3}
s.add(4)
print(s)

# update()
s1={1,2}
s1.update([3,4,5])
print(s1)

# remove()
set1={1,3,4,2,5,6,8}
set1.remove(8)
print(set1)
# set1.remove(9)
# print(set1)

# discard()
set1.discard(9)
print(set1)

# pop()
set1.pop()
print(set1)
set1.pop()
print(set1)

# clear()
set1.clear()
print(set1)

a={1,2,3}
b={3,4,5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))


# Add value 10 to a set.

set2={1,3,5,8}
set2.add(10)
print(set2)

# Remove value 3 from a set.
set2.remove(3)
print(set2)

# Find union of {1,2} and{2,3}.
s1={1,2}
s2={2,3}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1&s2)
print(s1.difference(s2))
print(s1-s2)

x={1,2,4}
y={1,2}
print(x.issubset(y))
print(y.issubset(x))