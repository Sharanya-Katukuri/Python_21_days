# LOOPS
# loops are used to repeat a block of code multiple times 
# insted of writing the same code again and again, loops help us run it
# automatically based on a condtion or 
# two types
# while loop
# for loop


# while loop
# The while loop executes a block of code as long as a condition is True. Before each
# iteration, Python checks the condition.

i=1
while i<=5:
    print(i)
    i+=1

# for loop
# The for loop is used to iterate over a sequence such as: • list • string • tuple • range of numbers

fruits=["apple","banana","orange"]
for fruit in fruits:
    print(fruit)

# range():the range() function is used with for loops to generate a sequence of numbers

for i in range(5):
    print(i)

for i in range(1,11,2):
    print(i)


# task1:
i=1
while i<11:
    print(i)
    i+=1

# task2:
i=2
while i<11:
    print(i)
    i+=1

# task3:
str1="python"
for char in str1:
    print(char)

# task4:
for i in range(1,6):
    print(i)

# task5:

sum=0
for i in range(1,6):
    sum+=i
print(sum)

# task6:

i=1
while i<11:
    print(f"5x1={5*i}")
    i+=1

# task7:

for i in range(1,21):
    if i%2!=0:
        print(i)

# task8:

str2="programming"
count=0
for char in str2:
    count+=1
print("count:",count)

# task9:

for i in range(10,0,-1):
    print(i)

# task10:

for i in range(1,6):
    print(i*i)