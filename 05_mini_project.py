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

email = "Jessica.nia@gmail.com"
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

# String Method & Function
at_count = email.count('@')
length = len(email)

# Conditions
if at_count == 1 and length > 5:
    print("✓ Valid Email")
else:
    print("✗ Invalid Email")

# ----------------------------------------------------------
#    STEP 03:     Username Generator
# ----------------------------------------------------------

print("\n--- Create Username ---")

# String Methods
name_parts = username.split('.')

# Indexing
option1 = name_parts[0][0] + name_parts[1]  # jnia
option2 = username.replace('.', '_')        # jessica_nia

print("Option 1: ", option1)
print("Option 2: ", option2)

# ----------------------------------------------------------
#    STEP 04:     Password Checker
# ----------------------------------------------------------

print("\n--- Password Check ---")

password = "Nia1jess"
print("Password: ", password)

# String Functions & Methods
length = len(password)
has_upper = any(c.isupper() for c in password)
has_number = any(c.isdigit() for c in password)
