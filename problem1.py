def calculate_sum(limit):
    # Initialize the sum
    total_sum = 0

    # Loop through each number from 1 to limit - 1
    for number in range(limit):
        # Check if the number is a multiple of 3 or 5
        if number % 3 == 0 or number % 5 == 0:
            # Add the number to total sum
            total_sum += number

    print(f"The sum of all multiples of 3 and 5 below {limit} is {total_sum}")

# Define the limit
limit = 1000

# Call the function with the limit
calculate_sum(limit)



