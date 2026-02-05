# LOOP CONTROL STATEMENTS
# They change the normal flow loops based on certain conditions

# break
# continue
# pass

# break statement:
# the break statement is used to immediately stop a loop,even if the loop condition still True

for i in range(1,10):
    if i==5:
        break
    print(i)

# continue
# the continue statement is used to skip the current iteration and move to the nesxt iteration of the loop

for i in range(1,8):
    if i==5:
        continue
    print(i)

# pass
# the pass statement is used as a placeholder. it does nothing but avoids sytax errors when a statement is required

for i in range(1,6):
    if i==3:
        pass
    print(i)

print("task1:")
# Task1:
for i in range(1,11):
    if i==6:
        break
    print(i)

print("task2:")

# task2:

for i in range(1,11):
    if i==4:
        continue
    print(i)

print("task3:")

# task3:
for i in range(1,11):
    if i%3==0:
        continue
    print(i)


print("task4:")

# task4

for i in range(1,11):
    if i%2==0:
        continue
    print(i)

print("task5:")

# task5

for i in range(1,6):
    if i==3:
        pass
    print(i)

print("task6:")
# task6
lst=[2,4,6,8,10,7,12]
for i in lst:
    if i==7:
        break
    print(i)


print("task7:")
# task7

str1="python programming"
for char in str1:
    if char=='o':
        continue
    print(char)


print("task8:")

# task8

for i in range(1,11):
    if i%8==0:
        break
    print(i)


print("task9:")

# task9

lst=["apple","","banana","","cherry"]
for i in lst:
    if i =="":
        continue
    print(i)


print("task10:")

# task10

student={"name":"arjun","age":20,"marks":85}
for i in student:
    if i=="age":
        pass
    else:
        print(i,":",student[i])
