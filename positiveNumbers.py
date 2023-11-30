def print_positive_numbers(input_list):
    positive_numbers = [num for num in input_list if num > 0]
    print(f"Input: {input_list} Output: {positive_numbers}")

# Example 1
list1 = [12, -7, 5, 64, -14]
print_positive_numbers(list1)

# Example 2
list2 = [12, 14, -95, 3]
print_positive_numbers(list2)
