"""

===========================================================
   LECTURE 02 - SET 02 : INDEXING & SLICING
   Topics : Indexing, Slicing, Negative Slicing 
   Total Questions :  
============================================================

"""

# ==========================================================
# PART A:   Indexing
# ==========================================================

# Q1: Basic indexing
#   Given: word = "Python"
#   Print each character using positive indexing 
#   (0, 1, 2, 3, 4, 5)
#   Print first and last character.

word = "PYTHON"

print("Index 0:", word[0])
print("Index 1:", word[1])
print("Index 2:", word[2])
print("Index 3:", word[3])
print("Index 4:", word[4])
print("Index 5:", word[5])
print("First:", word[0], " , Last:", word[5])

# ----------------------------------------------------------

# Q2: Given: email = "user@example.com"
#    Print character at index 0, 4, 5, and last character
#    Print the '@' symbol using indexing

print("\n--- Email Character Extraction ---")

email = "user@example.com"

print("Index 0:", email[0])
print("Index 4:", email[4])
print("Index 5:", email[5])
print("Last character:", email[15])
print("@ symbol at index:", email[4])

# ----------------------------------------------------------

# ==========================================================
# PART B:   Slicing
# ==========================================================

# Q3: Basic slicing
#   Given: text = "Hello World"
#   Extract: "Hello", "World", "Hello World", "llo Wo"
#   Print each with the slice notation used.

text = "Hello World"

print("text[0:5] =", text[0:5])
print("text[6:11] =", text[6:11])
print("text[0:11] =", text[0:11])
print("text[2:9] =", text[2:9])

# ----------------------------------------------------------

# Q4: Slicing with step
#   Given: numbers = "0123456789"
#   Extract every 2nd character
#   Extract every 3rd character
#   Extract characters in reserve.

numbers = "0123456789"

print("Every 2nd:", numbers[::2])
print("Every 3rd:", numbers[::3])
print("Reversed:", numbers[::-1])

# ----------------------------------------------------------

# Q5: Palindrome checker using slicing
#    Given: word1 = "radar", word2 = "python"
#    Check if each is palindrome by comparing with reversed
#     version
#    Print result for both.

word1 = "radar"
word2 = "python"
print("'radar' reserved:", word1[::-1])
print("Is 'radar' a palindrome?", word1 == word1[::-1])
print("'python' reversed:", word2[::-1])
print("Is 'python' a palindrome?", word2 == word2[::-1])

# ----------------------------------------------------------

# Q6: Reserve string using slicing
#   Given: text = "Hello World"
#   Reserve only entire string
#   Reserve only "Hello" part
#   Reserve only "World" part
#   Swap "Hello" and "World" positions.

text = "Hello World"
print("Original:", text)
print("Reserved:", text[::-1])
print("Reserve 'Hello':", text[0:5][::-1], text[5:] )
print("Reserve 'World':", text[0:6], text[6:][::-1])
print("Swapped:", text[6:], text[0:5])

# ----------------------------------------------------------

