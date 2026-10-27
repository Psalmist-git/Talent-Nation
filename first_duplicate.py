def first_duplicates(numbers):
    if not numbers:
        return None

    char = set()

    for number in numbers:
        if number in char:
            return number

        char.add(number)

    return None

print(first_duplicates([4, 7, 2, 7, 5, 4]))  
print(first_duplicates([1, 2, 3, 4]))  
print(first_duplicates([5, 5, 3])) 
