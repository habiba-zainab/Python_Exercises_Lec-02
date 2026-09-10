"""

===========================================================
   LECTURE 02 - SET 01 : BASICS OF STRINGS
   Topics : String Methods & Escape Sequences
   Total Questions :  
============================================================

"""
# ==========================================================
# PART A:   Strings
# ==========================================================

# Q1: String split and join
#    Given: data = "apple , banana , orange , mango"
#    Split by comma into list
#    Join list with " - " seperator
#    Print both results.

data = "apple, banana, orange, mango"
print("Original:", data)
split_list = data.split(',')
print("Split list:", split_list)
print("Joined:", ' - ' .join(split_list))

# ----------------------------------------------------------

# Q2: String method chaining
#    Given: messy_text = "   HELLO world   "
#    Chain methods to: strip spaces, convert to title case, 
#    replace 'o' with 'O'
#    Do it in one line
#    Print original and result.

messy_text = "   HELLO world   "
print("Original: '" + messy_text + "'")
print("After chaining: '" + messy_text.strip().title().replace('o', 'O') + "'")

# ----------------------------------------------------------

# ==========================================================
# PART B:   Escape Sequences
# ==========================================================

# Q3: Escape sequences demonstration
#    Create strings using escape sequences:
#    - Newline: Print "Hello" and "World" on seperate lines
#    - Tab: Print "Name:\tJohn"
#    - Backslash: Print "C:\Users\Desktop"
#    - Quotes: Print She said "Hello"

print("Hello\nWorld")
print("Name:\tRobert")
print("C:\\Users\\Desktop")
print('She said "Hello"')

# ----------------------------------------------------------

# Q4: Multi-line string with escape sequences
#    Create a formatted receipt using escape sequences:
#    Use \n for new lines, \t for tabs
#    Include: Store name, items with prices, total.

print("================================")
print("\t   PYTHON STORE")
print("================================")
print("Item\t\t\tPrice")
print("--------------------------------")
print("Laptop\t\t\t$999.99")
print("Mouse\t\t\t$25.50")
print("Keyword\t\t\t$75.00")
print("--------------------------------")
print("Total:\t\t\t$1100.49")
print("================================")

# ----------------------------------------------------------

# Q5: Raw strings and escape sequences
#    Create two versions of a file path:
#    1. Using escape sequences: C:\Users\Desktop\file.txt
#    2. Using raw string (r"...")
#    Also create a regex pattern using raw string: 
#    r"\d{3}-\d{3}-\d{4}"
#    Print all three.
