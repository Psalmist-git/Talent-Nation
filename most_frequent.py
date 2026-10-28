def most_frequent(numbers):
    if not numbers:
        return None

    frequencies = {}
    for num in numbers:
        frequencies[num] = frequencies.get(num, 0) + 1

    max_count = -1
    best_num = None

    for num in numbers:
        if frequencies[num] > max_count:
            max_count = frequencies[num]
            best_num = num

    return best_num

print(most_frequent([2, 5, 2, 8, 2, 5]))
print(most_frequent([4, 7, 7, 4]))
