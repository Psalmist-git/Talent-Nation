def list_sum(numbers):
    if list == []:
        return 0
    total = 0
    for number in numbers:
        total += number
    return total

print(list_sum([2, 4, 6, 8]))
