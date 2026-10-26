def count_even(numbers):
    
    count = 0

    for number in numbers:
        if number % 2 == 0:
            count += 1

    return count

print(count_even([1, 2, 3, 4, 6]))


    





























def count_even(numbers):
    # Initialize a variable to keep track of the count
    count = 0
    
    # Loop through each number in the list
    for num in numbers:
        # Check if the number is even (remainder is 0 when divided by 2)
        if num % 2 == 0:
            count += 1
            
    return count
