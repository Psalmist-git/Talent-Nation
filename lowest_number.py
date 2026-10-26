def find_smallest(numbers):

    if not numbers:
        return "None"
    
    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest

smallest_number = ([3, 41, 56, 21, 76, 9])
i = find_smallest(smallest_number)
print(i)
