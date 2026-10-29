def missing_number(numbers):
    char = len(numbers)
    expected_sum = char * (char + 1) // 2
    actual_sum = sum(numbers)
    return expected_sum - actual_sum

print(missing_number([3, 0, 1]))
print(missing_number([0, 1]))
print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))