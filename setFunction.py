# Define two sets
set_E = {0, 1, 2, 3, 4, 5, 6}
set_N = {2, 4, 6, 8}

# Perform set operations
union_result = set_E.union(set_N)
intersection_result = set_E.intersection(set_N)
difference_result = set_E.difference(set_N)
symmetric_difference_result = set_E.symmetric_difference(set_N)

# Display the results
print(f"Union of E and N is {union_result}")
print(f"Intersection of E and N is {intersection_result}")
print(f"Difference of E and N is {difference_result}")
print(f"Symmetric difference of E and N is {symmetric_difference_result}")
