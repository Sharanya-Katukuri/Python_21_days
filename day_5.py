# TYPE CASTING
# Type casting or type conversion is the process of converting a value from one data type into another data type.

# there are two types:
# Implicit Type conversion : python automatically converts one data type to another without user intervention  to avoid data loss.

a=10
b=2.5
c=a+b
print(c)
print(type(c))


# Explicit Type Casting: the programmer manually converts one data type to another using built-in functions
#  function:
# int()  ---integer
# float() ---float 
# str()   ---string
# list()  ---list
# tuple() ---tuple
# set()   ---set
# dict()  ---dict

# number-->string
num=25
s=str(num)
print(s,type(s))

# string -->integer
s="100"
i=int(s)
print(i,type(i))
f=float(i) #integer to float
print(f,type(f))

text=str(f) #number to string
print(text,type(text))



# list-->tuple
lst=[1,2,3]
t=tuple(lst)
print(t,type(t))


# tuple-->set
t=(1,2,2,3)
s=set(t)
print(s)

age=input("enter your age:")
age=int(age)
print("After 5 years:",age+5)


# task1:
a="50"
b="20"
c=int(a)+int(b)
print(c,type(c))

# task2:
pi=3.14
i=int(pi)
print(i,type(i))

# task3:
age=25
age=str(age)
print(f"Iam {age} years old")

# task4:
num1=0
num2=1
bool1=bool(num1)
print(bool1,type(bool1))
bool2=bool(num2)
print(bool2,type(bool2))

# task5:
number=input("enter a number:")
print(number*2)
num=int(number)
print(num*2)

# task6:
string="15.7"
fl=float(string)
print(fl,type(fl))
integer=int(fl)
print(integer,type(integer))

# task7:
my_data=[1,2,3]
my_tuple=tuple(my_data)
print(my_tuple,type(my_tuple))

# task8:
n1=int(input("enter a number:"))
n2=int(input("enter a number:"))
result=str(n1+n2)
print(f"The total sum is :{result}")


# task9:
print(bool(""),bool(" "))

# task10:
flt=9.99
x=int(flt)
sr="5"
y=int(sr)
add=x+y
print(add)