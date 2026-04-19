# Boss 4: Nested List Maximum Finder 📊
# Instructions:
#  You are given a nested list that may contain integers or other lists.
#  Your task is to find the maximum number in the entire structure using recursion.
# Examples:
#  [1, [2, 3], [4, [5, 10]]] → 10
#  [[-1, -5], [-3, [-10]]] → -1

def nested_list_maximum(nested_list):
    if type(nested_list) == int:
        return nested_list
        
    biggest = nested_list_maximum(nested_list[0])
    
    for item in nested_list:
        item_max = nested_list_maximum(item)
        if item_max > biggest:
            biggest = item_max
            
    return biggest

print(nested_list_maximum([1, [2, 3], [4, [5, 10]]]))
print(nested_list_maximum([[-1, -5], [-3, [-10]]]))