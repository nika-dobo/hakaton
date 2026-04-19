# Task 6: Number Comparison
# Instructions:
#  Compare if a is greater than b and store the result in result.
# Test Cases:
#  assert result == True when a = 5, b = 3
#  assert result == False when a = 2, b = 7

def number_comparison(a, b):
    if a > b:
        return True
    else:
        return False

print(number_comparison(5, 3))
print(number_comparison(2, 7))