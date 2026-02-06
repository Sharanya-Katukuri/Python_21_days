# # Write a Python program to check whether a given number is positive, negative, or zero.

# n=int(input("enter a number:"))
# if n==0:
#     print("number is zero")
# elif n>0:
#     print("positive number")
# else:
#     print("negative number")


# # Write a Python program to check whether a given number is even or odd
# n=int(input("enter a number:"))
# if n%2==0:
#     print("Even number")
# else:
#     print("Odd number")

# num=int(input("enter a number:"))
# if num&1==0:
#     print("even number")
# else:
#     print("odd number")


# # Write a Python program to find the largest of three numbers using conditional statements.

# n1=int(input("enter first number:"))
# n2=int(input("enter second number:"))
# n3=int(input("enter third number:"))

# if n1>=n2 and n1>=n3:
#     print(f"{n1} is largest number")
# elif n2>=n3 and n2>=n1:
#     print(f"{n2} is largest number")
# else:
#     print(f"{n3} is largest number")

# # Write a Python program to check whether a given year is a leap year.
# year=int(input("enter a year:"))
# if year%4==0 and year%100!=0 or year%400==0:
#     print("leap year")
# else:
#     print("not a leap year")


# Write a Python program to take marks (0–100) as input and print the grade:

# marks=int(input("enter marks:"))
# if marks<=100 and marks>=90:
#     print("grade:A")
# elif marks>=75:
#     print("grade:B")
# elif marks>=50:
#     print("grade:C")
# else:
#     print("Fail")

# # Write a Python program to check whether a given character is a vowel or consonant.

# char=input("enter a single character:").lower()
# if char.isalpha():
#     if char in "aeiou":
#         print("vowel")
#     else:
#         print("consonant")

# # Write a Python program to check whether a number is a multiple of both 5 and 11.

# num=int(input("enter a number:"))
# if num%5==0 and num%11==0:
#     print("multiple of both 5 and 11")
# else:
    # print("not multiple of both 5 and 11")

# # Write a Python program to check whether a given number is a 3-digit number.

# # only work on positive number
# n=int(input("enter a 3 digit number:"))
# if n>=100 and n<=999:
#     print("it is 3-digit number")
# else:
#     print("not a 3-digit number")

# #work on positive number and negative number
# n=int(input("enter a 3 digit number:"))
# if 100<=abs(n)<=999:
#     print("it is 3-digit number")
# else:
#     print("not a 3-digit number")


# # Print Numbers from 1 to N
# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     print(i)

# # Write a Python program to print all even numbers between 1 and 50 using a loop.

# for i in range(1,51):
#     if i%2==0:
#         print(i)


# for i in range(2,51,2):
#     print(i)


# # Write a Python program to find the sum of the first N natural numbers using a loop.
# n=int(input("enter a number:"))
# total=0
# for i in range(1,n+1):
#     total+=i
# print(total)


# # Write a Python program to print the multiplication table of a given number (from 1 to 10).
# n=int(input("enter a number:"))
# for i in range(1,11):
#     print(f"{n}x{i}={n*i}")


# # Write a Python program to count the number of digits in a given number using a loop.



# n=int(input("enter a number:"))
# count=0
# if n==0:
#     count=1
# else:
#     while n>0:
#         count+=1
#         n//=10
# print(count)


# # Write a Python program to find the factorial of a given number using a loop.

# n=int(input("enter a number:"))
# fact=1

# for i in range(1,n+1):
#     fact*=i
# print(fact)


# # Write a Python program to reverse a given number using a loop.

# num=int(input("enter a number:"))
# rev=0
# while num>0:
#     ld=num%10
#     rev=rev*10+ld
#     num//=10
# print(rev)

# # Write a Python program to print all factors of a given number using a loop.


# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)


# Write a Python program to check whether a given number is prime or not.

# n=int(input("enter a number:"))
# if n<=1:
#     print("plaese enter greater than one value")
# else:
#     for i in range(2,n):
#         if n%i==0:
#             print("not a prime number")
#             break
#     else:
#         print("prime number")


# # Write a Python program to print all prime numbers between 1 and 100.

# for i in range(2,101):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)

# Write a Python program to check whether a given number is a palindrome.

# n=int(input("enter a number:"))
# temp=n
# rev=0
# while temp>0:
#     ld=temp%10
#     rev=rev*10+ld
#     temp//=10
# if rev==n:
#     print("palindrome")
# else:
#     print("not palindrome")


# Write a Python program to check whether a number is an Armstrong number.

# n=int(input("enter a number:"))
# temp=n
# count=len(str(n))
# a=0
# while temp>0:
#     ld=temp%10
#     a+=ld**count
#     temp//=10
# if a==n:
#     print("armstrong")
# else:
#     print("not armstrong")

# Write a Python program to find the sum of digits of a given number.

# n=int(input("enter a number:"))
# total=0
# while n>0:
#     ld=n%10
#     total+=ld
#     n=n//10
# print(total)

# # Write a Python program to find the largest digit in a given number.

# n=int(input("enter a number:"))
# s=0
# while n>0:
#     ld=n%10
#     if ld>s:
#         s=ld
#     n=n//10
# print(s)


# Write a Python program to count how many even and odd digits are present in a given number.

n=int(input("enter a number:"))
even_count=0
odd_count=0
while n>0:
    ld=n%10
    if ld%2==0:
        even_count+=1
    else:
        odd_count+=1
    n//=10
print(even_count)
print(odd_count)

