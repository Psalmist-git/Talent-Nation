def count_occurrencies(numbers, target):
    if not numbers:
        return [0]
    
    chap = 0

    for number in numbers:
        if number == target:
            chap  += 1

    return chap

target_number = ([2, 5, 2, 8, 2])
chap  = count_occurrencies(target_number,2)
print(chap)


