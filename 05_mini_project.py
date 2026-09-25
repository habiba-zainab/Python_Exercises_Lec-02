"""

===========================================================
   LECTURE 02 - SET 05 : MINI PROJECT
   Topics :     All Topics are included
============================================================

"""

# ===========================================================
#               EMAIL VALIDATOR
# ===========================================================

# ----------------------------------------------------------
#    STEP 01:     Email Info
# ----------------------------------------------------------

print("\n--- Extract Email Parts ---")

email = "Jessica@gmail.com"
print("Email:", email)

# String Methods: split
parts = email.split('@')
username = parts[0]
domain = parts[1]

# Indexing & Slicing
print("First letter:", email[0])
print("Last letter:", email[-1])
print("Username:", username)
print("Domain:", domain[:5])  # gmail

# ----------------------------------------------------------
#    STEP 02:     Validate Email
# ----------------------------------------------------------

print("\n--- Check Valid ---")

