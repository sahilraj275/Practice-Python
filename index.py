# Write a program to concatenate two strings. Use + and .join() methods to achieve the same result.
s1 = "Hello"
s2 = "World"

# print(s1 + s2)
# print(s1.join(s2)) --> #This does not achieve the intended result. Instead, .join() inserts the first string (s1) between each character of the second string (s2).
# print("".join([s1, s2]))

# Given a string text = "Python is fun!", write a program to:
# Access the first and last character.
# Slice the substring "Python" from the string.

text = "Python is fun!"

# print(text[0])
# print(text[-1])
# print("Python" in text)
# print(f"Does 'Python' exist in the text? {'Python' in text}")

# Write a program to count the number of vowels in a string.


# def countVowel():
#     count = 0
#     text = "Python is fun!"
#     for i in range(len(text)):
#         if (
#             text[i] == "a"
#             or text[i] == "e"
#             or text[i] == "i"
#             or text[i] == "o"
#             or text[i] == "u"
#         ):
#             count += 1
#     print(count)


# countVowel()


# def count_vowels(text):
#     vowels = "aeiou"
#     count = 0
#     for char in text.lower():  # Convert to lowercase for case insensitivity
#         if char in vowels:  # Check membership in the vowels string
#             count += 1
#     return count


# # Example usage
# text = "Python is fun!"
# print(f"Number of vowels in '{text}': {count_vowels(text)}")

# Given text = " Learn Python! ", write a program to:
# Remove leading and trailing whitespaces.
# Convert the string to lowercase and check if it starts with "learn".

text = " Learn Python! "
# print(text.strip())

text1 = text.lower()
# print(text1.startswith("learn"))

# Write a program to replace all occurrences of "is" with "was" in the string sentence = "This is a string. It is fun.".

sentence = "This is a string. It is fun."
updatedstr = sentence.replace("is", "was")
# print(sentence)
# print(updatedstr)

#! Write a program to reverse the words in a sentence. For example:

# Input: "Python is fun"
# Output: "fun is Python"


def reverseString(text):
    # str = " ".join(text.split()[::-1])
    str = text.split()[::-1]
    return " ".join(str)
    # return str


# str1 = reverseString("Hello Dear")
# print(str1)

# with reversed keyword
# def reverseKeyword(text):
#     str = text.split()
#     return " ".join(reversed(str))


# rev = reverseKeyword("Reverse Me")
# print(rev)


# type conversion
# int to str
# num = 23
# name = str(num)
# boolean = bool(name)
# decimal = float(name)
# print(type(name))
# print(type(decimal))
# print(type(boolean))

# name = "Sahil"
# integer = int(name)
# print(type(integer))

# implicit type conversion

# res = 3 + 6.4
# print(res)

# Basic Mathematical Operations
# import math

# x = 4
# # print(math.sqrt(x))
# # print(math.pow(x,3))
# # print(math.sin(x))
# # print(math.exp(x))
# # print(math.log(x))

# y = 9.6
# print(math.ceil(y))
# print(math.floor(y))
# print(math.trunc(y))

# a = "Sahilraj"
# # print(a[-1])
# # print(a[1::2])
# # print(len(a))
# # loop
# # for i in a:
# #     print(i)
# # repeat
# # a2 = a * 3
# # print(a2)

# index = 0
# while index < len(a):
#     char = a[index]
#     print(char)
#     index += 1


# string method
s = " labrador "
# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())

# s = "The quick brown fox"
# dog = s.split()
# # print(dog)

# words = ["The", "quick", "brown", "fox"]
# sentence = " ".join(words)
# # print(sentence)#
# index=s.find("fox")
# print(index)

# str1 = "Emma-is-a-data-scientist"
# substr = " ".join(str1.split("-"))
# print(substr)

#! List Practice
# list is a data type that stores ordered collection of items. key features of list are-
# 1. Ordered -> list stores data in order manner it means we can store and retrieve data in the same sequence.
# 2. Mutable -> lists are mutable meaning we can update, remove, add in the same way.
# 3.Heterogenous -> list can contain different types of data inside it.
# 4. Dynamic size -> list can grow and shink accordingly

myList = [1, 2, 3, 4, "Data", 55, 34]
print(myList)
# accessing a list
print(myList[2])
# slicing a list
# mylist([start:stop:step])
print(myList[1:3])
print(myList[:3])
print(myList[3:])
print(myList[1::2])
# updating a list
myList[4] = "Sahil"
print(myList)

# list function
# len()
print(len(myList))
# append() -> it adds the item in the last
myList.append(444)
# extend() -> The extend() method in Python is used to add all the elements of an iterable (list, tuple, set, etc.) to the end of the current list.
myList.extend((1, 2, 4))
print(myList)
