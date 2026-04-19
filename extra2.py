# Extra 2: Find the Largest Number in a List
# Instructions:
#  Given a list of numbers, find the largest number and store it in result.
# Test Cases:
#  assert result == 9 when list = [3, 7, 9, 2]
#  assert result == 5 when list = [5, 3, 1]

def largest_number(list):
    return max(list)

print(largest_number([3, 7, 9, 2]))
print(largest_number([5, 3, 1]))