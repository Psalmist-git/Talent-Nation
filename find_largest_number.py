def find_largest(numbers):

    if not numbers:
        return "None"
    
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest

largest_number = ([3, 41, 56, 21, 76, 9])
i = find_largest(largest_number)
print(i)


