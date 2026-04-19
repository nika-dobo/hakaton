# Task 7: Range Sum with for Loop
# Instructions:
#  Use a for loop and range() to compute the sum of numbers from 0 to 7 and store it in result.
# Test Cases:
#  assert result == 28

def range_sum():
    result = 0
    for i in range(0, 8):
        result += i
    return result

print(range_sum())