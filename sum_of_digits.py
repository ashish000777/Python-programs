def sum_of_digits(number):

    if number == 0:
        return 0  # Handle the edge case of 0

    sum_of_digits = 0
    absolute_value = abs(number)  # Ensure positive value for calculations

    while absolute_value > 0:
        digit = absolute_value % 10  # Extract the last digit
        sum_of_digits += digit
        absolute_value //= 10  # Remove the last digit

    return sum_of_digits

# Example usage
number = int(input("Enter the number: "))
result = sum_of_digits(number)
print("The sum of digits in", number, "is", result)  # Output: The sum of digits in -12345 is 15
