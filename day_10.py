# String: a string is a sequence of characters enclosed in quotes 
# single quotes: 'python'
# Double quotes: "python"
# triple quotes: """python"""
# string is immutable, meaning their values cannot be changed after creation

language="python"
print(language)
print(type(language))

# string indexing:
# each character in a string has an index number
text="python"
print(text[0])
print(text[3])
print(text[-1])

# string slicing
# slicing allows you to extract a portion of a string

text="programming"
print(text[0:6]) #characters from index 0 to 5
print(text[3:8]) #from index 3 to 7
print(text[:5]) # from start to index 4
print(text[5:]) # from index 5 to till end
print(text[::2]) # skip characters
print(text[::-1]) # Reverse string



# methods
# String methods are built-in functions that help us manipulate and analyze text easily.
# Since strings are immutable, these methods always return a new string instead of changing
# the original one.

# 1.lower()-converting all uppercase characters in a string into lower case
text="HELLO WORLD"
result=text.lower()
print(result)

# 2.upper()-converting all lowercase characters into uppercase
text="python programming"
result=text.upper()
print(result)

# 3.string- it removes extrs spaces from the beginning and end of a string.very useful when handling user input
text="   sharanya     "
result=text.strip()
print(result)

# 4.replace:replaces a specific word or character with another one 
text="i like java"
result=text.replace("java","python")
print(result)

# 5.split:splits a string into a list based on a delimiter.

text="apple,banana,orange"
result=text.split(",")
print(result)

# 6.join():joins elements of a list into a single string using a separator
words=["python","is","easy"]
result=" ".join(words)
print(result)

# 7.find() : returns the index position of the first occurrence of a substring. 
# if substring is not found, it returns -1.

text="python programming"
result=text.find("programming")
print(result)
results=text.find("o")
print(results)


# 8.count()-counts how many times a character or word appears in a string
text="banana"
result=text.count("a")
print(result)

# 9.startswith():checks whether a string starts with a specific value.
# it returns either True or False

text="python"
result=text.startswith("p")
print(result)

# 10.endswith()-checks whether a string ends with a specific value

text="lesson.pdf"
result=text.endswith(".pdf")
print(result)

# 11.capitalize():converts the first character of a string to uppercase
text="python"
result=text.capitalize()
print(result)

# 12.title():capitalizes the first letter of each word in a string
text="python programming language"
result=text.title()
print(result)

# 13.isdigit():checks whether a string contains only numberic digits

text="12345"
print(text.isdigit())
word="sharanya"
print(word.isdigit())

# 14.isalpha():checks whether a string contains only alphabets
text="python"
result=text.isalpha()
print(result)

text="python123"
result=text.isalpha()
print(result)

# isalnum():checks whether a string contains both alphabets and numbers
text="python123"
result=text.isalnum()
print(result)


# Task 1: Reverse the string "Python" using slicing.
word="sharanya"
print(word[::-1])

# Task 2: Extract "gram" from "programming".
word="programming"
print(word[3:7])

# Task 3: Convert "WELCOME" to lowercase.
text="WELCOME"
print(text.lower())

# Task 4: Count number of "a" in "banana".
fruit="banana"
print(fruit.count('a'))

# Task 5: Split "10|20|30" using |.
text="10|20|30"
print(text.split("|"))

# Task 6: Join ["Python","is","fun"] with spaces.
lst=["Python","is","fun"] 
print(" ".join(lst))

# Task 7: Check if "123abc" is alphanumeric.
text="123abc"
print(text.isalnum())

# Task 8: Replace "old" with "new" in a string.
text="java programming"
print(text.replace("java","python"))

# Task 9: Check if "file.txt" ends with ".txt".
text="file.txt"
print(text.endswith(".txt"))

# Task 10: Convert "hello world" to title case.
text="hello world"
print(text.title())