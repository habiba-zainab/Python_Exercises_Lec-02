"""

===========================================================
   LECTURE 02 - SET 03 : STRING FUNCTIONS
   Topics :     String Functions
   Total Questions :  
============================================================

"""
# ==========================================================
# PART A:   Search Functions
# ==========================================================

# Q1: Given: text = "Python Programming is fun. Python is 
#             powerful."
#    Find the position of:
#     - First occurence of "Python"
#     - First occurence of "is"
#     - Substring "Java" (not present)
#     - Second occurence of "Python" 
#       (Hint: use find with start parameter)

text = "Python Programming is fun. Python is powerfull."
print("Text: ", text)
print("First 'Python' at: ", text.find("Python"))
print("First 'is' at: ", text.find("is"))
print("'Java' position: ", text.find("Java"))
print("Second 'Python' at: ", text.find("Python", 7))

# ----------------------------------------------------------

# Q2: Given: data = "Hello World"
#    Use str.index() to find:
#     - Position of "World"
#     - Position of "o" (first occurence)

data = "Hello World"
print("Data: ", data)
print("'World' index: ", data.index("World"))
print("'o' index: ", data.index("o"))

# ----------------------------------------------------------

# ==========================================================
# PART B:   Counting & Validation Functions
# ==========================================================

# Q3: Given: sentence = "apple banana apple cherry pie apple"
#    Count how many times:
#     - "apple" appears
#     - "banana" appears
#     - "a" appears (character count)
#     - " " (space) appears

sentence = "apple banana apple cherry pie apple"
print("Sentence: ", sentence)
print("'apple' count: ", sentence.count("apple"))
print("'banana' count: ", sentence.count("banana"))
print("'a' count: ", sentence.count("a"))
print("Spaces count: ", sentence.count(" "))

# ----------------------------------------------------------