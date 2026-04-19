# Task 10: Sum of Even Numbers from 1 to 10
# Instructions:
#  Use a for loop with range() to calculate the sum of all even numbers from 1 to 10 and store it in result.
# Test Cases:
#  assert result == 30

def sum_even_numbers():
    result = 0
    for i in range(1, 11):
        if i % 2 == 0:
            result += i
    return result

print(sum_even_numbers())


jhgjhghj