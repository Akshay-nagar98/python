#Write a Python program to combine two dictionary adding values for common keys
#d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400}
#Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).


from collections import Counter

def combine_dicts(d1, d2):
    # Use Counter to add values for common keys
    combined = Counter(d1) + Counter(d2)
    return combined

# Example dictionaries
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Combine dictionaries and print the result
combined_dict = combine_dicts(d1, d2)
print("Combined dictionary with summed values:")
print(combined_dict)
