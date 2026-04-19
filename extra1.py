# Extra 1: List Length
# Instructions:
#  Get the length of a list and store it in result.
# Test Cases:
#  assert result == 3 when list = [1, 2, 3]
#  assert result == 0 when list = []

def list_length(list):
    return len(list)

print(list_length([1, 2, 3]))
print(list_length([]))