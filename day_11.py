# LIST:
# a list is a collection of multiple values stored in a single variable

# numbers=[1,2,3,4,5,6]
# print(numbers)
# print(type(numbers))
# print(numbers[2])
# print(numbers[-1])
# print(numbers[1:4])

# # append()
# nums=[1,2,3]
# nums.append(4)
# print(nums)
# # extend
# nums.extend([5,6,7])
# print(nums)
# # insert(position,value)
# nums.insert(2,10)
# print(nums)
# # remove()
# nums.remove(2)
# print(nums)
# # pop()
# nums.pop()
# print(nums)
# nums.pop(5)
# print(nums)
# # clear()
# nums.clear()
# print(nums)

# data=[10,20,30,40,10,30,20,10]
# # index()
# print(data.index(40))
# # count()
# print(data.count(10))
# print(data.count(20))
# # sort()
# data.sort()
# print(data)
# data.sort(reverse=True)
# print(data)
# # reverse()
# list1=[4,5,3,2,1,0]
# list1.reverse()
# print(list1)
# # copy()
# list2=list1.copy()
# print(list2)
# # len()
# print(len(list1))
# # max()
# print(max(list1))
# # min()
# print(min(list1))
# # sum()
# print(sum(list1))


# Task 1: Add number 50 to the list [10, 20, 30].
list1=[10,20,30]
list1.append(50)
print(list1)

# Task 2: Insert number 25 at index 1 in [10, 20, 30].
list2=[10,20,30]
list2.insert(1,25)
print(list2)

# Task 3: Remove number 20 from the list.
list2.remove(20)
print(list2)

# Task 4: Count how many times 5 appears in [5,5,2,5].
a=[5,5,2,5]
print(a.count(5))

# Task 5: Sort the list [3,1,4,2].
b=[3,1,4,2]
b.sort()
print(b)

# Task 6: Reverse the list [1,2,3].
d=[1,2,3]
d.reverse()
print(d)

# Task 7: Find the index of 40 in [10,20,30,40].
c=[10,20,30,40]
print(c.index(40))

# Task 8: Find the maximum value in [7,4,9].
lst=[7,8,9]
print(max(lst))

# Task 9: Find the sum of [10,20,30].
list3=[10,20,30]
print(sum(list3))

# Task 10: Create a copy of a list.
list4=list3.copy()
print(list4)

# Task 11: Using a for loop, print each element in the list [10, 20, 30, 40].

numbers=[10,20,30,40]
for num in numbers:
    print(num)


# Task 12: Using a for loop, calculate the sum of all elements in the list [5, 10, 15].
list1=[5,10,15]
total=0
for i in list1:
    total+=i
print(total)

# Task 13: Using a for loop, count how many even numbers are present in [1, 2, 3, 4,5, 6].

list2=[1,2,3,4,5,6]
count=0
for i in list2:
    if i%2==0:
        count+=1
print(count)

# Task 14: Using a for loop, create a new list that contains only numbers greater than 10 from [5, 12, 8, 20, 3].
old_list=[5,12,8,20,3]
new_list=[]
for i in old_list:
    if i>10:
        new_list.append(i)
print(new_list)


# Task 15: Using a for loop, find the largest number in the list [4, 9, 2, 7].
list5=[4,9,2,7]
largest=list5[0]
for i in list5:
    if i>largest:
        largest=i
print(largest)

