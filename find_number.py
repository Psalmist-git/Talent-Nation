def find_number(numbers, target):

    chap = 0

    while chap < len(numbers):
        if numbers[chap] == target:
            return chap
        chap += 1
        
    return -1

print(find_number([10, 25, 30, 45], target = 30))
print(find_number([5, 8, 5, 9], target = 5))
print(find_number([10, 20, 30], target = 99))

