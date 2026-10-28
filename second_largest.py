def find_second_largest(numbers):
    if len(numbers) < 2:
        return None

    largest = second_largest = numbers[0]
    
    has_second = False

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
            has_second = True
        elif num < largest:

            if not has_second or num > second_largest:
                second_largest = num
                has_second = True

    return second_largest if has_second else None

print(find_second_largest([10, 5, 8, 10, 3, 15]))   
print(find_second_largest([4, 4, 4]))           
print(find_second_largest([-5, -2, -8, -3]))    
