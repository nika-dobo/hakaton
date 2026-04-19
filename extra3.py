# Extra 3: Check if a List Contains a Value
# Instructions:
#  Check if the number 5 exists in a list. If it does, store True in result, otherwise store False.
# Test Cases:
#  assert result == True when list = [1, 2, 5, 7]
#  assert result == False when list = [0, 3, 4]

def contains_value(list):
    return 5 in list

print(contains_value([1, 2, 5, 7]))
print(contains_value([0, 3, 4]))