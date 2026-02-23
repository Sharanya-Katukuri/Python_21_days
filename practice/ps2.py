# # Write a Python program to count the number of characters in a given string
# # (without using len()).

# text=input("enter a string:")
# count=0
# for i in text:
#     count+=1
# print(count)

# # Write a Python program to count the number of vowels in a given string.
# text=input("enter a string:").lower()
# count=0
# for i in text:
#     if i in "aeiou":
#         count+=1
# print(count)

# # Write a Python program to count the number of consonants in a given string.

# text=input("enter a string:").lower().replace(" ","")
# count=0
# for i in text:
#     if i.isalpha() and i not in "aeiou":
#         count+=1
# print(count)

# Write a Python program to reverse a string (without using slicing [::-1]).
word=input("enter a string:")
rev=""
for char in word:
    rev=char+rev
print(rev)