def reverse_list(items):
    if not list:
        return []

    reversed_items = []
    
    char = len(items) -1
    while char >= 0:
        reversed_items = reversed_items + [items[char]]
        char -= 1

    return reversed_items
    
        
target_number = [1, 2, 3, 4]
target_alpha = ["a", "b", "c", "d"]

print(reverse_list(target_number)) 
print(reverse_list(target_alpha))