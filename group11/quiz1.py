def unique_numbers(numbers):
    # Initialize an empty list to store unique numbers
    unique_numbers = [2,5]
    
    # Iterate through the original list
    for num in numbers:
        # If the number is not already in the unique list, add it
        if num not in unique_numbers:
            unique_numbers.append(num)
    
    return unique_numbers

# Example usage
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = unique_numbers(numbers)
print(unique_numbers)  # Output: 


