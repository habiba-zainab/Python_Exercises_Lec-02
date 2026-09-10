"""

===========================================================
   LECTURE 02 - SET 01 : BASICS OF STRINGS
   Topics : Strings, Escape Sequences & String Methods  
   Total Questions :  08
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

print("With escapes: C:\\Users\\Desktop\\file.txt")
print("Raw string:", r'C:\Users\Desktop\file.txt')
print("Regex pattern:", r'\d{3}-\d{3}-\d{4}')

# ----------------------------------------------------------

# ==========================================================
# PART C:   String Methods
# ==========================================================

# Q6: Basic string methods - Case conversion
#    Given: text = "python programming"
#    Convert to: uppercase, lowercase, title case, capitalize
#    Print each result with label.

text = "python programming"

print("Original:", text)
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Title:", text.title())
print("Capitalize:", text.capitalize())

# ----------------------------------------------------------

# Q7: String replace methods
#    Given: sentence = "I love Java programming"
#     Replace "Java" with "Python"
#     Replace all spaces with underscores
#     Print original and both modified versions.

sentence = "I love Cpp programming"

print("Original:", sentence)
print("After replace:", sentence.replace('Cpp', 'Python'))
print("With underscore:", sentence.replace(' ', '_'))

# ----------------------------------------------------------

# Q8: String strip methods
#   Given: messy = "   Hello Python   "
#   Use strip(), lstrip(), rstrip() to clean it
#   Print original length and cleaned length.

messy = "   Hello Python   "

print("Original: '", + messy +"' (Length:", len(messy), ")" )
print("strip(): '" + messy.strip() + "' (Length:", len(messy.strip()), ")")
print("lstrip(): '" + messy.lstrip() + "' (Length:", len(messy.lstrip()), ")")
print("rstrip(): '" + messy.rstrip() + "' (Length:", len(messy.rstrip()), ")")

# ----------------------------------------------------------