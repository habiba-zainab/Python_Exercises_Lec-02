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

