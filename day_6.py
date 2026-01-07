# OPERATORS
# ----->Operatorsare special symbols or keywords that perform on variables and values.

# Arithmetic Operators: used fro basic mathematical calucations

# addition(+)
# subtraction(-)
# Multiplication(*)
# Division(/)
# Modulus(%)
# Exponentiation(**)
# Floor Division(/)

print(2+4)
print(9-7)
print(10*4)
print(20/2)
print(30/4)
print(5**3)
print(55//5)

# Assignment:Used to store or update values in variables

# assignment(=)
# compound(+=,-=,*=,...)
a=4
a+=3
print(a)


# Comparision: Used to comapare two values , they always return True or False

# Equal to(==)
# not equal to(!=)
# Greater than(>)
# less than(<)
# Greater than or equal(>=)
# Less than or equal(<=)

print(5==5)
print(10!=9)
print(5>9)
print(4<7)
print(5>=9)
print(5<=9)

# Logical Operators : Used to combine Statements

# and: True if both statements are True
#  or : True if atleast one statement is True
# not:Reverse the result(True becomes False and False becomes True)

x=10
y=5
print(x>5 and y<10)
print(x>15 or y<10)
print(not(x>5))

# Identity Operators: Checks whether two variables refer to the same object in memory, not just equal values

# is:Returns True if both variables point to the same object
# is not:Returns Ture if they point to different objects


a=[1,2,3]
b=a
c=[1,2,3]
print(a is b)
print(a is c)
print(a is not c)

# membership Operators: Membership operators check whether a value exits inside a sequence such as a list, tuple,string,or set

# in:Returns True if the value exists
# not in : Returns True if the value does not exist

numbers=[1,2,3,4]
print(3 in numbers)
print(5 not in numbers)
print(2 not in numbers)

word="python"
print("p" in word)
print("z" in word)

# Bitwise Operators: It work on numbers at the binary level.

# computers store numbers in binary (base 2)
# decimal 5 = Binary 101
# decimal 3 = Binary 011

# AND(&): Bit is 1 only if both bits are 1
# OR(|):Bit is 1 if at least one bit is 1.
# XOR(^):Bit is 1 if bits are different.
# NOT(~):Inverts all bits.
# Left shift(<<): Shifts bits left(multiplies by 2)
# Right shift(>>):shifts bits right (divides by 2) 

a=5
b=3
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<1)
print(a>>1)


# Task1:
print(37%5)

# task2:
y=20
y-=5
print(y)

# task3:
print(50>40 and 50<60)

# task4:
lst=["java","python","c++"]
print("python" in lst)

# task5:
print(17//3)

# task6:
print(3**4)

# task7
a=5
b=10
a,b=b,a
print(a)
print(b)

# task8:
print(10 is not 10.0)

# task9

print("z" not in "sky")

# task10:
print(2&3)