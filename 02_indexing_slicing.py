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
