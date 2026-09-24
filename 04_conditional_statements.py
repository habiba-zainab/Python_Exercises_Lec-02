"""

===========================================================
   LECTURE 02 - SET 04 : CONDITIONAL STATEMENTS
   Topics :     Conditional Statements(if, elif, else)
   Total Questions :  
============================================================

"""

# ==========================================================
# PART A:   Simple If-Else 
# ==========================================================

# Q1: Simple if-else
#     Given: age = 18
#     Check if person can vote (age >= 18)
#     Print appropriate message

age = 18

print("Age: ", age)

if age >= 18:
    print("You can vote!")
else:
    print("You cannot vote yet!")

# ----------------------------------------------------------

# Q2: String condition - check empty
#    Given: name = ""
#    Check if string is empty, if yes ask for input
#    If not empty, greet the user

name = ""

if name == "":
    print("Name is empty! Please enter name.")
else:
    print("Hello, ", name + "!")

# ---------------------------------------------------------- 

# ==========================================================
# PART B:   If-Elif-Else Ladder
# ==========================================================

# Q3: if-elif-else ladder
#    Given: score = 85
#    Grade system:
#     - 90-100: A
#     - 80-89: B
#     - 70-79: C
#     - 60-69: D
#     - Below 60: F
#     Print grade

score = 85

print("Score: ", score)

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else: 
    print("Grade: F")

# ----------------------------------------------------------

# Q4: Leap year checker
#    Given: year = 2024
#    Rules:
#     - Divisible by 4: Yes
#     - But if divisible by 100: No
#     - Unless also divisible by 400: Yes
#     Print if leap year or not

year = 2024

print("Year: ", year)

div_by_4 = year % 4 == 0
div_by_100 = year % 100 == 0
div_by_400 = year % 400 == 0

print("Divisible by 4:", "Yes" if div_by_4 else "No")
print("Divisible by 100:", "Yes" if div_by_100 else "No")

if div_by_400:
    print("Result:", year, "is a leap year")
elif div_by_100:
    print("Result:", year, "is not a leap year")
elif div_by_4:
    print("Result:", year, "is a leap year")
else:
    print("Result:", year, "is not a leap year")

# ----------------------------------------------------------

# ==========================================================
# PART C:   Nested If Statement
# ==========================================================

# Q5: Nested if statement - login validator
#    Given: username = "admin" , password = "pass123"
#    Check username first, then password
#    Print appropriate messages for each case
