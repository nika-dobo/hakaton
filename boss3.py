# Boss 3: Password Strength Checker 
# Instructions:
#  Create a function that checks the strength of a given password.
# The password is considered:
# "Weak" if its length is less than 6
# "Medium" if:
# length is at least 6
# contains at least 1 letter and 1 digit
# "Strong" if:
# length is at least 8
# contains at least 1 uppercase letter
# contains at least 1 lowercase letter
# contains at least 1 digit
# The function should return the corresponding strength as a string.
# Examples:
#  "abc" → "Weak"
#  "abc123" → "Medium"
#  "Abc12345" → "Strong"

def password_strength(password):
    length = len(password)
    has_lower = False
    has_upper = False
    has_digit = False
    
    for c in password:
        if c.islower():
            has_lower = True
        elif c.isupper():
            has_upper = True
        elif c.isdigit():
            has_digit = True
            
    has_letter = has_lower or has_upper
    
    if length >= 8 and has_lower and has_upper and has_digit:
        return "Strong"
    elif length >= 6 and has_letter and has_digit:
        return "Medium"
    else:
        return "Weak"

print(password_strength("abc"))
print(password_strength("abc123"))
print(password_strength("Abc12345"))