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


str1 = reverseString("Hello Dear")
print(str1)

# with reversed keyword
# def reverseKeyword(text):
#     str = text.split()
#     return " ".join(reversed(str))


# rev = reverseKeyword("Reverse Me")
# print(rev)

#! Given a string containing numbers separated by commas (e.g., "1,2,3,4,5"), write a program to calculate the sum of the numbers.

