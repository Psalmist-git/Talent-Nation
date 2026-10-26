def find_number(numbers, target):
    if not numbers:
        return -1

    chap = 0

    for number in numbers:
        if number == target:
            return chap
        chap += 1
    return -1


target_number = [10, 25, 45, 30]


print(find_number(target_number, 30))
print(find_number(target_number, 25))
print(find_number(target_number, -1))

