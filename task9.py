# Task 9: Check if Number is Positive
# Instructions:
#  Check if a number a is greater than 0. Store True in result if it is, otherwise store False.
# Test Cases:
#  assert result == True when a = 4
#  assert result == False when a = -2

def check_positive(a):
    if a > 0:
        return True
    else:
        return False

print(check_positive(4))
print(check_positive(-2))