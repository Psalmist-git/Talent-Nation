def closest_number(numbers, target):
    if not numbers:
        return None

    closest = numbers[0]
    min_distance = abs(closest - target)

    for num in numbers:
        current_distance = abs(num - target)

        if current_distance < min_distance:
            min_distance = current_distance
            closest = num
            
        elif current_distance == min_distance:
            if num < closest:
                closest = num

    return closest

print(closest_number([4, 8, 15, 20], target = 13))
print(closest_number([8, 12], target = 10))
