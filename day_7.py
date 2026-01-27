# conditional statements :it is an decision making statement.
# it checks the conditions one by one ,if True code will be executed  , if it is False it skips the condtions

# if
# if-else
# if-elif-else

# if Statement:
# it checks only one condtion if the condition is true code will be exected otherwise it skips

age=23
if age>=18:
    print("you are eligible to vote")

# if-else statement:
# it checks the two condtions,True and False
# if the condtion True ,if block will be exected, Otherwise else block will be exected

number=7
if number%2==0:
    print("Even number")
else:
    print("Odd number")


# if-elif-else
# it checks multiple condtions
# first check if condition,if condtion true if block will be exected,
# if condtion false next, checks the elif condtion, it checks util the condtion true
# if all condtion false , then else block will be exected

marks=75
if marks>=90:
    print("Grade A")
elif marks>=60:
    print("Grade B")
else:
    print("Grade c")


# task1:
num=int(input("enter a number:"))
if num>0:
    print("Positive")
else:
    print("Not positive")

# task2:
n1=int(input("enter a number:"))
if n1%2==0:
    print("Even")
else:
    print("Odd")

# task3:
age=int(input("enter youe age:"))
if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible")

# task4:
n2=int(input("enter a number:"))
if n2>100:
    print("Greater than 100")
else:
    print("100 or less")

# task5:
char=input("enter a character:")
if char in "aeiou":
    print("Vowel")
else:
    print("Not a vowel")

# task6:
n3=int(input("enter a number:"))
if n3%3==0 and n3%5==0:
    print("Divisible")
else:
    print("Not divisible")

# task7:
a=int(input("enter a value:"))
b=int(input("enter a value:"))
if a>b:
    print(f"{a} is largest")
else:
    print(f"{b} is largest")

# task8:
marks=int(input("enter your marks:"))
if marks>=90:
    print("Grade:A")
elif marks>=60:
    print("Grade:B")
else:
    print("Grade:C")

# task9:
year=int(input("enter a year:"))
if (year%100!=0 and year%4==0) or year%400==0:
    print("Leap Year")
else:
    print("Not a Leap year")

# task10:
age=int(input("enter age:"))
if age<12:
    print(50)
elif age<60:
    print(100)
else:
    print(70)
